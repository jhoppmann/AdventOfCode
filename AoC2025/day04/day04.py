from typing import Any


def run():
    with open('input.txt') as file:
        warehouse = file.read().splitlines()

    result = remove_possible_rolls(warehouse)
    print('Part 1:', result[0])

    running_total_rolls = 0
    while True:
        (rolls, new_warehouse) = remove_possible_rolls(warehouse)
        running_total_rolls += rolls
        if warehouse == new_warehouse:
            break
        else:
            warehouse = new_warehouse

    print('Part 2:', running_total_rolls)


def check_adjacent_spots(warehouse, x, y) -> bool:
    adjacent_rolls = 0
    num_rows = len(warehouse)
    num_cols = len(warehouse[y])
    for line_shift in range(-1, 2):
        for col_shift in range(-1, 2):
            new_col_index = x + col_shift
            new_row_index = y + line_shift
            if 0 <= new_row_index < num_rows and 0 <= new_col_index < num_cols and not (
                    col_shift == 0 and line_shift == 0) \
                    and warehouse[new_row_index][new_col_index] == '@':
                adjacent_rolls += 1
    return adjacent_rolls < 4


def remove_possible_rolls(warehouse: list[str]) -> tuple[int, list[str]]:
    removable_rolls = 0
    warehouse_after_removal: list[str] = []
    for y in range(len(warehouse)):
        row_after_removal = []
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == '@':
                if check_adjacent_spots(warehouse, x, y):
                    removable_rolls += 1
                    print(y, x)
                    row_after_removal.append('.')
                else:
                    row_after_removal.append('@')
            else:
                row_after_removal.append('.')
        warehouse_after_removal.append(''.join(row_after_removal))
    return removable_rolls, warehouse_after_removal


if __name__ == '__main__':
    run()
