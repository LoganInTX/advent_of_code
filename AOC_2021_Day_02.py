with open('2021/02_input.txt') as f:
    data = f.read().splitlines()

x = y = 0
for d in data:
    cmd, n = d.split()
    if cmd == 'forward':
        x += int(n)
    elif cmd == 'down':
        y += int(n)
    elif cmd == 'up':
        y -= int(n)
    
print(f'Part 1: {x * y}')

x = y = aim = 0
for d in data:
    cmd, n = d.split()
    n = int(n)
    if cmd == 'forward':
        x += n
        y += (n * aim)
    elif cmd == 'down':
        aim += n
    elif cmd == 'up':
        aim -= n

print(f'Part 2: {x * y}')
