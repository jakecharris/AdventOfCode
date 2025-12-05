'''
Day 1: Secret Entrance (https://adventofcode.com/2025/day/1)

Problem 1.1: You need to get into the base, but there is a set of instrucitons
to open a safe with numbers 0-99. The instructions tell you which direction to
turn (Right or Left) and by how many units. The initial start is at 50.

How many times while turning based on the instructions do you land exactly on 0?
'''

# Open safe turn directions from input.txt
turns = [line.strip() for line in open('input1.txt').readlines()]
turns = [[t[:1], int(t[1:])] for t in turns]  # [['R', n], ['L', n], ...]
print(f'Num. of turns: {len(turns)}')  # 4671 turns

# Problem 1.1: Number of times landed exactly on 00 while turning 
pos = 50  # initial position
zero_count = 0  # times landed on 00
for turn in turns:
    if turn[0] == 'R':
        pos += turn[1]
    elif turn[0] == 'L':
        pos -= turn[1]
    zero_count += 1 if pos % 100 == 0 else 0
print(f'Problem 1.1: Zero count: {zero_count}')  # Answer: 1177




# for turn in turns:
#     pos = start_pos
#     if turn[0] == 'R':
#         pos += turn[1]
#         if pos >= 100:
#             pos = pos - 100
#             # zero_count += 1
#     elif turn[0] == 'L':
#         pos -= turn[1]
#         if pos < 0:
#             pos = pos + 100
#             # zero_count += 1
#     zero_count += 1 if pos == 0 else 0
        

