import os, sys
sys.path.insert(0, os.path.abspath("../../"))

import pandas as pd
from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.findkeywords import findMatchingKeywords
from resumeapp.resume.redisdata import findAllSkillsInSet

import warnings
warnings.filterwarnings("ignore")


#single i
i = 0

#find the skills and experience
df = pd.read_excel("JD.xlsx")

jobProfile = df["Title"][i]
jobDescription = df["Description"][i]
filename = 'profiles/' + df["Resume"][i] + ".pdf"
extractedText = extractTextFromPDF(filename)
languages = findAllSkillsInSet("Skills")
ngrams = findMatchingKeywords(extractedText, jobDescription, languages)
print(ngrams)

#(relevantSkills,skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
#            secondarySkillsInRelevantSkills, pointsFromPrimarySkills, 
#            pointsFromSecondarySkills, matchPercent) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)