from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
from findExperienceText import findSubtextForExperienceSearch
from findExperience import findDatesFromText
from cleanText import cleanTextUsingNLP
import pandas as pd
import warnings

extractedText = extractTextFromPDF("Resume6.pdf")
print(extractedText.split("\n"))
subText = findSubtextForExperienceSearch(extractedText)
for i in subText.split("\n"):
    print(i)
