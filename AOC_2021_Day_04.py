from typing import List
import numpy as np

with open('2021/04_input.txt') as f:
    numbers = [int(x) for x in f.readline().split(',')]
    all_boards = f.read().splitlines()

boards = []
i = 0
while i < len(all_boards):
    i += 1
    board = []
    rows = []
    for j in range(5):
        row = []
        for k in range(5):
            row.append(int(all_boards[i][k*3:(k*3)+2]))
        board.append(row)
        i +=1
    # transpose rows and columns
    cols = list(map(list, zip(*board)))
    board.extend(cols)
    boards.append(board)

def find_winning_score(n: List, w: int) -> int:
    w_boards = {}
    for x in range(4, len(n)):
        for b_num, b in enumerate(boards):
            for r in b:
                if set(r).issubset(n[0:x+1]):
                    w_boards[b_num] = 1
                    if len(w_boards) == w:
                        unmarked_nums = np.sum(b[0:5]) - np.sum(np.intersect1d(b[0:5], n[0:x+1]))
                        score = unmarked_nums * n[x]
                        return score
    
    return None

print(f'Part 1: {find_winning_score(numbers, 1)}')
print(f'Part 2: {find_winning_score(numbers, len(boards))}')

