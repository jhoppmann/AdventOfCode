import re
import math


def run():
    with open('input.txt') as file:
        games = file.read().splitlines()

    id_sum = 0
    power_sum = 0
    maxima = {'red': 12, 'green': 13, 'blue': 14}
    for game in games:
        max_draws_by_color = {}
        game_num = int((re.search(r'\d+', game.split(':')[0])).group(0))
        draws = game.split(':')[1].split(';')
        draws = [str.strip(x) for x in draws]
        for draw in draws:
            for color in draw.split(','):
                color = str.strip(color)
                num = int(color.split(' ')[0])
                color_name = color.split(' ')[1]
                if color_name in max_draws_by_color:
                    max_draws_by_color[color_name] = max(num, max_draws_by_color[color_name])
                else:
                    max_draws_by_color[color_name] = num
        for color, num in max_draws_by_color.items():
            if maxima[color] < num:
                break
        else:
            id_sum += game_num
        power_sum += math.prod(max_draws_by_color.values())
    print("Part 1:", id_sum)
    print("Part 2:", power_sum)


if __name__ == '__main__':
    run()
