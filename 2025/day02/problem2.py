'''
Day 2: Gift Shop (https://adventofcode.com/2025/day/2)

There are a series of product ID ranges. Invalid IDs are those with made of
just two sequences of repeating digits (e.g. 55 (two 5s), 1010 (two 10s), 123123
(two 123s)). None of the numbers have leading zeroes.

Problem 2.1: From an input of given IDs, find all the invalid IDs and sum all
them up. 
'''

# Open ID ranges file
with open('input2.txt') as f:
    id_ranges = f.read().strip()  # remove '\n' at end of file
    id_ranges = id_ranges.split(',')
    id_ranges = [id_nums.split('-') for id_nums in id_ranges]

# Search for invalid IDs 
invalid_ids = []
for id_ran in id_ranges:
    id1, id2 = int(id_ran[0]), int(id_ran[1])
    # make list of IDs that are even in length of digits
    even_ids = [str(i) for i in range(id1, id2+1) if len(str(i)) % 2 == 0]
    # append those IDs with front half digits that are same as back half digits
    for i in even_ids:
        half1, half2 = i[:len(i)//2], i[len(i)//2:]
        invalid_ids.append(int(i) if half1 == half2 else 0)

sum_invalid_ids = sum(invalid_ids)
print(f'Sum of invalid IDs: {sum_invalid_ids}')  # Answer: 15873079081