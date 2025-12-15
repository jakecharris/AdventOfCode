'''
Day 4: Printing Department (https://adventofcode.com/2025/day/4)

You are looking at a large stack of rolls of paper, notated by . for empty and
@ for paper. You need to remove certain rolls of paper in order to lower the 
wall of paper.

Problem 4.1: How many rolls of paper can be removed assuming that only those
rolls which are surrounded by fewer than 4 adjacent rolls in eight directions
are accessible?
'''

# Problem 4.1 - matrix grid problem

# Open file as array with padding width of 1
array = [line for line in open('input4.txt').read().strip().splitlines()]
pad = '$' * (len(array[0]))
array.insert(0, pad)  # top
array.append(pad)  # bottom
for i in range(len(array)):  # left/right 
    array[i] = '$' + array[i] + '$'

# Go through array, search for '@' symbol, and count surrounding '@' 
# symbols to check if fewer than 4
total_accessible = 0
for y in range(len(array)):  # 
    for x in range(len(array[y])):
        s = []  # symbols
        if array[x][y] == '@':
            s.append(array[x-1][y+1])
            s.append(array[x][y+1])
            s.append(array[x+1][y+1])
            s.append(array[x-1][y])
            s.append(array[x+1][y])
            s.append(array[x-1][y-1])
            s.append(array[x][y-1])
            s.append(array[x+1][y-1])
            total_accessible += 1 if s.count('@') < 4 else 0
        else:
            pass
print(f'Answer part 1: {total_accessible}')  # Answer: 1480

