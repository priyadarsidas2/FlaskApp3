from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
from findExperienceText import findSubtextForExperienceSearch
from findExperience import findDatesFromText
from cleanText import cleanTextUsingNLP
import pandas as pd
import warnings
import re
warnings.filterwarnings("ignore")

primarySkill = "Python"
secondarySkill = "SQL"

jobDescription = """
Python Developer responsibilities include:
Writing effective, scalable code
Developing back-end components to improve responsiveness and overall performance
Integrating user-facing elements into applications
Job brief
We are looking for a Python Developer to join our engineering team and help us develop and maintain various software products.

Python Developer responsibilities include writing and testing code, debugging programs and integrating applications with third-party web services. To be successful in this role, you should have experience using server-side logic and work well in a team.

Ultimately, you’ll build highly responsive web applications that align with our business needs.

Responsibilities
Write effective, scalable code
Develop back-end components to improve responsiveness and overall performance
Integrate user-facing elements into applications
Test and debug programs
Improve functionality of existing systems
Implement security and data protection solutions
Assess and prioritize feature requests
Coordinate with internal teams to understand user requirements and provide technical solutions
Requirements and skills
Work experience as a Python Developer
Expertise in at least one popular Python framework (like Django, Flask or Pyramid)
Knowledge of object-relational mapping (ORM)
Familiarity with front-end technologies (like JavaScript and HTML5)
Team spirit
Good problem-solving skills
BSc in Computer Science, Engineering or relevant field
"""
extractedText = extractTextFromPDF("Resume11.pdf")



"""
monthsToNum = {"jan": 1 , "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12, "sept": 9,
                  "january": 1 , "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
    
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "sept",
            "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

listOfDates1rev = []
listOfDates1 = re.findall(r'[A-Z,a-z]+\s\d{4}', extractedText)
for i in range(0, len(listOfDates1)):
    print(listOfDates1[i].split(" ")[0])
    listOfDates1[i] = listOfDates1[i].replace(",", "")
    listOfDates1[i] = listOfDates1[i].replace(".", "")
    for j in months:
        #print(j)
        if j in listOfDates1[i].split(" ")[0].lower():
            print("j", j)
            date = "1/" + str(monthsToNum[j]) + "/" + str(listOfDates1[i].split(" ")[1])
            listOfDates1rev.append(date)
            break
print(listOfDates1rev)
    
"""

matchPercent, skillsFound, skillsNotFound, experienceInYears, pointsAchieved, pointsLost, similarityPercent, totalScore = scoringAndExperienceCheck(
                                                                                primarySkill, secondarySkill, extractedText, jobDescription)
