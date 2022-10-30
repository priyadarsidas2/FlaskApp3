from distutils.command.clean import clean
import os, sys
sys.path.insert(0, os.path.abspath("../../"))

from resumeapp.resume.cleanText import cleanTextUsingNLP

def findMatchingKeywords(extractedText, jobDescription, languages):
    cleanedJD = cleanTextUsingNLP(jobDescription)
    cleanedJD = cleanedJD.lower()
    cleanedResume = cleanTextUsingNLP(extractedText)
    cleanedResume = cleanedResume.lower()
    
    listOfKeywords = []
    
    
    for j in cleanedJD.split():
        if j + " " in cleanedResume:
            listOfKeywords.append(j)
    
    cleanedJDToList = cleanedJD.split()
    print("cleanedJDToList", cleanedJDToList)
    print("cleanedResume", cleanedResume)

    for k in range(0, len(cleanedJDToList)-1):
        if (cleanedJDToList[k] + " " + cleanedJDToList[k+1] + " ") in cleanedResume:
            listOfKeywords.append(cleanedJDToList[k] + " " + cleanedJDToList[k+1])
            
    for l in range(0, len(cleanedJDToList)-2):
        if (cleanedJDToList[l] + " " + cleanedJDToList[l+1] + " " + cleanedJDToList[l+2] + " ") in cleanedResume:
            listOfKeywords.append(cleanedJDToList[l] + " " + cleanedJDToList[l+1] + " " + cleanedJDToList[l+2])
    
    newKeywords = list(set([i for i in listOfKeywords if i not in languages]))
    
    return newKeywords