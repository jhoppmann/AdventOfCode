def get_new_facing(facing, turn):
    new_facing = ''
    if turn == 'R':
        if facing == 'N':
            new_facing = 'E'
        elif facing == 'E':
            new_facing = 'S'
        elif facing == 'S':
            new_facing = 'W'
        elif facing == 'W':
            new_facing = 'N'
    elif turn == 'L':
        if facing == 'N':
            new_facing = 'W'
        elif facing == 'W':
            new_facing = 'S'
        elif facing == 'S':
            new_facing = 'E'
        elif facing == 'E':
            new_facing = 'N'
    return new_facing


def manhattan_distance(position: tuple) -> int:
    return abs(position[0]) + abs(position[1])


def run():
    with open('input.txt') as file:
        directions = file.read()
    directions = [x for x in directions.split(", ")]
    facing = 'N'
    position = (0, 0)

    for d in directions:
        turn = d[0]
        distance = int(d[1:])
        facing = get_new_facing(facing, turn)
        if facing == 'E':
            position = (position[0], position[1] + distance)
        elif facing == 'S':
            position = (position[0] - distance, position[1])
        elif facing == 'W':
            position = (position[0], position[1] - distance)
        elif facing == 'N':
            position = (position[0] + distance, position[1])

    print(position, manhattan_distance(position))


if __name__ == '__main__':
    run()
