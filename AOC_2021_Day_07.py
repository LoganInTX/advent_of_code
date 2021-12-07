import numpy as np

with open('2021/07_input.txt') as f:
    data = [int(n) for n in f.read().split(',')]

crabs = np.array(data)

crabs_median = np.median(crabs)
crabs_dist = np.abs(crabs - crabs_median)
crabs_total_fuel = np.sum(crabs_dist)
print(f'Part 1: {crabs_total_fuel}')

# Since the mean will often fall between two numbers, you need to test both options to find the minimum
crabs_mean1 = np.floor(np.mean(crabs))
crabs_mean2 = np.ceil(np.mean(crabs))
crabs_dist1 = np.abs(crabs - crabs_mean1)
crabs_dist2 = np.abs(crabs - crabs_mean2)
crabs_total_fuel1 = np.sum((crabs_dist1 * (crabs_dist1 + 1)) / 2)
crabs_total_fuel2 = np.sum((crabs_dist2 * (crabs_dist2 + 1)) / 2)
print(f'Part 2: {min(crabs_total_fuel1, crabs_total_fuel2)}')
