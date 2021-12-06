from collections import deque
from typing import Deque

with open('2021/06_input.txt') as f:
    data = [int(n) for n in f.read().split(',')]

def setup_fish(days: int) -> Deque:
    fish = deque(maxlen=days)
    for i in range(days):
        fish.append(0)
    for d in data:
        fish[d] += 1
    return fish

def process_day(f: Deque):
    new_fish = f[0]
    f.rotate(-1)
    f[6] += new_fish


def count_fish(f: Deque, days: int) -> int:
    for day in range(days):
        process_day(f)
    return sum(f)

fish = setup_fish(9)
print(f'Part 1: {count_fish(fish, 80)}')
fish = setup_fish(9)
print(f'Part 2: {count_fish(fish, 256)}')
