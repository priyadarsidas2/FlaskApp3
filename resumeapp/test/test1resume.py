import pandas as pd
from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
import warnings
warnings.filterwarnings("ignore")

"""
#single i
i = 83

#find the skills and experience
df = pd.read_excel("JD.xlsx")

jobProfile = df["Title"][i]
jobDescription = df["Description"][i]
try:
    filename = 'Resumes/profiles/' + df["Resume"][i] + ".pdf"
    extractedText = extractTextFromPDF(filename)
except:
    filename = 'Resumes/profiles/' + df["Resume"][i] + ".docx"
    extractedText = extractTextFromPDF(filename)
    
(relevantSkills, skillsMatched, skillsNotFound, jobProfile, profile, pointsFromProfile, 
                matchPercent2) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)
print("jobProfile", jobProfile)
print("profile", profile)
print("pointsFromProfile", pointsFromProfile)

"""
#multiple i
df = pd.read_excel("JD.xlsx")

relevantSkillsList = []
skillsMatchedList = []
skillsNotFoundList = []
jobProfileList = []
profileList = []
pointsFromProfileList = []
#primarySkillsInRelevantSkillsList = []
#secondarySkillsInRelevantSkillsList = []
#pointsFromPrimarySkillsList = []
#pointsFromSecondarySkillsList = []
#matchPercentList = []
matchPercentList2 = []

for i in range(0,100):
    #find the skills and experience
    jobProfile = df["Title"][i]
    jobDescription = df["Description"][i]
    try:
        filename = 'Resumes/profiles/' + df["Resume"][i] + ".pdf"
        extractedText = extractTextFromPDF(filename)
    except:
        filename = 'Resumes/profiles/' + df["Resume"][i] + ".docx"
        extractedText = extractTextFromPDF(filename)
    (relevantSkills, skillsMatched, skillsNotFound, jobProfile, profile, pointsFromProfile, 
     matchPercent2) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)
    relevantSkillsList.append(relevantSkills)
    skillsMatchedList.append(skillsMatched)
    skillsNotFoundList.append(skillsNotFound)
    jobProfileList.append(jobProfile)
    profileList.append(profile)
    pointsFromProfileList.append(pointsFromProfile)
    #primarySkillsInRelevantSkillsList.append(primarySkillsInRelevantSkills)
    #secondarySkillsInRelevantSkillsList.append(secondarySkillsInRelevantSkills)
    #pointsFromPrimarySkillsList.append(pointsFromPrimarySkills)
    #pointsFromSecondarySkillsList.append(pointsFromSecondarySkills)
    #matchPercentList.append(matchPercent)
    matchPercentList2.append(matchPercent2)

resumeList = df["Resume"]
titleList = df["Title"]
descriptionList = df["Description"]

scoring = pd.DataFrame(zip(resumeList, titleList, descriptionList, relevantSkillsList, skillsMatchedList,
                           skillsNotFoundList, jobProfileList, profileList, pointsFromProfileList, matchPercentList2),
                       columns=["Resume", "Title", "Description", "Relevant Skills",
                                "Skills Matched", "Skills Not Found", "Job Profile", "Profile Classified", 
                                "Points From Profile", "Match Percent 2"])

scoring.to_excel("Scoring.xlsx")
