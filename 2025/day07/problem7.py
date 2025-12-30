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
read_array = [line for line in open('input7.txt').read().strip().splitlines()] 
ex = 'abcdefg'
ex_lst = list(ex)
ex_lst[3] = '#'
ex = ''.join(ex_lst)
print(ex)

# find indexes of chars using enumerate in a dict

total_splits = 0
array = read_array
# for i in range(len(array)-1):
for i in range(0, 5):
    # dicts of indexes of symbols in reference/next rows
    ref_row = array[i]
    # print(ref_row)
    ref_idx = {ele: [] for ele in ref_row}
    for idx, ele in enumerate(ref_row):
        ref_idx[ele].append(idx)
    next_row = array[i+1]
    # print(next_row)
    next_idx = {ele: [] for ele in next_row}
    for idx, ele in enumerate(next_row):
        next_idx[ele].append(idx)
    
    # first beam symbol below 'S'
    if ('S' in ref_row):
        next_lst = list(next_row)
        for j in ref_idx['S']:
            next_lst[j] = '|' 
        next_row = ''.join(next_lst)
    # extend existing beams into next_row
    elif ('^' in ref_row) and ('|' in ref_row):
        next_lst = list(next_row)
        for j in ref_idx['|']:
            next_lst[j] = '|'
        next_row = ''.join(next_lst)
    # split beams (or continue if not split)
    elif ('|' in ref_row) and ('^' in next_row):
        # look for equal idx in ref beams and next splits
        beam_split_idx = list(set(ref_idx['|']) & set(next_idx['^']))
        next_lst = list(next_row)
        for j in beam_split_idx:
            if j in ref_idx['|']:
                next_lst[j-1] = '|'
                next_lst[j+1] = '|'
                total_splits += 1
            # if ref beam but no next split, just extend beams
            else:
                next_lst[j] = '|'
        next_row = ''.join(next_lst)

print(total_splits)

'''
row 0: S row, no changes
row 1: change below S to beam
row 2: first split, change .s on either side to beams
row 3: change .s below beams to extend beams
row 4: second split, change .s on either side to beams
etc

'''

