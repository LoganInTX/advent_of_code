import re
import math

with open('./2023/day6_input.txt') as f:
    data = f.read().splitlines()
    
times = data[0].split(':')[1].split()
dists = data[1].split(':')[1].split()

records = []

for i, time in enumerate(times):
    record = 0
    t = int(time)
    d = int(dists[i])
    print(i+1,t)
    for j in range(1, t + 1):
        d2 = (t-(j))*(j)
        if d2 > d:
            record += 1
    records.append(record)

total = math.prod(records)


print(f'Part 1: {total}')

t2 = int(''.join(times))
d2 = int(''.join(dists))

record = 0
for i in range(1, t2 + 1):
    d = (t2-(i))*(i)
    if d > d2:
        record += 1

print(t2, d2)
total2 = record
print(f'Part 2: {total2}')
