'''Day 2: Red-Nosed Reports (https://adventofcode.com/2024/day/2)

Problem 2.1: You are given a series of values which represents readouts from a 
power plant. Each row is a report while each column is a power level. In order 
to be counted as safe, a report must have both:
    - all increasing or all decreasing levels
    - all adjacent levels change between 1 and 3.
How many safe power reports are there in the provided data?
(Results taken from r/AdventOfCode Reddit solution thread)
'''

import csv

# Load individual report rows from input2.txt into list of lists
reports = []
with open('input2.txt', newline='') as file:
    report_reader = csv.reader(file, delimiter=' ')
    for row in report_reader:
        reports.append([int(i) for i in row])

safe_count_1 = 0

def safety_check(arr):
    # Default True; change if report values prove otherwise
    increasing = True
    decreasing = True
    # Check each val in array for increasing/decreasing differences
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            increasing = False
        if arr[i] < arr[i+1]:
            decreasing = False
        # Check for abs(difference) between 1 and 3
        if abs(arr[i] - arr[i+1]) > 3 or abs(arr[i] - arr[i+1]) < 1:
            return False
    
    return increasing or decreasing

# Check each individual report in full reports lists; count safe reports
for rep in reports:
    if safety_check(rep):
        safe_count_1 += 1
print(safe_count_1) # Solution: 332

'''Problem 2.2: Some of the reports that were marked as "unsafe" can actually be
considered as "safe" if you were to remove a single value from them while still
following the previously stated requirements from earlier. With this in mind,
how many reports are can now be considered "safe?"'''

safe_count_2 = 0

# Go through reports again
for arr in reports:
    for i in range(len(arr)):
        # Check each report by removing one val to see if safety_check() passes
        if safety_check(arr[:i] + arr[i+1:]):
            # print(arr[:i] + arr[i+1:])
            # print(safety_check(arr[:i] + arr[i+1:]))
            safe_count_2 += 1
            break
print(safe_count_2)