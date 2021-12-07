from statistics import mean

with open('2021/03_input.txt') as f:
    data = f.read().splitlines()

data_len = len(data[0])
data2 = list(map(list, zip(*data)))

gamma = ''
epsilon = ''
for i in range(len(data2)):
    d = [int(x) for x in data2[i]]
    half_data_len = len(d) / 2
    gamma += '1' if sum(d) > half_data_len else '0'
    epsilon += '1' if sum(d) < half_data_len else '0'

print(f'Part 1: {int(gamma, base=2) * int(epsilon, base=2)}')

data3 = [int(x, base=2) for x in data]
oxygen = data3.copy()
for i in range(data_len):
    # x & 2^(data_len - i) == 2^(data_len - i)
    sum1 = sum([1 for x in oxygen if (x >> (data_len - i - 1)) & 1])
    if sum1 >= (len(oxygen) / 2):
        oxygen = [x for x in oxygen if (x >> (data_len - i - 1)) & 1]
    else:
        oxygen = [x for x in oxygen if not ((x >> (data_len - i - 1)) & 1)]

    if len(oxygen) == 1:
        break

co2 = data3.copy()
for i in range(data_len):
    # x & 2^(data_len - i) == 2^(data_len - i)
    sum1 = sum([1 for x in co2 if (x >> (data_len - i - 1)) & 1])
    if sum1 >= (len(co2) / 2):
        co2 = [x for x in co2 if not ((x >> (data_len - i - 1)) & 1)]
    else:
        co2 = [x for x in co2 if (x >> (data_len - i - 1)) & 1]

    if len(co2) == 1:
        break

print(f'Part 2: {oxygen[0] * co2[0]}')



