from gettext import find
from resumeapp.resume.redisdata import findKeysAndValuesInHash

def classifyJobProfile(cleanedTextAsString):
    titles = {**(findKeysAndValuesInHash("jobTitles")), **(findKeysAndValuesInHash("jobTitlesStaging"))}
    
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
    return keymax
