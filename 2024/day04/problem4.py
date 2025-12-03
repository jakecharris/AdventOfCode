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
            col_txt = ''.join([row[pos_idx] for row in txt])
        except:
            break
        # check for 'XMAS' in column text, move to new column
        count_xmas(col_txt)
        pos_idx += 1
vertical_count(array)

# Diagonal instances - shift each row by one, then do vertical 
# def diagonal_count(txt, direction):
#     row_txt = txt[:len('XMAS')]
#     shifted_array = []
#     # while True:
#     if direction == 'R': # right diagonal
#         for i, row_txt in enumerate(txt):
#             row_shift = row_txt[i:]
#             shifted_array.append(row_shift)
#             vertical_count(shifted_array)
#             shifted_array = []
#     if direction == 'L': # left diagonal
#         for i, row_txt in enumerate(txt):
#             row_shift = row_txt[3 - i:]
#             shifted_array.append(row_shift)
#             vertical_count(shifted_array)
#             shifted_array = []
        
# diagonal_count(array, 'R')
# diagonal_count(array, 'L')

# print(xmas_sum)
# answer of 831 was too low
# While loop in diagonal() led to infinite loop

# Diagonal shift - move pos_idx window of text of interes for each row by 1 
# going down depending if roated by right (top row doesn't move) or left (bottom
# row doesn't move)

# def diagonal_count(txt, direction):
#     crop_array = []
#     row_idx = 0
#     for idx in range(len(txt)):
#         row_idx = idx
#         try:
#             # select 4 rows from overall array
#             crop_array = txt[row_idx : row_idx+len('XMAS')]
#             shift_array = []
#             if direction == 'R':
#                 shift_array.append(crop_array[row_idx][row_idx : -len('XMAS')+1 + row_idx])
#                 vertical_count(shift_array)
#             if direction == 'L':
#                 shift_array.append(crop_array[row_idx][len('XMAS')-1 - row_idx : -len('XMAS')+1 + row_idx])
#                 vertical_count(shift_array)
#         except:
#             break    
#         row_idx += 1

# print(xmas_sum)

# scratch code - find 'XMAS'
ex_arr = ['XabSopfj', 'sMAffnvns', 'sMAdfofnsbne', 'XieSmvjbeufg', 'skdjfbso', 'fifififi', 'sdoivbwod']
# for i in range(len(ex_arr)):
#     print(ex_arr[i])
# print(' ')
def diag_ex(txt):
    pos_idx = 0
    while pos_idx <= len(txt)-len('XMAS'):
        try:
            crop_array = txt[pos_idx : pos_idx+len('XMAS')]
            print('crop:', crop_array)
            shift_rows_dwn = ''.join([crop_array[i][i] for i in range(len('XMAS'))])
            shift_rows_up = ''.join([crop_array[i][i] for i in range(len('XMAS')-1, -1, -1)])
            print('rows_dwn:', shift_rows_dwn)
            print('rows_up:', shift_rows_up)
            # shift_cols = ''.join([row[pos_idx] for row in crop_array])
            # print('shift:', shift_cols)
        except:
            break
        count_xmas(shift_rows_dwn)
        count_xmas(shift_rows_up)
        pos_idx += 1
diag_ex(ex_arr)
    
print(xmas_sum)
    
    # while row_idx < len(ex_arr):
    #     for i in range(len(ex_arr)):
    #         row_idx = i
    #         try:
    #             row = ex_arr[row_idx][row_idx : row_idx+len('XMAS')] # need to make loop stop at 4 indx, not continue
    #             # print(row)
    #             select_rows.append(row)
    #         except:
    #             break
    #         row_idx += 1
    # return(select_rows)

    # for i in range(5):
    #     print(word[i:len(word)+i+1])
word = 'abcd'
print(word[:20])


# solution from https://bversion.com/WordPress/2024/12/06/aoc-2024/#day-4
# Part 1
f = open("Day 4 - input.txt", "r")
a = []
w = ['']*8
total = 0

for i in f:
    a.append(i.strip())

s = 'Z' * (len(a[0])+6)
for i in range(len(a)):
    a[i] = 'ZZZ' + a[i] + 'ZZZ'
    
for i in range(3):
    a.insert(0, s)
    a.append(s)

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 'X':
            w[0] = a[y][x:x+4]
            w[1] = a[y][x]+a[y+1][x+1]+a[y+2][x+2]+a[y+3][x+3]
            w[2] = a[y][x]+a[y+1][x]+a[y+2][x]+a[y+3][x]
            w[3] = a[y][x]+a[y+1][x-1]+a[y+2][x-2]+a[y+3][x-3]
            w[4] = a[y][x]+a[y][x-1]+a[y][x-2]+a[y][x-3]
            w[5] = a[y][x]+a[y-1][x-1]+a[y-2][x-2]+a[y-3][x-3]
            w[6] = a[y][x]+a[y-1][x]+a[y-2][x]+a[y-3][x]
            w[7] = a[y][x]+a[y-1][x+1]+a[y-2][x+2]+a[y-3][x+3]
            total += w.count('XMAS')    
            
print(total)

# part 2
f = open("Day 4 - input.txt", "r")
a = []
w = ['']*2
total = 0

for i in f:
    a.append(i.strip())

s = 'Z' * (len(a[0])+2)
for i in range(len(a)):
    a[i] = 'Z' + a[i] + 'Z'
    
for i in range(3):
    a.insert(0, s)
    a.append(s)

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == 'A':
            w[0] = a[y-1][x-1]+a[y][x]+a[y+1][x+1]
            w[1] = a[y+1][x-1]+a[y][x]+a[y-1][x+1]
            if w.count('MAS')+w.count('SAM') == 2:
                total += 1
                       
print(total)