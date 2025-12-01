def run():
    with open('input.txt') as file:
        movements = file.read().splitlines()

    position = 50
    result = 0
    result_part_two = 0

    for move in movements:
        direction = move[0]
        clicks = int(move[1:])
        for i in range(clicks):
            if direction == 'R':
                position += 1
            elif direction == 'L':
                position -= 1
            else:
                raise ValueError
            if position % 100 == 0:
                result_part_two += 1

        position %= 100
        if position <= 0:
            position = -position
        if position == 0:
            result += 1

    print (result)
    print (result_part_two)


if __name__ == '__main__':
    run()