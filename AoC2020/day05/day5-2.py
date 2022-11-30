import math

with open('input.txt') as file:
    boarding_passes = file.read().splitlines()


def calc_ids(line) -> int:
    row_lower = 0
    row_upper = 127
    column_lower = 0
    column_upper = 7
    for char in line[0:7]:
        middle = math.ceil((row_upper + row_lower) / 2)
        if char == 'B':
            row_lower = middle
        if char == 'F':
            row_upper = middle - 1
    for char in line[7:]:
        middle = math.ceil((column_upper + column_lower) / 2)
        if char == 'R':
            column_lower = middle
        if char == 'L':
            column_upper = middle - 1
    return row_upper * 8 + column_upper


ids = [calc_ids(x) for x in boarding_passes]
ids.sort()

for i in range(1, len(ids) - 1):
    if ids[i] + 1 != ids[i+1]:
        print(ids[i] + 1)
