import re
import math
from itertools import combinations

total = total2 = 0

with open('./2023/dayz11_input.txt') as f:
    data = f.read().splitlines()

galaxies = []
galaxy_rows = []
galaxy_cols = [set() for d in data]
empty_rows = []
empty_cols = []

for d in data:
    row = []
    row = [c for c in d]
    galaxy_rows.append(set(row))
    galaxies.append(row)
    for i, r in enumerate(row):
        galaxy_cols[i].add(r)

for i, row in enumerate(galaxy_rows):
    if '.' in row and len(row) == 1:
        empty_rows.append(i)

for i, col in enumerate(galaxy_cols):
    if '.' in col and len(col) == 1:
        empty_cols.append(i)

g = set()

for i in range(len(galaxies)):
    for j in range(len(galaxies[i])):
        if galaxies[i][j] == '#':
            g.add((i, j))

def find_dist(c, n):
    empty_space = len(set(range(min(c[1][0], c[0][0]), max(c[1][0], c[0][0]) + 1)).intersection(set(empty_rows)))
    empty_space += len(set(range(min(c[1][1], c[0][1]), max(c[1][1], c[0][1]) + 1)).intersection(set(empty_cols)))
    empty_space *= n
    dist = empty_space + abs(c[1][0] - c[0][0]) + abs(c[1][1] - c[0][1])
    return dist

g2 = combinations(g, 2)
for c in g2:
    # print(c)
    dist = find_dist(c, 1)
    # print(dist)
    total += dist

print(f'Part 1: {int(total)}')

g2 = combinations(g, 2)
for c in g2:
    # print(c)
    dist = find_dist(c, 999999)
    # print(dist)
    total2 += dist

print(f'Part 2: {total2}')
