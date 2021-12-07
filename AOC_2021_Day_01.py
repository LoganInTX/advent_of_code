with open('2021/01_input.txt') as f:
    data = [int(x) for x in f.read().splitlines()]

total = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        total += 1

print(f'Part 1: {total}')

total = 0
for i in range(3, len(data)):
    if (data[i] + data[i-1] + data[i-2]) > (data[i-1] + data[i-2] + data[i-3]):
        total += 1

print(f'Part 2: {total}')
