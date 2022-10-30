import os, sys
sys.path.insert(0, os.path.abspath("../../"))

from resumeapp.resume.scoringAndExperience import scoringAndExperienceCheck
from resumeapp.resume.readpdf import extractTextFromPDF
from resumeapp.resume.cleanText import cleanTextUsingNLP
from resumeapp.resume.classify import classifyJobProfile
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

extractedText = extractTextFromPDF("profiles/Good match Profile_Senior UI Developer JD3.pdf")
cleanedTextAsString = cleanTextUsingNLP(extractedText)

text = extractedText.lower()
text = text.replace("  ", " ")
#print(text)
profile = classifyJobProfile(text)
#print(text.count("web ui developer"))
#print(text.count("mean stack developer"))
print(profile)
