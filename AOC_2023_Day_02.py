import re
from math import prod

with open('./2023/day2_input.txt') as f:
    data = f.read().splitlines()

games = {}
limits = { 'red': 12, 'green': 13, 'blue': 14 }

total = total2 = 0
for i in range(0, len(data)):
    game, cube_pulls = data[i].split(': ')
    game = int(game.split(' ')[1])
    for cube_pull in cube_pulls.split('; '):
        cubes = [cube for cube in  cube_pull.split(', ')]

        for cube in cubes:
            num, color = cube.split(' ')
            if not games.get(game):
                games[game]= {color: int(num)}
            elif int(num) > games[game].get(color, 0):
                games[game].update({color: int(num)}) 
    
    total2 += prod(games[game].values())

    for color, num in limits.items():
        if games[game].get(color) > num:
            games.pop(game)
            break

    total = sum(games.keys())
print(f'Part 1: {total}')
    
print(f'Part 2: {total2}')
