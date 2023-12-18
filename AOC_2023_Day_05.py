import re


with open('./2023/day5_input.txt') as f:
    seeds = f.readline().strip().split(': ')[1].split()
    print(f'seeds: {seeds}')
    f.readlines(2)
    seed_soils = []
    seed_soil = f.readline().strip().split()
    
    while seed_soil:
        seed_soils.append(seed_soil)
        seed_soil = f.readline().strip().split()

    f.readlines(2)
    soil_ferts = []
    soil_fert = f.readline().strip().split()

    while soil_fert:
        soil_ferts.append(soil_fert)
        soil_fert = f.readline().strip().split()

    f.readlines(2)
    fert_waters = []
    fert_water = f.readline().strip().split()

    while fert_water:
        fert_waters.append(fert_water)
        fert_water = f.readline().strip().split()

    f.readlines(2)
    water_lights = []
    water_light = f.readline().strip().split()

    while water_light:
        water_lights.append(water_light)
        water_light = f.readline().strip().split()

    f.readlines(2)
    light_temps = []
    light_temp = f.readline().strip().split()

    while light_temp:
        light_temps.append(light_temp)
        light_temp = f.readline().strip().split()

    f.readlines(2)
    temp_hums = []
    temp_hum = f.readline().strip().split()

    while temp_hum:
        temp_hums.append(temp_hum)
        temp_hum = f.readline().strip().split()

    f.readlines(2)
    hum_locs = []
    hum_loc = f.readline().strip().split()

    while hum_loc:
        hum_locs.append(hum_loc)
        hum_loc = f.readline().strip().split()

total = total2 = 0
seed_locs = []
seed_locs2 = []


def find_map_dest(map, source, found, cantfind):
    for m in map:
        if source >= int(m[1]) and source <= int(m[1]) + int(m[2]) - 1:
            return source + int(m[0]) - int(m[1]), (found and True), False
        else:
            if source > int(m[1]) + int(m[2]) - 1:
                cantfind |= True
    return source, False, cantfind
            


def find_seed_loc(seed):
    found = True
    cantfind = True
    dest, found, cantfind = find_map_dest(seed_soils, seed, found, cantfind)
    dest, found, cantfind = find_map_dest(fert_waters, dest, found, cantfind)
    dest, found, cantfind = find_map_dest(water_lights, dest, found, cantfind)
    dest, found, cantfind = find_map_dest(soil_ferts, dest, found, cantfind)
    dest, found, cantfind = find_map_dest(light_temps, dest, found, cantfind)
    dest, found, cantfind = find_map_dest(temp_hums, dest, found, cantfind)
    dest, found, cantfind = find_map_dest(hum_locs, dest, found, cantfind)
    return dest, found, cantfind

for seed in seeds:
    seed_locs.append(find_seed_loc(int(seed)))

total = min(seed_locs)
print(f'Part 1: {total}')

total2 = 2**32
for i in range(int(len(seeds)/2)):
    for s1 in range(int(seeds[i*2]), int(seeds[i*2]) + int(seeds[(i*2)+1])):
        loc, found, cantfind = find_seed_loc(s1)
        if loc < total2:
            total2 = loc
        if found or cantfind:
            break

print(f'Part 2: {total2}')
