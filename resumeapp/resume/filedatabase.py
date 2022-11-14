import flask_login
from resumeapp.resume.redisdata import addValueToSet, addValueToHash, findLengthOfHash

def updateFileDatabase(title, description, emailid, fileName, extractedText, file_url,
                           relevantSkills, skillsMatched, skillsNotFound, pointsFromProfile,
                           matchPercent2, ngrams, dateToday):
    user = flask_login.current_user.id
    print("User details")
    print(user, type(user))
    ##create hash 1 - ID, FileID
    lastID = findLengthOfHash("index")
    currentID = lastID + 1
    fileID = "file"+ str(currentID)
    addValueToHash("index", currentID, fileID)
    
    ##create hash 2 - fileID, all details
    addValueToHash(fileID, "title", title)
    addValueToHash(fileID, "description", description)
    addValueToHash(fileID, "emailid", emailid)
    addValueToHash(fileID, "fileName", fileName)
    addValueToHash(fileID, "extractedText", extractedText)
    addValueToHash(fileID, "file_url", file_url)
    addValueToHash(fileID, "relevantSkills", ", ".join(relevantSkills))
    addValueToHash(fileID, "skillsMatched", ", ".join(skillsMatched))
    addValueToHash(fileID, "skillsNotFound", ", ".join(skillsNotFound))
    addValueToHash(fileID, "pointsFromProfile", str(pointsFromProfile))
    addValueToHash(fileID, "matchPercent2", str(matchPercent2))
    addValueToHash(fileID, "ngrams", ", ".join(ngrams))
    addValueToHash(fileID, "dateToday", str(dateToday))
    addValueToHash(fileID, "user", str(user))
    
    ##create set 1 - UserID, FileID
    addValueToSet(str(user)+"files", fileID)
    
    ##create set 1 - Date, FileID
    addValueToSet(str(dateToday), fileID)
    
    ##create set 1 - Job Title, FileID
    addValueToSet(title, fileID)
    