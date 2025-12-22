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
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|

'''
