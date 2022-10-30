import os, sys
sys.path.insert(0, os.path.abspath(".."))
import pandas as pd
from resume.redisdata import (addValueToSet, removeValueFromSet, 
                findValueInSet, addValueToHash, removeValueFromHash, 
                findValueInHash, findKeysInHash, findKeysAndValuesInHash,
                findAllSkillsInSet)

"""testing findKeysInHash
keys  = findKeysInHash("jobTitles")
keysDecoded = [i.decode() for i in keys]
print(keysDecoded)
"""

"""testing findKeysAndValuesInHash
titles = findKeysAndValuesInHash("jobTitles")
print(titles)
"""

#testing findAllSkillsInSet
skills = findAllSkillsInSet("Skills")
print(skills)
