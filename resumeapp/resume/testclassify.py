from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
from findExperienceText import findSubtextForExperienceSearch
from findExperience import findDatesFromText
from cleanText import cleanTextUsingNLP
from classify import classifyJobProfile
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

extractedText = extractTextFromPDF("Good match profile for JD-4.pdf")
cleanedTextAsString = cleanTextUsingNLP(extractedText)

profile = classifyJobProfile(cleanedTextAsString)
print(profile)