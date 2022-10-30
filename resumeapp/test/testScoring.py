import os, sys
sys.path.insert(0, os.path.abspath("../../"))

from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.findExperienceText import findSubtextForExperienceSearch
from resumeapp.resume.findExperience import findDatesFromText
from resumeapp.resume.cleanText import cleanTextUsingNLP
import pandas as pd
import warnings

i = 99

df = pd.read_excel("JD.xlsx")

jobDescription = df["Description"][i]
jobProfile = df["Title"][i]
try:
    filename = "profiles/" + df["Resume"][i] + ".pdf"
    extractedText = extractTextFromPDF(filename)
except:
    filename = "profiles/" + df["Resume"][i] + ".docx"
    extractedText = extractTextFromPDF(filename)

jobDescription = extractedText
relevantSkills,skillsMatched, skillsNotFound, jobProfile, profile, pointsFromProfile, matchPercent2 = scoringAndExperienceCheck(
                                                jobProfile, extractedText, jobDescription)

print("relevantSkills", relevantSkills)
print("skillsMatched", skillsMatched)
print("skillsNotFound", skillsNotFound)
print("jobProfile", jobProfile)
print("profile", profile)
print("pointsFromProfile", pointsFromProfile)
print("matchPercent2", matchPercent2)