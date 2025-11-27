'''Day 3: Mull It Over (https://adventofcode.com/2024/day/3)

Problem 3.1: A memory leak has caused a string of text which contains instructions 
for multiplying numbers to become jumbled. Find the uncorrupted multiplication
instructions in the text with the structure "mul(X,Y)" - MUST only use round 
brackets () and no spaces - multiply each pair, and add the total products to
get the answer.
'''

import re

# Open file, search for instances of 'mul(X,Y)' regex pattern
txt = ''
with open('input3.txt') as file:
    for line in file:
        txt += line.strip()
mul_lst = re.findall(r'(mul\(\d+,\d+\))', txt)

# Replace unecessary 'mul()' text from mul_lst, multiply numbers, add products
total_sum = 0
for entry in mul_lst:
    num_txt = re.sub(r'mul\(', '', entry)
    num_txt = re.sub(r'\)', '', num_txt)
    num_int = [int(num) for num in num_txt.split(',')]
    product = num_int[0] * num_int[1]
    total_sum += product
print(total_sum)

