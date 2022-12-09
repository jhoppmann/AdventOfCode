def run():
    with open('input.txt') as file:
        topographic_scan = file.read().splitlines()

    height_map = []
    for line in topographic_scan:
        height_map.append([int(x) for x in list(line)])

    highest_score = 0

    for row in range(0, len(height_map)):
        for column in range(0, len(height_map[row])):
            tree = height_map[row][column]
            up, down, left, right = 0, 0, 0, 0
            for row_offset in range(1, len(height_map) - row):
                if height_map[row + row_offset][column] >= tree or row + row_offset == len(height_map) - 1:
                    down = row_offset
                    break

            for row_offset in range(1, row + 1):
                if height_map[row - row_offset][column] >= tree or row - row_offset == 0:
                    up = row_offset
                    break

            for column_offset in range(1, len(height_map[row]) - column) :
                if height_map[row][column + column_offset] >= tree or column + column_offset == len(height_map[row]) - 1:
                    right = column_offset
                    break

            for column_offset in range(1, column + 1):
                if height_map[row][column - column_offset] >= tree or column-column_offset == 0:
                    left = column_offset
                    break

            score = up * down * left * right
            highest_score = max(highest_score, score)

    print(highest_score)




if __name__ == '__main__':
    run()
