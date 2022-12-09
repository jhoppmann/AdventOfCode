def run():
    with open('input.txt') as file:
        topographic_scan = file.read().splitlines()

    height_map = []
    for line in topographic_scan:
        height_map.append([int(x) for x in list(line)])

    trees_seen = set()

    for index in range(0, len(height_map[0])):
        trees_seen.add((0, index))
        trees_seen.add((len(height_map)-1, index))

    for index in range(0, len(height_map)):
        trees_seen.add((index, 0))
        trees_seen.add((index, len(height_map[0]) - 1))

    for row in range(1, len(height_map)):
        min_tree_height = height_map[row][0]
        for column in range(1, len(height_map[row]) - 1):
            if height_map[row][column] > min_tree_height:
                trees_seen.add((row, column))
                min_tree_height = height_map[row][column]

        min_tree_height = height_map[row][-1]
        for column in range(2, len(height_map[row])):
            if height_map[row][-column] > min_tree_height:
                trees_seen.add((row, len(height_map[row]) - column))
                min_tree_height = height_map[row][-column]

    for column in range(1, len(height_map[0]) - 1):
        min_tree_height = height_map[0][column]
        for row in range(1, len(height_map) - 1):
            if height_map[row][column] > min_tree_height:
                trees_seen.add((row, column))
                min_tree_height = height_map[row][column]

        min_tree_height = height_map[-1][column]
        for row in range(2, len(height_map)):
            if height_map[-row][column] > min_tree_height:
                trees_seen.add((len(height_map) - row, column))
                min_tree_height = height_map[-row][column]

    print(len(trees_seen))


if __name__ == '__main__':
    run()
