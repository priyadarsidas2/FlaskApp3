def addSimilarSkills(skills):
    listOfSkills = [
                    ["qa", "quality assurance", "testing", "test", "quality", "automation", "tester"],
                    ["bi", "business intelligence"],
                    ["react", "react js", "frontend", "javascript", "mean", "ui", "front end"],
                    ["manager", "owner", "lead", "ecommerce"],
                    ["scrum", "agile"],
                    ["ariba", "SAP"],
                    ["strategy", "security", "linux"],
                    ["data", "sql"],
                    ["adf", "azure data factory"]
                    ]
    skills = [i.lower() for i in skills]
    addedSkills = skills
    for i in listOfSkills:
        for j in i:
            if j.lower() in skills:
                addedSkills.extend(i)
                
    return list(set(addedSkills))

#if __name__ == "__main__":
#    skills = addSimilarSkills(["security", "data"])
#    print(skills)