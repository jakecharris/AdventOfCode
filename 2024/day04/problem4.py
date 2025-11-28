'''Day 4: Ceres Search (https://adventofcode.com/2024/day/4)

You are given a wordsearch puzzle with the only word to find being "XMAS". 
However, it is written in multiple directions, including horizontally, vertically,
diagonally, and backwards in all of the former directions. Some instances even 
overlap each other. In the given puzzle, how many instances of "XMAS" are there?
'''

import numpy as np

# Open text as numpy array
arr = []
with open('input4.txt') as file:
    # arr += [line.strip() for line in file]
    for line in file:
        line = line.strip()
        arr.append(list(line))
    arr = np.asarray(arr, dtype=str)
print(arr)