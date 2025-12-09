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
# Part 2: Combine largest 12 batteries from banks
# Solution from @No_Mobile_8915 on Reddit 
# (https://old.reddit.com/r/adventofcode/comments/1pcvaj4/2025_day_3_solutions/)
def part2():
    banks = [[int(n) for n in line] for line in open('input3.txt').read().strip().splitlines()]  # load each battery bank as individual ints
    total_output = 0
    for bank in banks:
        to_remove = len(bank) - 12  # this example: remove 3 digits from each to reach 12 digits
        stack = []  # First In Last Out 
        for battery in bank:
            # while digits can be removed and final digit is less than battery...
            while stack and to_remove > 0 and stack[-1] < battery:
                stack.pop()  # remove it from the stack
                to_remove -= 1  # and lower needed digits to be removed
            stack.append(battery)  # add digit to list; also initial condition as blank list is False
        if to_remove > 0:  # if reach end and still have to_remove, exclude final n digits
            stack = stack[:-to_remove]
        jolt_digits = stack[:12]  # pick from only front 12 digits
        output = int(''.join(map(str, jolt_digits)))
        total_output += output
    print(f'Answer part 2: {total_output}')
    
part2()  # Answer: 173848577117276
    