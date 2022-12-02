def run():
    with open('input.txt') as file:
        guide = file.read().splitlines()

    score = 0
    values = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    for line in guide:
        hand_shapes = line.split(" ")
        score += values[hand_shapes[1]]

        if values[hand_shapes[1]] == values[hand_shapes[0]]:
            score += 3
        elif values[hand_shapes[0]] == 1:
            if values[hand_shapes[1]] == 2:
                score += 6
            else:
                score += 0
        elif values[hand_shapes[0]] == 2:
            if values[hand_shapes[1]] == 3:
                score += 6
            else:
                score += 0
        elif values[hand_shapes[0]] == 3:
            if values[hand_shapes[1]] == 1:
                score += 6
            else:
                score += 0
    print(score)


if __name__ == '__main__':
    run()