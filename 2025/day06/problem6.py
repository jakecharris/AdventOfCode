'''
Day 6: Trash Compactor (https://adventofcode.com/2025/day/6)

You are given an array of numbers with a bottom row of math operation symbols
for either adding (+) or multiplying (*) all of the numbers for each vertical 
column of numbers.

Problem 6.1: Given the array of numbers with the math operator symbols, what is
the grand total of all of the calculated columns?
'''

# Problem 6.1: total of computed columns
import math

array = [line.split('\n\n') for line in open('input6.txt').read().strip().splitlines()]
num_array = []
for num_line in array[:-1]:
    nums = num_line[0].split()
    num_array.append(list(map(int, nums)))
op_array = [op for x in array[-1] for op in x.split()]

answer_part1 = 0
i = 0
while i < len(op_array):
    col = []
    for j in range(len(num_array)):
        col_num = num_array[j][i]
        col.append(col_num)
    if op_array[i] == '+':
        answer_part1 += sum(col)
    elif op_array[i] == '*':
        answer_part1 += math.prod(col)
    i += 1
print(answer_part1)  # Answer: 4878670269096


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
# need a way to determine if each num is right or left aligned