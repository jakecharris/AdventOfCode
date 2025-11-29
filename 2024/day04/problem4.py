'''Day 4: Ceres Search (https://adventofcode.com/2024/day/4)

Problem 4.1: You are given a wordsearch puzzle with the only word to find being "XMAS". 
However, it is written in multiple directions, including horizontally, vertically,
diagonally, and backwards in all of the former directions. Some instances even 
overlap each other. In the given puzzle, how many instances of "XMAS" are there?

Solution adapted from 
https://github.com/UserGeorge24/aoc_24_python/blob/main/day_04_task_01.py
'''

import re

# Open text array as list with each row as an index
array = [line.strip() for line in open('input4.txt').readlines()]

xmas_sum = 0 # overall "XMAS" instances 

# Function to count number of 'XMAS' regex in each direction of selected txt
def count_xmas(txt):
    global xmas_sum # allows for changing xmas_sum outside function
    # regex to count number of forward + backward ([::-1]) txt instances
    xmas_sum += len(re.findall('XMAS', txt)) + len(re.findall('XMAS', txt[::-1]))

# Horizontal instances
for line in array:
    count_xmas(line)
    
# Vertical instances
# make strings of each array column
def vertical_count(txt):
    pos_idx = 0 # position index
    while True:
        try:
            col_txt = ''.join([col[pos_idx] for col in txt])
        except:
            break
        # check for 'XMAS' in column text, move to new column
        count_xmas(col_txt)
        pos_idx += 1
vertical_count(array)

# Diagonal instances - shift each row by one, then do vertical 
def diagonal_count(txt, direction):
    row_txt = txt[:len('XMAS')]
    shifted_array = []
    # while True:
    if direction == 'R': # right diagonal
        for i, row_txt in enumerate(txt):
            row_shift = row_txt[i:]
            shifted_array.append(row_shift)
            vertical_count(shifted_array)
            shifted_array = []
    if direction == 'L': # left diagonal
        for i, row_txt in enumerate(txt):
            row_shift = row_txt[3 - i:]
            shifted_array.append(row_shift)
            vertical_count(shifted_array)
            shifted_array = []
        
diagonal_count(array, 'R')
diagonal_count(array, 'L')

print(xmas_sum)
# answer of 831 was too low
# While loop in diagonal() led to infinite loop