import os
from flask import Flask, flash, request, redirect, url_for
from resumeapp.resume.forms import ResumeForm, SkillsForm, TitlesForm, TitlesAddForm
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.emailconfig import sendEmail
from resumeapp.resume.redisdata import (addValueToSet, findAllSkillsInSet, findKeysAndValuesInHash, 
                                        addValueToHash, findAllValuesInHash)
from resumeapp.resume.s3integration import uploadFileToS3
from resumeapp.resume.filedatabase import updateFileDatabase
import re
import pandas as pd

resume = Blueprint('resume',__name__)

UPLOAD_FOLDER = 'F:\Python\1. Flask\1. Resume Screening\1. Final'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

common_ngram = ''

@resume.route('/home', methods=['GET','POST'])
@login_required
def create_post():
    form = ResumeForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        emailid = form.emailid.data
        fileName = form.fileName.data
        fileName.save(fileName.filename)
        extractedText = extractTextFromPDF(fileName.filename)
        file_url, dateToday = uploadFileToS3(fileName.filename)
        (relevantSkills,skillsMatched, skillsNotFound, jdProfile, resumeProfile, pointsFromProfile, matchPercent2, ngrams) = scoringAndExperienceCheck(
                                                                            title, extractedText, description)
        profileStatus = "Match" if pointsFromProfile == 20 else "Mismatch"
        #fileName.save(os.path.join(app.config['UPLOAD_FOLDER'], fileName))
        htmlPage = render_template('output.html',form=form,
                                    title = title,
                                    description = description,
                                    fileName = fileName.filename,
                                    relevantSkills = ", ".join(relevantSkills),
                                    skillsMatched = ", ".join(skillsMatched),
                                    skillsNotFound = ", ".join(skillsNotFound),
                                    profileStatus = profileStatus,
                                    matchPercent2 = matchPercent2,
                                    emailid = emailid,
                                    ngrams = ngrams,
                                )
        sendEmail(emailid, fileName.filename, htmlPage)
        global common_ngram
        common_ngram = ngrams
        print("common_ngram", common_ngram)
        print("ngrams", ngrams)
        updateFileDatabase(title, description, emailid, fileName.filename, extractedText, file_url,
                           relevantSkills, skillsMatched, skillsNotFound, pointsFromProfile,
                           matchPercent2, ngrams, dateToday)
        #deletefilefromec2
        return htmlPage
    return render_template('index.html',form=form)

@resume.route('/scoring', methods=['GET','POST'])
@login_required
def scoring_report():
    if request.method == "POST":
        skillsIndex = request.form.getlist('mycheckbox')
        skillsIndex = [int(i) for i in skillsIndex]
        skillsToBeAdded = []
        print("common ngrams", common_ngram)
        print("skillsIndex", skillsIndex)
        for i in skillsIndex:
            print("i", i)
            skillsToBeAdded.append(common_ngram[i])
        for j in skillsToBeAdded:
            addValueToSet("SkillsStaging", j)
        
        return render_template('skillsadded2.html', skillsToBeAdded = ", ".join(skillsToBeAdded))
    return 'Not Done'

common_skill = ''

@resume.route('/skills', methods=['GET','POST'])
@login_required
def find_skills():
    form = SkillsForm()
    
    skillsFound = "Search for a skill"
    if form.validate_on_submit():
        skill = form.skill.data
        skill = skill.lower()
        #search for the skill in database
        allSkills = findAllSkillsInSet("Skills") + findAllSkillsInSet("SkillsStaging")
        print(allSkills)
        allSkills = [i.lower() for i in allSkills]
        if skill in allSkills:
            skillsFound = "Skill available in database, search for another skill"
            print("present")
        else:
            print("absent")
            skillsFound = "Skill unavailable in database"
        global common_skill
        common_skill = skill
    return render_template("findskills.html", form = form, skillsFound = skillsFound,
                           form_action_url = url_for('resume.add_skill'))

@resume.route('/addskill', methods=['GET','POST'])
@login_required
def add_skill():
    addValueToSet("SkillsStaging", common_skill)
    return render_template('skilladded.html', skillsToBeAdded = common_skill)

commontitlesDict = {}

@resume.route('/jobtitles', methods=['GET','POST'])
@login_required
def find_title():
    form = TitlesForm()
    
    titlesFound = "Search for a job title"
    if form.validate_on_submit():
        title = form.title.data
        title = title.lower()
        titlesDict = {}
        #search for the job titles in database
        allTitles = {**(findKeysAndValuesInHash("jobTitles")), **(findKeysAndValuesInHash("jobTitlesStaging"))}
        print(allTitles)
        #allTitles = [i.lower() for i in allTitles]
        for i in allTitles: #allTitles -> 
            if title in i.lower():
                print("title", title)
                print("i", i)
                domain = allTitles[i]
                titlesDict[i] = domain 
                titlesFound = "Title available in database:"
                print("present")
                
        if len(titlesDict)==0:
            print("absent")
            titlesFound = "Title unavailable in database"
        global commontitlesDict
        commontitlesDict = titlesDict
        return render_template("findtitles.html", form = form, titlesFound = titlesFound, titlesDict = titlesDict)
    return render_template("findtitles.html", form = form, titlesFound = titlesFound)

@resume.route('/addjobtitle', methods=['GET','POST'])
@login_required
def add_titles():
    form = TitlesAddForm()
    
    if form.validate_on_submit():
        title = form.title.data
        domain = form.domain.data
        addValueToHash("jobTitlesStaging", title, domain)
        message = "Successfully added to database: " + title + ":" + domain
        return render_template('titlesaddedsuccess.html', title = title, domain = domain)
    
    return render_template('titlesadded.html', form = form)

@resume.route('/userhistory', methods=['GET','POST'])
@login_required
def userHistory():
    user = current_user.id
    fileNames = findAllSkillsInSet(str(user) + "files")
    details = []
    for i in fileNames:
        data = findKeysAndValuesInHash(i)
        print(type(data))
        details.append(data)
    df = pd.DataFrame(details)
    print(df)
    #page = request.args.get('page', 1, type=int)
    #detailsPaginated = details.paginate(page=page, per_page=10)
    #for i in range(0, len(data)):
    
    return render_template('userhistory.html', df = df)