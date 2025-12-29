'''
Day 7: Laboratories (https://adventofcode.com/2025/day/7)

You see a screen with a tachyon diagram showing splits whenever a tachyon particle 
encounters a splitter. As a beam moves downward, starting at S, it then splits
at each '^' marking to the left and right before continuing downward.

Problem: 7.1: Based on this beam splitting pattern, how many times will a beam
be split based on the provided diagram?
'''

# Problem 7.1: number of tachyon beam splits
'''
.......S.......
.......|.......    |  -> direction of beam
......|^|......   |^| -> splits immediately at left and right of splitter
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....    total number of splits = 21
....|.|.|.|....     
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.    pattern: only count when a '|' is above a '^'???
|^|^|^|^|^|||^|             only count when a 
|.|.|.|.|.|||.|

'''
import re

# load in unmod file
# for row 0 has S
# for odd rows, change periods to | to reflect beam pattern
    # if beam right above ^ , then change periods next to it to beams, count split
    # change periods in rows below to | 

# open lines of array file 
array = [line for line in open('input7.txt').read().strip().splitlines()] 
even_rows = [array[i] for i in range(len(array)) if i % 2 == 0]
odd_rows = [array[i] for i in range(len(array)) if i % 2 != 0]

print(all('^' in even_rows[i] for i in range(2, len(even_rows))))  # True
print(any('^' in odd_rows[i] for i in range(len(odd_rows))))  # False

print(even_rows[0].index('.'))  # S in row 0 at index 70

# find indexes of chars using enumerate in a dict

total_splits = 0
i = 1
for i in range(len(array)):
    # dict of indexes of symbols in row
    char_idx = {ele: [] for ele in array[i]}
    for idx, ele in enumerate(array[i]):
        char_idx[ele].append(idx)
    
    for row in array:
        # first beam symbol below 'S'
        if ('S' in row[i]):
            row_lst = list(array[i+1])
            for j in char_idx['S']:
                row_lst[j] = '|' 
            ''.join(row_lst)
        # split beams on either side of splitter
        if ('^' in row[i]) and ('|' in row[i-1]):
            
            beam_lst = list(array[i-1])
            split_lst = list(array[i])
            for j in char_idx['|']:
                split_lst[j-1] = '|' 
                split_lst[j+1] = '|'
            ''.join(row_lst)
            
            
        else:
            pass
    

# change '.' in row 1, index 70 below S to '|'  
row1_lst = list(array[1])
row1_lst[70] = '|'
''.join(row1_lst)

