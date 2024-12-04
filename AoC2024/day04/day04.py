def next_letters(x_diff, y_diff, word_grid, x, y) -> bool:
    return (word_grid[x + x_diff][y + y_diff] == 'M'
            and word_grid[x + 2 * x_diff][y + 2 * y_diff] == 'A'
            and word_grid[x + 3 * x_diff][y + 3 * y_diff] == 'S')


def check_for_word(x, y, word_grid) -> int:
    found = 0
    if y >= 3:
        if next_letters(0, -1, word_grid, x, y):
            found += 1
        if x >= 3 and next_letters(-1, -1, word_grid, x, y):
            found += 1
        if x < len(word_grid) - 3 and next_letters(1, -1, word_grid, x, y):
            found += 1
    if y < len(word_grid[x]) - 3:
        if next_letters(0, 1, word_grid, x, y):
            found += 1
        if x >= 3 and next_letters(-1, 1, word_grid, x, y):
            found += 1
        if x < len(word_grid) - 3 and next_letters(1, 1, word_grid, x, y):
            found += 1
    if x >= 3 and next_letters(-1, 0, word_grid, x, y):
        found += 1
    if x < len(word_grid) - 3 and next_letters(1, 0, word_grid, x, y):
        found += 1

    return found


def run():
    with open('input.txt') as file:
        word_grid = file.read().splitlines()

    found_instances = 0
    for x in range(0, len(word_grid)):
        for y in range(0, len(word_grid[x])):
            if word_grid[x][y] == 'X':
                found_instances += check_for_word(x, y, word_grid)
    print("Part 1:", found_instances)


if __name__ == '__main__':
    run()
