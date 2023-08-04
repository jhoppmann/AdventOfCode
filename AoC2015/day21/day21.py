from itertools import product

from AoC2015.day21.Character import Character
from Item import Item
import copy


def build_characters(equipment):
    characters = []

    for combination in equipment:
        armor = 0
        damage = 0
        cost = 0
        for item in combination:
            armor += item.armor
            damage += item.damage
            cost += item.cost
        character = Character(100, damage=damage, armor=armor)
        characters.append((character, cost))

    characters.sort(key=lambda x: x[1])
    return characters


def does_char_win(character: Character, boss: Character):
    boss = copy.deepcopy(boss)
    character = copy.deepcopy(character)
    while True:
        boss.hp = boss.hp - max(0, character.damage - boss.armor)
        if boss.hp <= 0:
            return True
        character.hp = character.hp - max(0, boss.damage - character.armor)
        if character.hp <= 0:
            return False


def run():
    equipment = build_equipment_combinations()

    boss = Character(109, 8, 2)
    player_characters = build_characters(equipment)

    for character in player_characters:
        if does_char_win(character[0], boss):
            print("Part 1: " + str(character[1]))
            break

    max_cost_to_lose = 0
    for character in player_characters:
        if not does_char_win(character[0], boss):
            max_cost_to_lose = max(max_cost_to_lose, character[1])
    print("Part 2: " + str(max_cost_to_lose))



def build_equipment_combinations():
    weapons = [Item("Dagger", 8, 4, 0),
               Item("Shortsword", 10, 5, 0),
               Item("Warhammer", 25, 6, 0),
               Item("Longsword", 40, 7, 0),
               Item("Greataxe", 74, 8, 0)]
    armors = [Item("None", 0, 0, 0),
              Item("Leather", 13, 0, 1),
              Item("Chainmail", 31, 0, 2),
              Item("Splintmail", 53, 0, 3),
              Item("Bandedmail", 75, 0, 4),
              Item("Platemail", 102, 0, 5)]
    rings = [Item("None", 0, 0, 0),
             Item("None", 0, 0, 0),
             Item("Damage +1", 25, 1, 0),
             Item("Damage +2", 50, 2, 0),
             Item("Damage +3", 100, 3, 0),
             Item("Defense +1", 20, 0, 1),
             Item("Defense +2", 40, 0, 2),
             Item("Defense +3", 80, 0, 3),
             ]
    equipment = []
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1 == ring2:
                        continue
                    equipment.append([weapon, armor, ring1, ring2])
    return equipment


if __name__ == '__main__':
    run()
