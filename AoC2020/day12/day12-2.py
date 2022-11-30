with open('input.txt') as file:
    instructions = file.read().splitlines()

position = (0, 0)
position_wp = (10, 1)  # (West To East, South To North)
directions = ['N', 'E', 'S', 'W']
facing = 1

for line in instructions:
    instruction = line[0]
    distance = int(line[1:])
    if instruction == 'N':
        position_wp = (position_wp[0], position_wp[1] + distance)
    if instruction == 'S':
        position_wp = (position_wp[0], position_wp[1] - distance)
    if instruction == 'E':
        position_wp = (position_wp[0] + distance, position_wp[1])
    if instruction == 'W':
        position_wp = (position_wp[0] - distance, position_wp[1])
    if instruction == 'R' or instruction == 'L':
        turns = int(distance / 90) % 4
        for i in range(turns):
            if instruction == 'R':
                position_wp = (position_wp[1], -position_wp[0])
            if instruction == 'L':
                position_wp = (-position_wp[1], position_wp[0])
    if instruction == 'F':
        position = (position[0] + position_wp[0]*distance, position[1] + position_wp[1]*distance)

    print(instruction, distance, position, position_wp)
print(abs(position[0]) + abs(position[1]))
