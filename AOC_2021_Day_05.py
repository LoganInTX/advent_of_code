from collections import defaultdict

# Process the input data into a list
with open('2021/05_input.txt') as f:
    data = f.read().splitlines()

# create an object defintion to store points
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __repr__(self) -> str:
        return str(self.x) + ',' + str(self.y)

# use a default dict to keep score of how many times a point was crossed
grid = defaultdict(int)

# Go through each point in the input
for d in data:
    p1, p2 = d.split(' -> ')
    p1 = Point(*p1.split(','))
    p2 = Point(*p2.split(','))

    # for vertical lines
    if p1.x == p2.x:
        for i in range(min(p1.y, p2.y), max(p1.y, p2.y) + 1):
            grid[str(p1.x) + ',' + str(i)] += 1

    # for horizontal lines
    if p1.y == p2.y:
        for i in range(min(p1.x, p2.x), max(p1.x, p2.x) + 1):
            grid[str(i) + ',' + str(p1.y)] += 1

print(f'Part 1: {sum([1 for p in grid.values() if p >= 2])}')

for d in data:
    p1, p2 = d.split(' -> ')
    p1 = Point(*p1.split(','))
    p2 = Point(*p2.split(','))

    # for diagonal lines, determine the direction and how to increment/defrement the x,y values
    if abs(p1.x - p2.x) == abs(p1.y - p2.y):
        point_count = abs(p1.x - p2.x) + 1
        if p1.x < p2.x and p1.y < p2.y:
            for i in range(point_count):
                grid[str(p1.x + i) + ',' + str(p1.y + i)] += 1
        elif p1.x < p2.x and p1.y > p2.y:
            for i in range(point_count):
                grid[str(p1.x + i) + ',' + str(p1.y - i)] += 1
        elif p1.x > p2.x and p1.y > p2.y:
            for i in range(point_count):
                grid[str(p1.x - i) + ',' + str(p1.y - i)] += 1
        elif p1.x > p2.x and p1.y < p2.y:
            for i in range(point_count):
                grid[str(p1.x - i) + ',' + str(p1.y + i)] += 1
    
print(f'Part 2: {sum([1 for p in grid.values() if p >= 2])}')
