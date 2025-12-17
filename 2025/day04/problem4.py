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
def total_accessible_part1() -> str:
    total_part1 = 0
    for y in range(len(array)):  
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
                total_part1 += 1 if s.count('@') < 4 else 0
            else:
                continue
    return(f'Answer part 1: {total_part1}')  # Answer: 1480
# print(total_accessible_part1())


'''
Problem 4.2: Now consider that as rolls of paper are removed, there will be new
rolls of paper made accessible by the absence of the removed paper. With this in
mind, how many rolls of paper will be removed from the stack before no more rolls
can be removed?
(https://adventofcode.com/2025/day/4#part2)
'''

# Problem 4.2 - removing and replacing paper rolls
# same idea as before, but take note of which rolls are taken and replace character
# do this for each round until no more rolls are accessible, return total


# Same array search as before, but take note of accessible papers until 
# no more papers are accessible
def total_accessible_part2() -> str:
    total_part2 = 0
    changed = True
    while changed:
        to_replace = []
        for y in range(len(array)):
            for x in range(len(array[y])):
                # make list of symbols & x/y coordinates
                s = []
                if array[x][y] == '@':
                    s.append(array[x-1][y+1])
                    s.append(array[x][y+1])
                    s.append(array[x+1][y+1])
                    s.append(array[x-1][y])
                    s.append(array[x+1][y])
                    s.append(array[x-1][y-1])
                    s.append(array[x][y-1])
                    s.append(array[x+1][y-1])
                    if s.count('@') < 4:
                        to_replace.append([x, y]) # PROBLEM: appending too many times
                        total_part2 += 1
                else:
                    continue
        
        # replace '@' symbols with "." using to_replace coordinates
        if len(to_replace) > 0:
            x = [i[0] for i in to_replace]
            y = [i[1] for i in to_replace]
            for (i, j) in zip(x, y):
                row = array[i]
                row = row[:j] + '.' + row[j+1:]
                array[i] = row
        # end While loop if array didn't change
        else:
            changed = False
            
    return(f'Answer part 2: {total_part2}')  # Answer: 

print(total_accessible_part2())

# print(array[137][1])  # array size: 139 x 139


# ex = ['bacd', 'efga', 'fgav', 'caad']
# r = [[0,1], [1,3], [2,2], [3,1], [3,2]]
# a = [i[0] for i in r]
# b = [i[1] for i in r]
# new_words = []
# for (i,j) in zip(a,b):
#     word = ex[i]
#     word = word[:j] + '@' + word[j+1:]  # SOLUTION?????
#     ex[i] = word
# print(ex)
# # for j in r:
# #     a, b = j[0], j[1]
# #     ex[a][b] = '@'
#     # ex = ex[a][b].replace('a', '@')
# print(ex)