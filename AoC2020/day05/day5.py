import math

with open('input.txt') as file:
    boarding_passes = file.read().splitlines()

result = 0
for line in boarding_passes:
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
    result = max(result, column_upper + row_upper*8)

print(result)
