'''Day 1: Historian Hysteria (https://adventofcode.com/2024/day/1)

Problem 1.1: Compare two lists of numbers, arrange each in increasing value, 
pair them based on value, and take the difference between each value. What is the 
sum of the total difference (i.e. the total distance score) between them?'''

import pandas as pd
import re

# Load in .txt file of lists
df = pd.read_csv('input1.txt', sep=r'\s+', header=None)

# Select & sort each column - returns lists
lst1 = sorted(df[0])
lst2 = sorted(df[1])

# Find difference between values of each list
diff = []
for i in range(len(lst1)):
    diff.append(abs(lst1[i] - lst2[i]))
total_dist = sum(diff)
print(total_dist)

'''Problem 1.2: The two lists have many of the same values. How many times do 
values from the left list appear in the right list (i.e. a similarity score)? 
Note: this does not mean only looking at unique instances for each left value.'''

from collections import Counter
from itertools import islice

# Count the instances of values from lst1 appearing in lst2
lst1_counts = Counter()
for num in lst1:
    lst1_counts[num] = lst2.count(num)
# lst1_first10 = dict(islice(lst1_counts.items(), 10)) # yields first 10 key-val pairs
lst1_dict = dict(lst1_counts)

# Multiply number of occurences of each lst1 values to find similarity score
num_occur = []
for key, val in lst1_dict.items():
    num_occur.append(key*val)
sim_score = sum(num_occur)
print(sim_score)