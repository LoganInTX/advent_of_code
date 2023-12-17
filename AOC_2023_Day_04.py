import re


with open('./2023/day4_input.txt') as f:
    data = f.read().splitlines()

scratchcards = {}

total = total2 = 0

for i in range(0, len(data)):
    x = data[i].split(': ')
    card = int(x[0].split()[1])
    numbers = x[1].split(' | ')
    win_nums = set(numbers[0].split())
    your_nums = set(numbers[1].split())
    wins = len(win_nums.intersection(your_nums))
    points = 2**(wins - 1) if wins > 0 else 0
    total += points

    scratchcards[card] = [wins, 1, points]

for scratchcard in scratchcards.items():
    for i in range(scratchcard[1][1]):
        for j in range(1, scratchcard[1][0] + 1):
            scratchcards[scratchcard[0] + j][1] += 1

for scratchcard in scratchcards.values():
    total2 += scratchcard[1]

print(f'Part 1: {total}')

print(f'Part 2: {total2}')
