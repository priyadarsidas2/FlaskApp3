import os, sys
sys.path.insert(0, os.path.abspath("../../"))

import numpy as np
import pandas as pd
from resumeapp.resume.cleanText import cleanTextUsingNLP
from resumeapp.resume.similar import addSimilarKeywords
from resumeapp.resume.classify import classifyJobProfile
from resumeapp.resume.simplifyprofile import simplifyJobProfile
from resumeapp.resume.redisdata import findAllSkillsInSet
from resumeapp.resume.findkeywords import findMatchingKeywords

import warnings
warnings.filterwarnings("ignore")

def scoringAndExperienceCheck(jobProfile, extractedText, jobDescription):
    languages1 = findAllSkillsInSet("Skills")
    languages1 = [i.lower() for i in languages1]
    try:
        languages2 = findAllSkillsInSet("SkillsStaging")
        languages2 = [i.lower() for i in languages2]
        languages = languages1 + languages2
    except:
        languages = languages1
    
    cleanedTextAsString = cleanTextUsingNLP(extractedText)
    cleanedTextAsString = cleanedTextAsString.lower()
    
    print(cleanedTextAsString)
    skillsFound = []
    
    for language in languages:
        if (language.lower() + " " in cleanedTextAsString or language.lower() + "\n" in cleanedTextAsString or 
            language.lower() + "," in cleanedTextAsString or language.lower() + "/" in cleanedTextAsString):
            skillsFound.append(language.lower())
    
    skillsFound = list(set(skillsFound))
    skillsFound = addSimilarKeywords(skillsFound)
    
    #finding the job profile from resume text
    profile = classifyJobProfile(extractedText.lower())
    
    #finding the skills from job description
    cleanedJD = cleanTextUsingNLP(jobDescription)
    cleanedJD = cleanedJD.lower()
    relevantSkills = []
    for language in languages:
        
        if (language.lower() + " " in cleanedJD or language.lower() + "\n" in cleanedJD or 
            language.lower() + "," in cleanedJD or language.lower() + "/" in cleanedJD):
            relevantSkills.append(language.lower())

    relevantSkills = list(set(relevantSkills))
    
    #matching skills in resume to relevant skills in job description
    skillsMatched = []

    for skill in relevantSkills:
        if skill in skillsFound:
            skillsMatched.append(skill)

    skillsMatched = list(set(skillsMatched))
            
    print("relevantSkills", relevantSkills)
    print("skillsMatched", skillsMatched)
    
    skillsNotFound = [i for i in relevantSkills if i not in skillsMatched]
    
    pointsFromProfile = 0
    jobProfile = jobProfile.lower()
    jobProfile = simplifyJobProfile(jobProfile)
    
    for word in profile:
        if word in jobProfile.lower():
            print(word)
            pointsFromProfile = 20
            break
            
    skillsFound = cleanTextUsingNLP(" ".join(skillsFound))
    skillsFound = skillsFound.split(" ")
    skillsFound = list(set(skillsFound))
    skillsFound = sorted(skillsFound)
    
    matchPercent2 = len(skillsMatched) / len(relevantSkills) * 100 if pointsFromProfile == 20 else 0
    matchPercent2 = round(matchPercent2, 2)
    ngrams = findMatchingKeywords(extractedText, jobDescription, languages)
    
    
    #printing outputs
    print("skillsFound", skillsMatched)
    print("skillsNotFound", skillsNotFound)
    print("pointsFromProfile", pointsFromProfile)
    print("matchPercent2", matchPercent2)
    print("languages", languages)
    return (relevantSkills,skillsMatched, skillsNotFound, jobProfile, profile, pointsFromProfile, matchPercent2, ngrams)
