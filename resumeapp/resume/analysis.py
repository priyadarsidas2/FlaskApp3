import pandas as pd
from readpdf import extractTextFromPDF
from addskills import addSimilarSkills

df = pd.read_excel("JD.xlsx")
finalKeywordsList = []
stringsList = []
scoreList = []

for i in range(0, 100):
    score = 0
    #single i
    #i = 7

    #find the skills and experience
    

    jobProfile = df["Title"][i]
    jobDescription = df["Description"][i]
    try:
        filename = 'profiles/' + df["Resume"][i] + ".pdf"
        extractedText = extractTextFromPDF(filename)
    except:
        filename = 'profiles/' + df["Resume"][i] + ".docx"
        extractedText = extractTextFromPDF(filename)
        
    extractedText = extractedText.lower()

    keywordsList = ['specialist', 'administrator', 'consultant', 'coach', 'security', 
                    'analytics', 'analyst', 'financials', 'ba', 'assurance', 'tester', 'lead', 
                    'engineer', 'admin', 'engineering', 'architect', 'supply chain', 'developer', 
                    'admin/developer', 'manager', 'transformation', 'owner', 'financial', 
                    'master', 'programmer']
    
    listOfStrings = []

    for i in extractedText.split("\n"):
        for j in keywordsList:
            if j + " " in i:
                #print(i)
                listOfWords = []
                listOfWords = i.split(" ")
                #print(len(listOfWords))
                for k in range(0, len(listOfWords)):
                    #print(k)
                    if listOfWords[k] == j:
                        #print(listOfWords[k])
                        listOfStrings.append(" ".join(listOfWords[k-2:k+1]))
    print(listOfStrings)
    print(filename)
    df2 = pd.read_excel("SkillsList.xlsx")
    finalKeywords = []
    listOfStrings = [i + " " for i in listOfStrings]
    for i in df2["Skills"]:
        for j in listOfStrings:
            if i.lower() + " " in j.lower():
                finalKeywords.append(i)
    stringsList.append(listOfStrings)
    finalKeywords = addSimilarSkills(finalKeywords)
    finalKeywordsList.append(finalKeywords)
    
    
    finalKeywords = list(set(finalKeywords))
    for i in finalKeywords:
        if i.lower() in jobProfile.lower():
            score = 100
    scoreList.append(score)
    
    
resumeList = df["Resume"]
titleList = df["Title"]

scoring = pd.DataFrame(zip(resumeList, titleList, stringsList, finalKeywordsList, scoreList),
                       columns=["Resume", "Title", "Matched phases", "Keywords", "Classification Score"])

scoring.to_excel("Analysis5.xlsx")