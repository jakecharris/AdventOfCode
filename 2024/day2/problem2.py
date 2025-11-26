'''Day 2: Red-Nosed Reports (https://adventofcode.com/2024/day/2)

You are given a series of values which represents readouts from a power plant. 
Each row is a report while each column is a power level. In order to be counted
as safe, a report must have both
    - all increasing or all decreasing levels
    - all adjacent levels change between 1 and 3.
How many safe power reports are there in the provided data?
'''

import csv
import re

# Load report rows from input2.txt into one list
reports = []
with open ('input2.txt', newline='') as file:
    report_reader = csv.reader(file, delimiter=' ')
    for row in report_reader:
        reports.append(row)
print(reports[:5])