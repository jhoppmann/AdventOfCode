import re


def run():
    with open('input.txt') as file:
        cards = file.read().splitlines()

    card_by_number = {}
    for card in cards:
        card_number = int(card[0:8][-3:])
        number_lists = card[10:].split('|')

        for i in range(0, len(number_lists)):
            number_lists[i] = [int(x) for x in re.findall(r'\d+', number_lists[i])]
        card_by_number[card_number] = number_lists

    cards_owned = {x: 1 for x in range(1, len(card_by_number.keys()) + 1)}

    for current_card_number in range(1, len(card_by_number.keys()) + 1):
        game_numbers = card_by_number[current_card_number]
        points = 0
        for number in game_numbers[1]:
            if number in game_numbers[0]:
                points += 1
        bonus_cards_index = current_card_number + 1
        for i in range(0, points):
            if bonus_cards_index + i in cards_owned:
                cards_owned[bonus_cards_index + i] += cards_owned[current_card_number]
        print(current_card_number, points, cards_owned)
    print(sum(cards_owned.values()))


if __name__ == '__main__':
    run()
