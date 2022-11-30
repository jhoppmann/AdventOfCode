def run():
    with open('input.txt') as file:
        input_content = file.read().splitlines()

        ingredients = []
        for line in input_content:
            split_line = line.split(" ")
            ingredient = [int(split_line[2][:-1]),
                          int(split_line[4][:-1]),
                          int(split_line[6][:-1]),
                          int(split_line[8][:-1]),
                          int(split_line[10])]
            ingredients.append(ingredient)

    max_score = 0
    for i in range(1, 101):
        for j in range(1, 101):
            if i + j > 100:
                continue
            for k in range(1, 101):
                if i + j + k > 100:
                    continue
                l = 100 - (i + j + k)
                if l < 0:
                    continue

                c = ingredients[0][0] * i + ingredients[1][0] * j + ingredients[2][0] * k + ingredients[3][0] * l
                d = ingredients[0][1] * i + ingredients[1][1] * j + ingredients[2][1] * k + ingredients[3][1] * l
                f = ingredients[0][2] * i + ingredients[1][2] * j + ingredients[2][2] * k + ingredients[3][2] * l
                t = ingredients[0][3] * i + ingredients[1][3] * j + ingredients[2][3] * k + ingredients[3][3] * l
                cal = ingredients[0][4] * i + ingredients[1][4] * j + ingredients[2][4] * k + ingredients[3][4] * l

                if c < 0 or d < 0 or f < 0 or t < 0:
                    continue
                if cal != 500:
                    continue
                score = c * d * f * t
                max_score = max(max_score, score)

    print(max_score)


if __name__ == '__main__':
    run()
