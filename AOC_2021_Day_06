from collections import defaultdict
from typing import DefaultDict

with open('2021/06_input.txt') as f:
    data = [int(n) for n in f.read().split(',')]

def setup_fish() -> DefaultDict:
    fish = defaultdict(int)
    for d in data:
        fish[d] += 1
    return fish

def process_day(f: DefaultDict):
    new_fish = f[0]
    f[0] = 0
    for i in range(8):
        f[i] += f[i+1]
        f[i+1] = 0
    f[6] += new_fish
    f[8] += new_fish

def count_fish(f: DefaultDict, days: int) -> int:
    for day in range(days):
        process_day(f)
    return sum(f.values())

fish = setup_fish()
print(f'Part 1: {count_fish(fish, 80)}')
fish = setup_fish()
print(f'Part 2: {count_fish(fish, 256)}')
