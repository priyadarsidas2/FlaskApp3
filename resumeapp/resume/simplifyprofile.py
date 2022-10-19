def simplifyJobProfile(jobProfile):
    
    jobProfileRepo = {
        "react": "Frontend",
        "quality": "Testing",
        "qa": "Testing",
        "automation": "Testing",
        "scrum": "Agile",
        "ariba": "SAP",
        "mean": "Frontend",
        "ecommerce": "Manager",
        "front": "Frontend",
        "demand": "supply",
        "lead": "Manager",
        "owner": "Manager",
        "strategy": "security",
        "ui": "frontend",
        "data": "sql",
        "adf": "sql"
    }
    
    for i in ["/", "-", "_", ",", "."]:
        if i in jobProfile:
            jobProfile = jobProfile.replace(i, " ")
            
    for word in jobProfile.split():
        if word.lower() in jobProfileRepo:
            return jobProfileRepo[word.lower()]

    return jobProfile