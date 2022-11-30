import re

with open('input.txt') as file:
    input_content = file.readlines()

lamps = {}


def switch_lamps(instruction: str) -> None:
    coordinates = re.findall('\\d+,\\d+', instruction)
    lower_right = (int(coordinates[0].split(',')[0]), int(coordinates[0].split(',')[1]))
    upper_left = (int(coordinates[1].split(',')[0]), int(coordinates[1].split(',')[1]))
    for x in range(lower_right[0], upper_left[0] + 1):
        for y in range(lower_right[1], upper_left[1] + 1):
            coordinate = (x, y)
            if 'off' in instruction:
                lamps[coordinate] = False
            elif 'on' in instruction:
                lamps[coordinate] = True
            else:
                if coordinate in lamps:
                    lamps[coordinate] = not lamps[coordinate]
                else:
                    lamps[coordinate] = True


for line in input_content:
    switch_lamps(line)

print(sum(value for value in lamps.values()))
