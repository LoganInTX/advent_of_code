import re
import math

total = total2 = 0


with open('./2023/day8_input.txt') as f:
    data = f.read().splitlines()

LR = data[0]
path = {}
A = []

for i in range(2, len(data)):
    d = data[i].split(' = ')
    path[d[0]] = (d[1].split(', ')[0][1:], d[1].split(', ')[1][:3])
    if d[0].endswith('A'):
        A.append(d[0])

cur = 'AAA'
i = 0
tot = len(LR)

# while cur != 'ZZZ':
    # cur = path.get(cur)[0] if LR[i % tot] == 'L' else path.get(cur)[1]
    # i+=1

total = i

print(f'Part 1: {total}')

cur = []
next = []
z = set()
i = 0

for a in A:
    next_path = path.get(a)[0] if LR[i % tot] == 'L' else path.get(a)[1]
    cur.append(next_path)
    z.add(next_path[:1:-1])
i += 1

while 'Z' not in z or len(z) > 1:
    z.clear()
    next.clear()
    for c in cur:
        next_path = path.get(c)[0] if LR[i % tot] == 'L' else path.get(c)[1]
        next.append(next_path)
        z.add(next_path[:1:-1])
    i += 1
    cur = next.copy()

total2 = i
print(f'Part 2: {total2}')
