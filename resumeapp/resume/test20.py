import pandas as pd
from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
from findExperienceText import findSubtextForExperienceSearch
from findExperience import findDatesFromText
from cleanText import cleanTextUsingNLP
import warnings
warnings.filterwarnings("ignore")

df = pd.read_excel("JDv3.xlsx")
#df['Manual Score'] = df['Manual Score'].astype(float)

for i in range(0,100):
    primarySkill = df["Primary"][i]
    secondarySkill = df["Secondary"][i]
    jobDescription = df["Description"][i]
    filename = df["Resume"][i] + ".pdf"
    extractedText = extractTextFromPDF(filename)
    matchPercent, skillsFound, skillsNotFound, experienceInYears, pointsAchieved, pointsLost, similarityPercent, totalScore = scoringAndExperienceCheck(
                                                primarySkill, secondarySkill, extractedText, jobDescription)
    experienceInYears = 0 if experienceInYears == "Could not be screened, try with a different format." else experienceInYears
    
    if primarySkill in skillsFound:
        df["Primary Found"][i] = "Yes"
    else:
        df["Primary Found"][i] = "No"
        
    if secondarySkill in skillsFound:
        df["Secondary Found"][i] = "Yes"
    else:
        df["Secondary Found"][i] = "No"
        
    df["Experience from Code"][i] = float(experienceInYears)
    otherSkills = [skill for skill in skillsFound if (skill!= primarySkill and skill != secondarySkill)]
    df["Other Skills"][i] = otherSkills
    df["Number of other skills"][i] = len(otherSkills)
    df["Score from Code"][i] = float(matchPercent)
    df["Experience from Code"][i] = experienceInYears
    #df["Scoring Error"][i] = (abs(float(df["Score from Code"][i]) - float(df["Manual Score"][i]))/ float(df["Manual Score"][i])) * 100 
    #df["Experience Error"][i] = (abs(float(df["Experience from Code"][i]) - float(df["Manual Experience"][i]))/ float(df["Manual Experience"][i])) * 100
    print()
    
df.to_excel("ScoringDoc.xlsx")
#df["Scoring Error"].mean()
#df["Experience Error"].mean()
