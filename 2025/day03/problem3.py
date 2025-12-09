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
joltages = [line.strip() for line in open('input3.txt').readlines()]
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
def part2():
    total_output = 0
    for jolt in joltages:
        bat_bank = ''
        pos = 0
        for i in range(12, 0, -1):
            digit = max(jolt[pos:-i])
            pos = jolt.find(digit, pos) + 1
            # print(f'i {i}, Digit {digit}, Pos {pos}')
            bat_bank += digit
        
        total_output += int(bat_bank)
    
    print(f'Answer part 2: {total_output}')

# part2() # Answer: 

print([i for i in range(11, 0, -1)])
print([i for i in reversed(range(12))])

n = '123'   
print(n[2:-1])