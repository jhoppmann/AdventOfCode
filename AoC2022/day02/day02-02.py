def run():
    with open('input.txt') as file:
        guide = file.read().splitlines()

    score = 0
    values = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    for line in guide:
        hand_shapes = line.split(' ')
        score += values[hand_shapes[1]]

        if values[hand_shapes[0]] == 1:
            if values[hand_shapes[1]] == 0:
                score += 3
            elif values[hand_shapes[1]] == 3:
                score += 1
            elif values[hand_shapes[1]] == 6:
                score += 2
        elif values[hand_shapes[0]] == 2:
            if values[hand_shapes[1]] == 0:
                score += 1
            elif values[hand_shapes[1]] == 3:
                score += 2
            elif values[hand_shapes[1]] == 6:
                score += 3
        elif values[hand_shapes[0]] == 3:
            if values[hand_shapes[1]] == 0:
                score += 2
            elif values[hand_shapes[1]] == 3:
                score += 3
            elif values[hand_shapes[1]] == 6:
                score += 1
    print(score)


if __name__ == '__main__':
    run()
