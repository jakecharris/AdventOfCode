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
id_ranges = []
inv_ids = []
for i in range(len(file)):
    if '-' in file[i]:
        nums = list(map(int, file[i].split('-')))
        nums_range = [i for i in range(nums[0], nums[1] + 1)]
        for n in nums_range:
            id_ranges.append(n)
    elif file[i] != '':
        inv_ids.append(int(file[i]))
    else:
        pass
print(id_ranges)


def num_fresh():
    pass

# ex = []
# num = '12-15'
# nums = list(map(int, num.split('-')))
# print(nums)
# nums_range = [i for i in range(nums[0], nums[1]+1)]
# print(nums_range)
# print(ex)
# print(nums)
# print(int(n) for n in range(nums[0], nums[1] + 1))