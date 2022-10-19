import pandas as pd
from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.readpdf import extractTextFromPDF
import warnings
warnings.filterwarnings("ignore")


#single i
i = 0

#find the skills and experience
df = pd.read_excel("JD.xlsx")

jobProfile = df["Title"][i]
jobDescription = df["Description"][i]
filename = 'Resumes/Profile10/' + df["Resume"][i] + ".pdf"
extractedText = extractTextFromPDF(filename)

for j in jobDescription:
    if j in extractedText:
        print(j)

#(relevantSkills,skillsMatched, skillsNotFound, pointsFromProfile, primarySkillsInRelevantSkills,
#            secondarySkillsInRelevantSkills, pointsFromPrimarySkills, 
#            pointsFromSecondarySkills, matchPercent) = scoringAndExperienceCheck(jobProfile, extractedText, jobDescription)