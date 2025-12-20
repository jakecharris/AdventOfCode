'''
Day 6: Trash Compactor (https://adventofcode.com/2025/day/6)

You are given an array of numbers with a bottom row of math operation symbols
for either adding (+) or multiplying (*) all of the numbers for each vertical 
column of numbers.

Problem 6.1: Given the array of numbers with the math operator symbols, what is
the grand total of all of the calculated columns?
'''

# Problem 6.1: total of computed columns
from math import prod
from itertools import groupby, chain

array: list[list[str]] = [line.split('\n\n') for line in open('input6.txt').read().strip().splitlines()]
num_array: list[list[str]] = [line for line in array[:-1]]
op_array: list[str] = [op for x in array[-1] for op in x.split()]

def part1():
    num_ints: list[list[int]] = []
    for num_line in num_array:
        nums = num_line[0].split()
        num_ints.append(list(map(int, nums)))
    
    answer_part1 = 0
    i = 0
    while i < len(op_array):
        col = []
        for j in range(len(num_ints)):
            col_num = num_ints[j][i]
            col.append(col_num)
        if op_array[i] == '+':
            answer_part1 += sum(col)
        elif op_array[i] == '*':
            answer_part1 += prod(col)
        i += 1
    print(answer_part1)  # Answer: 4878670269096

# part1()

'''
Problem 6.2: The provided columns of numbers are actually supposed to be read in a
right-to-left manner with each digit in its own column and then read top-down.
With this in mind and using the same operator rules as before, what is the new
total of calculated digit columns?
'''

# Problem 6.2: R-to-L arranged column digits
'''
    1  2  3                             6  4
       4  5  -> 356 * 24 * 1 = 8544     2  3    -> 4 + 431 + 623 = 1058
          6                             3  1  4
    *                                   +
'''
# lok for columns of all whitespace to use as reference for where to start/stop 
# read the entire length of num_array
# should have 1000 groups of 3 nums each for 1000 operators
def part2():
    # unpack list of 4 sublists into list of 4 num strings
    num_txt = list(chain.from_iterable(num_array))
    
    # loop through num_array, combine digits from R-to-L, top-to-bottom
    columns = []
    num = ''
    for col in range(len(num_txt[0])):
        for row in range(len(num_txt)):
            num = num + num_txt[row][col]
        columns.append(num)
        num = ''
    
    # group together numbers with empty whitespace columns as key
    is_space: list[bool] = []  # bool list if list is only spaces
    col_groups: list[list[str]] = []  # strings of nums, spaces
    for key, group in groupby(columns, lambda x: x.isspace()):
        is_space.append(key)
        col_groups.append(list(group)) 
    num_groups = [list(map(int, nums)) for space, nums in zip(is_space, col_groups) if not space]
    
    # run math for each group based on operator 
    answer_part2 = 0
    for i in range(len(op_array)):
        if op_array[i] == '+':
            answer_part2 += sum(num_groups[i])
        elif op_array[i] == '*':
            answer_part2 += prod(num_groups[i])
    print(answer_part2)
     
part2()
