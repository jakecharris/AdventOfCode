'''
Day 2: Gift Shop (https://adventofcode.com/2025/day/2)

There are a series of product ID ranges. Invalid IDs are those with made of
just two sequences of repeating digits (e.g. 55 (two 5s), 1010 (two 10s), 123123
(two 123s)). None of the numbers have leading zeroes.

Problem 2.1: From an input of given IDs, find all the invalid IDs made of digits
which occur twice and sum all them. 
'''

# Open ID ranges file
with open('input2.txt') as f:
    id_ranges = f.read().strip()  # remove '\n' at end of file
    id_ranges = id_ranges.split(',')
    id_ranges = [id_nums.split('-') for id_nums in id_ranges]

# Part 1: Search for invalid IDs of twice occuring digit patterns
def part1():
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
    print(f'Answer part 1: {sum_invalid_ids}')  

# part1()  # Answer: 15873079081

'''
Problem 2.2: Modify your search for invalid IDs by looking for IDs with digit 
patterns which occur *at least* twice (e.g. 99 (two 9s), 111 (three 1s), 
or 565656 (three 56s)).
'''

# Part 2: Search for IDs with at least twice occuring digit patterns
def part2():
    invalid_ids = []
    
    for id_ran in id_ranges:
        id1, id2 = int(id_ran[0]), int(id_ran[1])
        print(f'Running {id1, id2}')
        id_lst = [str(i) for i in range(id1, id2+1)]
        
        # loop through gradually increasing digit motif window, starting with 
        # 1 digit going up to len(id)//2
        for id_num in id_lst:
            n = 1
            while n <= len(id_num)//2:
                split_id = [id_num[j:j+n] for j in range(0, len(id_num), n)]
                if len(set(split_id)) == 1: 
                    invalid_ids.append(int(id_num))
                    n = 1
                    print(f'Added {id_num} to the list')
                    break
                elif set(split_id) != 1:
                    n += 1

    sum_invalid_ids = sum(invalid_ids)
    print(f'Answer part 2: {sum_invalid_ids}')         

part2()  # Answer: 22617871034