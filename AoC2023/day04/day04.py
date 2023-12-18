import re


def run():
    with open('input.txt') as file:
        cards = file.read().splitlines()

    points_running_total = 0
    for card in cards:
        card_name = card[0:8]
        number_lists = card[10:].split('|')

        for i in range(0, len(number_lists)):
            number_lists[i] = [int(x) for x in re.findall(r'\d+', number_lists[i])]

        game_worth = 0
        for number in number_lists[1]:
            if number in number_lists[0]:
                game_worth = max(2 * game_worth, 1)

        points_running_total += game_worth
    print(points_running_total)


if __name__ == '__main__':
    run()
