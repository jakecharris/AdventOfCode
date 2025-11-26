'''Day 2: Red-Nosed Reports (https://adventofcode.com/2024/day/2)

You are given a series of values which represents readouts from a power plant. 
Each row is a report while each column is a power level. In order to be counted
as safe, a report must have both
    - all increasing or all decreasing levels
    - all adjacent levels change between 1 and 3.
How many safe power reports are there in the provided data?
'''

import csv

# Load report rows from input2.txt into one list
reports = []
with open ('input2.txt', newline='') as file:
    report_reader = csv.reader(file, delimiter=' ')
    for row in report_reader:
        reports.append(row)




rep = 0
safe_count = 0
while rep < len(reports[:2]):
    for row in reports[:2]:
        diffs = [int(row[i]) - int(row[i-1]) for i in range(len(row)-1, -1, -1)]
        res = []
        for dif in diffs:
            if (dif >= 1) and (dif <= 3):
                res.append(1)
            elif (dif <= -1) and (dif >= -3):
                res.append(0)
            elif (dif == 0) or (abs(dif) > 3):
                continue
            
        print(res)
        if all(res) or not all(res):
            safe_count += 1
    rep += 1

print(safe_count)