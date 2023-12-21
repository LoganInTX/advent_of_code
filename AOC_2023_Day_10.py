import re
import math

total = total2 = 0

symbols = {'-': ((0, -1), (0, 1)), '|': ((-1, 0), (1, 0)), '7': ((0, -1), (1, 0)), 'L': ((-1, 0), (0, 1)), 'F': ((1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)), '.': ((-9999, -9999), (-9999, -9999)), 'S': ((-9999, -9999), (-9999, -9999))}

with open('./2023/dayz10_input.txt') as f:
    data = f.read().splitlines()

def get_connectors(c, x, y):
    a = symbols.get(c)
    return ((x+a[0][0], y+a[0][1]), (x+a[1][0], y+a[1][1]))

map = []
start = [0,0]
for i, d in enumerate(data):
    maprow = []
    for j, c in enumerate(d):
        maprow.append(get_connectors(c, i, j))
        if c == 'S':
            start = (i, j)
    map.append(maprow)

# map[start[0]][start[1]] = ()

def find_first_move(x, y, last):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x+i, y+j) != last:
                if (x, y) in map[x+i][y+j] or (x+i, y+j) == start:
                    return (x+i, y+j)

def find_next_move(x, y, last):
    next = list(set(map[x][y]).difference(set([last])))
    return next[0]

last = start
next = find_first_move(*start, last)
last = start
total += 1

while next != start:
    total += 1
    cur = next
    next = find_next_move(*next, last)
    last = cur

total /= 2
print(f'Part 1: {int(total)}')



print(f'Part 2: {total2}')
