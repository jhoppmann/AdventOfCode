from pprint import pprint


def calculate_new_value(line, column, grid):
    count_on = 0
    if (line == 0 and column == 0) or (line == 99 and column == 0) or \
            (line == 0 and column == 99) or (line == 99 and column == 99):
        return True
    for line_shift in range(-1, 2):
        for col_shift in range(-1, 2):
            new_col_index = column + col_shift
            new_row_index = line + line_shift
            if 0 <= new_row_index < 100 and 0 <= new_col_index < 100 and not (col_shift == 0 and line_shift == 0) \
                    and grid[new_row_index][new_col_index]:
                count_on += 1
    if grid[line][column] and (count_on == 2 or count_on == 3):
        return True
    if not grid[line][column] and count_on == 3:
        return True
    return False


def compute_new(grid: list) -> list:
    new_grid = []
    for line in range(0, 100):
        new_line = []
        for column in range(0, 100):
            new_line.append(calculate_new_value(line, column, grid))
        new_grid.append(new_line)
    return new_grid


def run():
    generations = 100
    with open('input.txt') as file:
        input_content = file.readlines()
    grid = []
    for line in input_content:
        new_line = []
        for char in line:
            new_line.append(char == '#')
        grid.append(new_line)
    grid[0][0] = True
    grid[0][99] = True
    grid[99][0] = True
    grid[99][99] = True

    for _ in range(generations):
        grid = compute_new(grid)
        pass

    on = 0
    for line in grid:
        on += line.count(True)

    print(on)


if __name__ == '__main__':
    run()
