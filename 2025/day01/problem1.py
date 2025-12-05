'''
Day 1: Secret Entrance (https://adventofcode.com/2025/day/1)

You need to get into the base, but there is a set of instrucitons to open a safe 
with numbers 0-99. The instructions tell you which direction to turn (Right or Left) 
and by how many units. The initial start is at 50.

Problem 1.1: How many times while turning based on the instructions do you land 
exactly on 0?

Problem 1.2: While turning the safe dial, how many times to you pass by 00?
'''

# Open safe turn directions from input.txt
turns = [line.strip() for line in open('input1.txt').readlines()]
turns = [[t[:1], int(t[1:])] for t in turns]  # [['R', n], ['L', n], ...]
print(f'Num. of turns: {len(turns)}')  # 4671 turns

pos = 50  # initial position
zero_count = 0  # times landed on 00
zero_pass = 0  # times pass by 00

for turn in turns:
    prev_pos = pos  # previous position to start from
    
    # Problem 1.1: number of times landing on 00
    if turn[0] == 'R':
        pos += turn[1]
    else:
        pos -= turn[1]
    # landed on 00 if pos == 100
    zero_count += 1 if pos % 100 == 0 else 0

    # Problem 1.2: number of times passed by 00
    # check difference in hundreds positions between prev pos and current pos
    prev_hundreds = prev_pos // 100
    curr_hundreds = pos // 100
    hunds_diff = abs(curr_hundreds - prev_hundreds)
    
    # if moving R and hunds_diff > 0, then passed 00
    zero_pass += hunds_diff
    
    # if moving L...
    if turn[0] == 'L':
        # land on 00, add to answer
        if pos % 100 == 0:
            zero_pass += 1
        # correct for overcounting if prev_pos = 100, meaning last turn already 
        # crossed from one hundreds digits to another (e.g. 1 to 0)
        if prev_pos % 100 == 0:
            zero_pass -= 1
        

print(f'Problem 1.1: Zero count: {zero_count}')  # Answer: 1177
print(f'Problem 1.2: Zero passes: {zero_pass}')  # Answer: 6768