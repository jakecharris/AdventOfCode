'''
Day 5: Cafeteria (https://adventofcode.com/2025/day/5)

The cafeteria has an ingredients database with two sets of data. The first part
is a range of fresh ingredient ID ranges (both ends inclusive, can overlap), and 
the second is a list of currently available ingredient IDs. If an available 
ingredient falls in a fresh ID range, then it is considered fresh. Otherwise, 
it is considered spoiled.

Problem 5.1: From the given fresh ID ranges and available ingredient IDs, how 
many ingredients in the database are fresh? 
'''

# Problem 5.1: number of fresh ingredients

# load in file and split into 2 lists: ingredient ranges and inventory IDs
file = [line for line in open('input5.txt').read().strip().splitlines()]
ing_ranges = []
inv_ids = []
for line in file:
    if '-' in line:
        nums = list(map(int, line.split('-')))
        ing_ranges.append(nums)
    elif line != '':
        inv_ids.append(int(line))
    else:
        pass

num_ranges = [range(x, y+1) for x, y in ing_ranges]
fresh_inv = set([i for i in inv_ids for r in num_ranges if i in r])
print(f'Answer part 1: {len(fresh_inv)}')  # Answer: 720


'''
Problem 5.2: Now, just consider the fresh ingredient ID ranges. Considering that
many of the ranges overlap each other, how many unique fresh ingredient IDs are there?
'''

# Problem 5.2: number of fresh ingredient IDs 
# combine overlapping inventory ranges 
ing_ranges.sort(key=lambda x: x[0])

i = 0
while i < len(ing_ranges) - 1:
    if ing_ranges[i][1] >= ing_ranges[i+1][0]:
        ing_ranges[i][1] = max(ing_ranges[i][1], ing_ranges[i+1][1])
        ing_ranges.pop(i+1)
    else:
        i += 1

fresh_ranges = [(y+1) - x for x, y in ing_ranges]

print(f'Answer part 2: {sum(fresh_ranges)}')  # Answer: 357608232770687