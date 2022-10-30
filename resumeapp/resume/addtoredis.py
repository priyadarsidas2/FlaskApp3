import os, sys
sys.path.insert(0, os.path.abspath("../../"))

import pandas as pd
from redisdata import (addValueToSet, removeValueFromSet, findValueInSet, 
                                        addValueToHash, removeValueFromHash, findValueInHash)

"""Build skillslist on redis
df = pd.read_excel("SkillsList.xlsx")
for i in df["Skills"]:
    message = addValueToSet("Skills", i)
    print(message)
"""

#build hash - titles vs skills list on redis
df2 = pd.read_excel("JobTitles.xlsx")
for i in range(0, len(df2["Job Titles"])):
    #print(df2["Job Titles"][i], df2["Skill"][i])
    message = addValueToHash("jobTitles", df2["Job Titles"][i], df2["Skill"][i])
    print(message)
    