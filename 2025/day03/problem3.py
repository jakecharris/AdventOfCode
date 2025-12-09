'''
Day 3: Lobby (https://adventofcode.com/2025/day/3)

You see a collection of banks of batteries. Each bank contains individual 
joltage ratings between 1-9 for individual batteries. For example, a bank of 
batteries labeled "123" has batteries with joltage ratings 1, 2, and 3. Turning
on certain batteries can allow them to combine their joltages into a greater value.

Problem 3.1: For each battery bank, turn on exactly two batteries which have the
highest values to make a single highest combined value (e.g. 2 and 3 from 123 
to make 23). *The two digits are read in left-to-right order!! Then, add up all 
of the resulting values from each bank to get a total maximum output joltage.
'''

# Open battery banks from input3.txt
joltages = [line for line in open('input3.txt').read().strip().splitlines()]
# print(f'Num. of joltages: {len(joltages)}')  # 200 joltages

# Part 1: Combine largest two batteries from each bank
# Solution based on https://github.com/mgtezak/Advent_of_Code/blob/master/2025/03/p1.py
def part1():
    total_output = 0
    for jolt in joltages:
        n1 = max(jolt[:-1])
        n2 = max(jolt[jolt.find(n1)+1:])
        total_output += int(n1 + n2)
    print(f'Answer part 1: {total_output}')

part1()  # Answer: 17524

'''
Problem 3.2: Now, you want to increase the total output of the battery banks by
turning on 12 of the highest joltage batteries from left to right. What is the
new total joltage output?
'''

# every len(joltage) = 100, so need to drop 88 digits




banks = [[int(n) for n in line] for line in open('input3.txt').read().strip().splitlines()]

PICK = 12
total = 0

for bank in banks:
    n = len(bank)
    to_remove = n - PICK
    stack = []
    for battery in bank:
        while stack and to_remove > 0 and stack[-1] < battery:
            stack.pop()
            to_remove -= 1
        stack.append(battery)
    if to_remove > 0:
        stack = stack[:-to_remove]
    joltages = stack[:PICK]
    total += int("".join(map(str, joltages)))

print(total)

ex = [4]
print(bool(ex))