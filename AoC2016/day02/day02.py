def run():
    with open('input.txt') as file:
        directions = file.read().splitlines()

    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    position = (1, 1)
    code = ''

    for line in directions:
        for direction in line:
            print(direction)
            if direction == 'U':
                position = (max(0, position[0] - 1), position[1])
            elif direction == 'D':
                position = (min(2, position[0] + 1), position[1])
            elif direction == 'L':
                position = (position[0], max(0, position[1] - 1))
            elif direction == 'R':
                position = (position[0], min(2, position[1] + 1))
        code += str(keypad[position[0]][position[1]])

    print(code)


if __name__ == '__main__':
    run()
