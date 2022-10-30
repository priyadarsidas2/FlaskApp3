import pandas as pd

df = pd.read_excel("Scoring.xlsx")

#match1 = df["Match Percent"]
match2 = df["Match Percent 2"]
"""
print("Scoring old")
sum1 = 0
for i in range(0, len(match1), 2):
    sum1 += df["Match Percent"][i]
    
#print(sum1)
avg1 = sum1 / (len(match1)//2)
print("Average of good profiles ", avg1)

sum2 = 0
for i in range(1, len(match1), 2):
    sum2 += df["Match Percent"][i]
    
#print(sum2)
avg2 = sum2 / (len(match1)//2)
print("Average of bad profiles ", avg2)
"""

################################################
################################################

print("Scoring New")
sum1 = 0
min1 = float("inf")
max1 = float("-inf")
for i in range(0, len(match2), 2):
    sum1 += df["Match Percent 2"][i]
    if df["Match Percent 2"][i] != 0:
        if df["Match Percent 2"][i] > max1:
            max1 = df["Match Percent 2"][i]
        if df["Match Percent 2"][i] < min1:
            min1 = df["Match Percent 2"][i]
        if df["Match Percent 2"][i] < 65:
            print(df["Resume"][i])
#print(sum1)
avg1 = sum1 / (len(match2)//2)
print("Average of good profiles ", avg1)
print("Max of good profiles ", max1)
print("Min of good profiles ", min1)

sum2 = 0
min2 = float("inf")
max2 = float("-inf")
for i in range(1, len(match2), 2):
    sum2 += df["Match Percent 2"][i]
    if df["Match Percent 2"][i] != 0:
        if df["Match Percent 2"][i] > max2:
            max2 = df["Match Percent 2"][i]
        if df["Match Percent 2"][i] < min2:
            min2 = df["Match Percent 2"][i]
    
#print(sum2)
avg2 = sum2 / (len(match2)//2)
print("Average of bad profiles ", avg2)
print("Max of bad profiles ", max2)
print("Min of bad profiles ", min2)

df["Skills Matched"] = df["Skills Matched"].astype(str)
for i in df["Skills Matched"]:
    stringi = str(i)
    stringlist = stringi.split(",")
    
    #if len(stringlist) <= 4:
    #    print(i)
    