with open('input.txt') as file:
    instructions = file.read().splitlines()

position = (0, 0)  # (West To East, South To North)
directions = ['N', 'E', 'S', 'W']
facing = 1

for line in instructions:
    instruction = line[0]
    distance = int(line[1:])
    if instruction == 'F':  # seems dirty. I like it.
        instruction = directions[facing]
    if instruction == 'N':
        position = (position[0], position[1] + distance)
    elif instruction == 'S':
        position = (position[0], position[1] - distance)
    elif instruction == 'E':
        position = (position[0] + distance, position[1])
    elif instruction == 'W':
        position = (position[0] - distance, position[1])
    else:
        turns = int(distance / 90)
        if instruction == 'R':
            facing = (facing + turns) % 4
        if instruction == 'L':
            facing = (facing - turns) % 4

print(abs(position[0]) + abs(position[1]))
