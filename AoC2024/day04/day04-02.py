def next_letters(x_diff, y_diff, word_grid, x, y) -> bool:
    if word_grid[x + x_diff][y + y_diff] == 'M':
        return word_grid[x - x_diff][y - y_diff] == 'S'
    if word_grid[x + x_diff][y + y_diff] == 'S':
        return word_grid[x - x_diff][y - y_diff] == 'M'
    return False


def check_for_word(x, y, word_grid) -> int:
    found = 0
    if next_letters(-1, -1, word_grid, x, y) and next_letters(1, -1, word_grid, x, y):
        found += 1

    return found


def run():
    with open('input.txt') as file:
        word_grid = file.read().splitlines()

    found_instances = 0
    for x in range(1, len(word_grid) - 1):
        for y in range(1, len(word_grid[x]) - 1):
            if word_grid[x][y] == 'A':
                found_instances += check_for_word(x, y, word_grid)
    print("Part 2:", found_instances)


if __name__ == '__main__':
    run()
