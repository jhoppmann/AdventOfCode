from copy import deepcopy


def contains_loop(starting_position: tuple, position: tuple, grid: list) -> bool:
    line = list(grid[position[1]])
    line[position[0]] = '#'
    grid[position[1]] = ''.join(line)
    current_position = starting_position
    current_direction = 'N'
    path = set()
    while True:
        if will_leave(grid, current_position, current_direction):
            return False
        elif next_tile(current_position, current_direction, grid) == '#':
            current_direction = turn(current_direction)
        else:
            current_position = move(current_position, current_direction)
            if (current_position, current_direction) in path:
                return True
            path.add((current_position, current_direction))


def run():
    with open('input.txt') as file:
        grid = file.read().splitlines()

    current_position = (0, 0)
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == '^':
                current_position = (x, y)
    starting_position = current_position
    path = set()
    path.add(current_position)
    current_direction = 'N'

    while True:
        if will_leave(grid, current_position, current_direction):
            break
        elif next_tile(current_position, current_direction, grid) == '#':
            current_direction = turn(current_direction)
        else:
            current_position = move(current_position, current_direction)
            path.add(current_position)

    possible_obstacle_positions = 0
    for position in path:
        if contains_loop(starting_position, position, deepcopy(grid)):
            possible_obstacle_positions += 1
    print('Part 1:', len(path))
    print('Part 2:', possible_obstacle_positions)


def will_leave(grid, current_pos, current_direction):
    if current_direction == 'N' and current_pos[1] == 0:
        return True
    if current_direction == 'W' and current_pos[0] == 0:
        return True
    if current_direction == 'S' and current_pos[1] == len(grid[0]) - 1:
        return True
    if current_direction == 'E' and current_pos[0] == len(grid) - 1:
        return True


def next_tile(current_position, current_direction, grid):
    pos = get_next_pos(current_position, current_direction)
    return grid[pos[1]][pos[0]]


def move(current_position, current_direction) -> tuple:
    return get_next_pos(current_position, current_direction)


def get_next_pos(current_position, current_direction) -> tuple:
    if current_direction == 'N':
        return current_position[0], current_position[1] - 1
    if current_direction == 'E':
        return current_position[0] + 1, current_position[1]
    if current_direction == 'S':
        return current_position[0], current_position[1] + 1
    if current_direction == 'W':
        return current_position[0] - 1, current_position[1]


def turn(current_direction: str) -> str:
    if current_direction == 'N':
        return 'E'
    if current_direction == 'E':
        return 'S'
    if current_direction == 'S':
        return 'W'
    if current_direction == 'W':
        return 'N'


if __name__ == '__main__':
    run()
