from gettext import find
from resumeapp.resume.redisdata import findKeysAndValuesInHash

def classifyJobProfile(cleanedTextAsString):
    titles = {**(findKeysAndValuesInHash("jobTitles")), **(findKeysAndValuesInHash("jobTitlesStaging"))}
    """
    titles = {
        "Java/J2EE Full Stack Developer": "Java",
        "Full stack Java Developer": "Java",
        "Java Developer": "Java",
        "Sr. Java Developer": "Java",
        "Java Programmer": "Java",
        "Sr. Full Stack Java Developer": "Java",
        "Java/J2EE Developer": "Java",
        "Java/J2EE Programmer": "Java",
        "Senior Java/J2ee Developer": "Java",
        
        "Software Quality Assurance": "Testing",
        "Tester": "Testing",
        "ETL Tester": "Testing",
        "Backend SQL Tester": "Testing",
        "QA Engineer": "Testing",
        "QA Automation Engineer": "Testing", 
        "QA Selenium Engineer": "Testing",
        "Software Test Specialist": "Testing", 
        "Sr. QA Test Data Manager": "Testing",
        "Sr. Quality Assurance Analyst": "Testing", 
        "QA Tester": "Testing",
        "QA Analyst": "Testing",
        "Manual Tester": "Testing",
        "ETL/Web Application Tester": "Testing",
        "ETL/QA Tester":  "Testing",
        "ETL QA Tester":  "Testing",
        "Sr. ETL/SQL Tester": "Testing",
        "ETL/ BI Tester": "Testing",
        "SQL/ BI Tester": "Testing",
        "Automation Engineer": "Testing",
        "Manual Test / Automation Engineer": "Testing",
        "Automation/Manual Test Engineer": "Testing",
        "Software QA Engineer": "Testing",
        "Sr. QA Automation Engineer": "Testing",
        "Automation selenium Tester": "Testing",
        "Quality Assurance Engineer": "Testing",
        "Test QA Engineer": "Testing",
        "Test Automation Engineer": "Testing",
        "Automation Test Engineer": "Testing",
        "QA Manual Tester": "Testing",
        
        "ETL Architect": "ETL",
        "Senior ETL Lead Developer": "ETL", 
        "ETL Architect": "ETL",
        "Sr. ETL Developer": "ETL", 
        "ETL Lead Developer": "ETL",
        "ETL Lead": "ETL", 
        "ETL Developer": "ETL",
        
        "SQL Developer": "SQL", 
        "SQL Server Developer": "SQL", 
        "SQL Report Analyst": "SQL", 
        "Data Warehouse Developer": "SQL",
        "Database Administrator": "SQL",
        "Data Engineer":"SQL",
        "Senior Data Engineer": "SQL",
        "Data Engineer III":"SQL", 
        "Sr. Data Engineer":"SQL", 
        "MSBI Analyst": "SQL",
        
        "Big Data Developer and Analyst": "Big Data", 
        "Big Data Developer": "Big Data",
        
        "Sr. Python Developer": "Python", 
        "Python Developer": "Python",
        "Jr. Python Developer": "Python",
        
        "Oracle Developer": "Oracle",
        
        "Sr.Scrum Master": "Agile", 
        "Scrum Master": "Agile",
        "Agile Coach": "Agile", 
        
        "Sr. Business Systems Analyst": "Business", 
        "Sr. Business data analyst": "Business",
        "Business data analyst": "Business", 
        "Business System Analyst": "Business",
        "Jr. Business Analyst": "Business",
        "Sr. Business Analyst": "Business",
        "BA Enterprise Data Analytics": "Business",
        "Business Analyst": "Business",
        "BA Analyst II": "Business",
        "Technical Business Analyst": "Business",
        
         "Frontend Developer": "Frontend", 
         "Front end Developer": "Frontend", 
         "Javascript Developer": "Frontend", 
         "Web Developer": "Frontend", 
         "Web UI Developer": "Frontend",
         "Mean Stack Developer": "Frontend",
         "UI Developer": "Frontend",
         "Sr. Frontend Full Stack Web Developer": "Frontend",
         "Sr. React Js": "Frontend",
         "Front End Web Developer": "Frontend",
         
         "Program Manager": "Manager", 
         "Project Manager": "Manager", 
         "Sr. Project Manager": "Manager", 
         "Senior Project Manager": "Manager",
         "Technical Program Manager": "Manager",
         "Senior Manager": "Manager",
         "Team Lead": "Manager",
         "Delivery Manager": "Manager",
         "Project Delivery Manager": "Manager",
         "Technical Product Manager": "Manager",
         "Technical Product Owner": "Manager",
         "Product Manager": "Manager",
         "Product Owner": "Manager",
         "SR. Business Analyst and Product Owner" : "Manager",
         
         "DEVOPS ENGINEER": "Devops",
         "LINUX ADMIN": "Linux",
         "Linux Engineer": "Linux",
         "System Administrator": "Linux",
         "Network system administrator": "Linux",
         
         "R12 Application Developer": "Oracle", 
         "Oracle Cloud Consultant": "Oracle",
         "Oracle Apps ERP Financial": "Oracle", 
         "EBS Financial Developer":"Oracle",
         "Oracle ERP Financials": "Oracle", 
         "EBS Application Developer": "Oracle",
         "EBS Consultant": "Oracle",
         
         "SharePoint Architect": "SharePoint",
         "SharePoint Search Solutions Architect":"SharePoint",
         "SharePoint Architect":"SharePoint", 
         "SharePoint Developer":"SharePoint",
         "SharePoint Consultant": "SharePoint", 
         "SharePoint Lead Consultant": "SharePoint",
         "SharePoint Business Analyst": "SharePoint", 
         "SharePoint Technical Lead": "SharePoint",
         
         "Salesforce Lightning Developer and Admin": "Salesforce", 
         "Sr.Salesforce Admin and Developer": "Salesforce", 
         "Salesforce Admin": "Salesforce", 
         "Salesforce Administrator": "Salesforce",
         "Dynamic CRM 365": "Salesforce",
         "Salesforce Business Analyst": "Salesforce",
         "Salesforce Project Manager": "Salesforce",
         
         
         "Sr. Business Intelligence Developer": "BI", 
         "SR. BI Developer": "BI",
         "Senior Business Intelligence Developer": "BI", 
         "BI Developer": "BI",
         "Sr Power BI /Tableau Developer ": "BI",
         "Power BI Lead Consultant": "BI",
         "Power BI/Tableau Developer": "BI",
         "BI Senior Analyst": "BI",
         "Lead BI Developer": "BI",
         "BI Reporting Architect ": "BI",
         "Senior Reporting Analyst": "BI",
         "Report Developer ": "BI",
         
         "SAP Consultant": "SAP",
         "Ariba Consultant": "SAP",
         "SAP MM consultant": "SAP",
         "LEAD SAP MM": "SAP",
         "SAP MM":"SAP",
         
         "WORKDAY DEVELOPER": "Workday",
         "WORKDAY CONSULTANT": "Workday",
         "WORKDAY INTEGRATION DEVELOPER": "Workday",
         "WORKDAY HCM CONSULTANT": "Workday",
         "WORKDAY SYSTEMS ANALYST": "Workday",
         
         "Microsoft D365 Admin/Developer": "D365",
         "Microsoft D365 Admin": "D365",
         "Microsoft D365 Developer": "D365",
         "MS Dynamics CRM Admin / Developer": "D365",
         "MS Dynamics CRM Admin": "D365",
         "MS Dynamics CRM Developer": "D365",
         "CRM Admin Consultant": "D365",
         
         "Dot.Net Developer": ".net",        
         
         "Data Analyst": "Data Analyst",
         
         "Sr. Network/Wireless/Penetration Security Engineer": "Security",
         "WAN Migration Engineer":  "Security",
         "Network Engineer": "Security",
         "Information Security Analyst": "Security",
         "Security Architecture & Engineering": "Security",
         "Project Coordinator & IAM Analyst": "Security",
         "Cyber Security Team": "Security",
         "Network Operations /IAM Security": "Security",
         "Senior Security Analyst": "Security",
         "Senior IS Analyst": "Security",
         
         "ServiceNow BA": "ServiceNow",
         
         
         "Azure Data Engineer": "Azure",
         
         "Trade Working Capital and S&OP": "Supply",
         "Supply Chain Digital Transformation" : "Supply",
         "Supply Chain Transformation": "Supply",
         "Demand to Delivery Transformation": "Supply",
         "Supply Chain": "Supply",
         
         "Third Party Risk Analyst": "Risk",
         "Information Secuirty Analyst": "Risk",
         "Senior Risk Analyst": "Risk",
         "Senior Operational Risk Lead Analyst": "Risk",
         
    }
    
    
    frequencyOfTitles = {
                        "Java": 0, "Testing": 0, "ETL": 0, "SQL": 0, "Big Data": 0,
                        "Python": 0, "Oracle": 0, "Business": 0, "Frontend": 0,
                        "Manager": 0, "Devops": 0, "Linux": 0, "Oracle": 0, "SharePoint": 0,
                        "Salesforce": 0, "BI": 0, "SAP": 0, "Workday": 0, "D365": 0, ".net": 0,
                        "Data Analyst": 0, "Security": 0, "ServiceNow": 0,
                        "Azure": 0, "Supply": 0, "Risk": 0, "Agile": 0
                         }
    """
    domains = list(set(titles.values()))
    frequencyOfTitles = {}
    
    for i in domains:
        frequencyOfTitles[i] = 0
    
    print("frequencyOfTitles", frequencyOfTitles)
    
    for title in titles:
        countOfOccurances = cleanedTextAsString.count(title.lower())
        #print(countOfOccurances)
        thisTitle = titles[title]
        frequencyOfTitles[thisTitle] += countOfOccurances

    print(frequencyOfTitles)
    max_value = max(frequencyOfTitles.values())
    keymax = [k.lower() for k,v in frequencyOfTitles.items() if v == max_value] if max_value != 0 else []
    #keymax = max(frequencyOfTitles, key = lambda x: frequencyOfTitles[x])
    return keymax
