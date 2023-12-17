import re


with open('./2023/day3_input.txt') as f:
    data = f.read().splitlines()

row_w = len(data[0])

total = total2 = 0

gears = {}

def check_num(i, l, r, num):
    for x in range(max(i-1, 0), min(i+2, len(data) - 1)):
        for y in range(max(l-1, 0), min(r+2, row_w - 1)):
            if x == i and y in range(l, r+1):
                continue
            if data[x][y] != '.':
                if data[x][y] == '*':
                    key = str(x) + ',' + str(y)
                    if not gears.get(key):
                        gears[key] = [num]
                    else:
                        gears[key].append(num)
                return True
    return False

for i in range(0, len(data)):
    j = row_w - 1
    while j >= 0:
        if re.match(r'\d', data[i][j]):
            num = int(data[i][j])
            r = l = j
            while re.match(r'\d', data[i][j-1]):
                j -= 1
                l = j
                num += int(data[i][j]) * 10**(r-l)
            result = check_num(i, l, r, num)
            if result:
                total += num
            else:
                print(num)
        j -= 1        

print(f'Part 1: {total}')

for val in gears.values():
    if len(val) == 2:
        total2 += val[0] * val[1]

print(f'Part 2: {total2}')
