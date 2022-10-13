from scoringAndExperience import scoringAndExperienceCheck
from readpdf import extractTextFromPDF
from findExperienceText import findSubtextForExperienceSearch
from findExperience import findDatesFromText
from cleanText import cleanTextUsingNLP
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

extractedText = extractTextFromPDF("Resume10.pdf")

subText = findSubtextForExperienceSearch(extractedText)

experience = findDatesFromText(subText)
print(experience)