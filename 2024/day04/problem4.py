'''Day 4: Ceres Search (https://adventofcode.com/2024/day/4)

You are given a wordsearch puzzle with the only word to find being "XMAS". 
However, it is written in multiple directions, including horizontally, vertically,
diagonally, and backwards in all of the former directions. Some instances even 
overlap each other. In the given puzzle, how many instances of "XMAS" are there?

Solution adapted from 
https://github.com/UserGeorge24/aoc_24_python/blob/main/day_04_task_01.py
'''

import re

# Open text array as list with each row as an index
arr = [line.strip() for line in open('input4.txt').readlines()]

xmas_sum = 0 # overall "XMAS" instances 
pos_idx = 0 # position index

# Function to count number of 'XMAS' regex in each direction of selected txt
def count_xmas(txt):
    global xmas_sum # allows for changing xmas_sum outside function
    # regex to count number of forward + backward ([::-1]) txt instances
    xmas_sum += len(re.findall('XMAS', txt)) + len(re.findall('XMAS', txt[::-1]))

# Horizontal instances
for i in arr:
    count_xmas(arr)
    
# Vertical instances
# make strings of each array column
while True:
    try:
        col_txt = ''.join([col[pos_idx] for col in arr])
    except:
        break
    # check for 'XMAS' in column text, move to new column
    count_xmas(col_txt)
    pos_idx += 1

