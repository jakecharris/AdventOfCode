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
print(answer_part1)