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
def total_product_sum(lst):
    total_sum = 0
    for entry in lst:
        num_txt = re.sub(r'mul\(', '', entry)
        num_txt = re.sub(r'\)', '', num_txt)
        num_int = [int(num) for num in num_txt.split(',')]
        product = num_int[0] * num_int[1]
        total_sum += product
    print(total_sum)

total_product_sum(mul_lst)

'''Problem 3.2: There are additional do() and don't() instructions throughout the
text which enable/disable following mul() functions, respectively. Think of it
like an on/off switch for multiplications. What is the new total sum of products 
if you take only those mul(X,Y) which are after do() statements?
'''

# Run same idea from above, but look for 'do()' and 'don't()' in txt 
sum_product = 0
do_func = True
for x in re.finditer(r'do\(\)|don\'t\(\)|(mul\(\d+,\d+\))', txt):
    print("x[0]: ", x[0])
    print("x[1]: ", x[1])
    match x[0]: # x[0] will be for either "do()" or "dont()" 
        case 'do()':
            do_func = True
        case 'don\'t()':
            do_func = False
        case _: # x[1] will be for either None (if do/dont) or a mul(X,Y)
            if do_func:
                num_txt = re.sub(r'mul\(', '', x[1])
                num_txt = re.sub(r'\)', '', num_txt)
                num_int = [int(num) for num in num_txt.split(',')]
                product = num_int[0] * num_int[1]
                sum_product += product
print(sum_product)