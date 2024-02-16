def find_starting_position(pipe_map: list) -> tuple:
    for index, row in enumerate(pipe_map):
        if 'S' in row:
            return row.index('S'), index
    return -1, -1


def get(pipe_map, position) -> str:
    max_x = len(pipe_map[0])
    max_y = len(pipe_map)
    if position[0] < 0 or position[1] < 0 or position[1] >= max_x or position[0] >= max_y:
        return '.'
    else:
        return pipe_map[position[1]][position[0]]


def find_starting_heading(pipe_map: list, position: tuple) -> int:
    east_tile = get(pipe_map, (position[0] - 1, position[1]))
    if east_tile == '-' or east_tile == 'F' or east_tile == 'L':
        return EAST
    west_tile = get(pipe_map, (position[0] + 1, position[1]))
    if west_tile == '-' or west_tile == 'J' or west_tile == '7':
        return WEST
    north_tile = get(pipe_map, (position[0], position[1] - 1))
    if north_tile == '|' or north_tile == 'F' or north_tile == '7':
        return NORTH
    south_tile = get(pipe_map, (position[0], position[1] + 1))
    if south_tile == '|' or south_tile == 'J' or south_tile == 'L':
        return SOUTH

    raise ValueError


def get_next_position_in_heading(position: tuple, heading: int) -> tuple:
    if heading == NORTH:
        return position[0], position[1] - 1
    elif heading == SOUTH:
        return position[0], position[1] + 1
    elif heading == EAST:
        return position[0] + 1, position[1]
    elif heading == WEST:
        return position[0] - 1, position[1]
    raise ValueError(heading)


def get_new_heading(symbol: str, heading: int) -> int:
    if symbol == '|' or symbol == '-':
        return heading
    if symbol == '7':
        if heading == NORTH:
            return WEST
        else:
            return SOUTH
    if symbol == 'F':
        if heading == NORTH:
            return EAST
        else:
            return SOUTH
    if symbol == 'L':
        if heading == SOUTH:
            return EAST
        else:
            return NORTH
    if symbol == 'J':
        if heading == SOUTH:
            return WEST
        else:
            return NORTH
    raise ValueError(symbol)


def run():
    with open('input.txt') as file:
        pipe_map = file.read().splitlines()

    current_position = find_starting_position(pipe_map)
    heading = find_starting_heading(pipe_map, current_position)

    waypoints = [current_position]
    loop_done = False
    while not loop_done:
        current_position = get_next_position_in_heading(current_position, heading)
        if get(pipe_map, current_position) == 'S':
            loop_done = True
        else:
            heading = get_new_heading(get(pipe_map, current_position), heading)
            waypoints.append(current_position)
        print(get(pipe_map, current_position), heading)
    print('Part 1:', int(len(waypoints) / 2))


NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
if __name__ == '__main__':
    run()
