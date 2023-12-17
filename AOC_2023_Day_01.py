import re

with open('./2023/day1_input.txt') as f:
    data = f.readlines()

word_nums = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
num_nums = { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9 }

patterns = "|".join(num_nums.keys())

# print(data)
total = 0
for i in range(0, len(data)):
    # numbers = re.findall(patterns, data[i])
    nums = re.finditer(f'(?=({patterns}))', data[i])
    numbers = [match.group(1) for match in nums]
    # print(numbers)
    value = (num_nums.get(numbers[0]) * 10) + num_nums.get(numbers[-1])
    # print(value)
    total += int(value) 
    # print(total)

print(f'Part 1: {total}')

all_nums = {**word_nums, **num_nums}
patterns = "|".join(all_nums.keys())

total = 0
for i in range(0, len(data)):
    # numbers = re.findall(patterns, data[i])
    nums = re.finditer(f'(?=({patterns}))', data[i])
    numbers = [match.group(1) for match in nums]
    # print(numbers)
    value = (all_nums.get(numbers[0]) * 10) + all_nums.get(numbers[-1])
    # print(value)
    total += int(value) 
    # print(total)

print(f'Part 2: {total}')
