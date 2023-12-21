import re
import math

total = total2 = 0


with open('./2023/day9_input.txt') as f:
    data = f.read().splitlines()

oasis = []
for d in data:
    oasis.append([[int(n) for n in d.split()]])

for o in oasis:
    next_level = []

    for j in range(1, len(o[0])):
        next_level.append(o[0][j] - o[0][j-1])
    o.append(next_level)

    while set(next_level) != {0}:
        next_level = []
        for j in range(1, len(o[-1])):
            next_level.append(o[-1][j] - o[-1][j-1])
        o.append(next_level)

for o in oasis:
    for i in range(1, len(o)):
        o[len(o)-i-1].append(o[len(o)-i-1][-1] + o[len(o)-i][-1])
    total += o[0][-1]
    print(o[0])

print(f'Part 1: {total}')

for o in oasis:
    for i in range(1, len(o)):
        o[len(o)-i-1].insert(0, o[len(o)-i-1][0] - o[len(o)-i][0])
    total2 += o[0][0]

print(f'Part 2: {total2}')
