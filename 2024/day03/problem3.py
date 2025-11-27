'''Day 3: Mull It Over (https://adventofcode.com/2024/day/3)

A memory leak has caused a string of text which contains instructions for 
multiplying numbers to become jumbled. Find the uncorrupted multiplication
instructions in the text with the structure "mul(X,Y)" - MUST only use round 
brackets () and no spaces - multiply each pair, and add the total products to
get the answer.
'''

import re

txt = ''
with open('input3.txt') as file:
    for line in file:
        txt += line.strip()

# Search for instances of 'mul(X,Y)' regex pattern
mul_lst = re.findall(r'(mul\(\d+,\d+\))', txt)
print(mul_lst)