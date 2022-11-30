import re

with open('input.txt') as file:
    bag_regulations = file.read().splitlines()

colors = set()
colors.add('shiny gold')


def map_to_parents(regulations: list) -> dict:
    colors_with_parents = {}

    for regulation in regulations:
        contents = regulation.split('contain')
        parent = contents[0].replace('bags', '').replace('bag', '').strip()
        for child in contents[1].split(','):
            color = re.sub('\\d+', '',child)
            color = color.replace('bags', '').replace('bag', '').replace('.', '').strip()
            if color not in colors_with_parents:
                colors_with_parents[color] = []
            colors_with_parents[color].append(parent)

    return colors_with_parents

map = map_to_parents(bag_regulations)
old_length = 0
while len(colors) != old_length:
    old_length = len(colors)
    parents = set()
    for color in colors:
        if color in map:
            for parent in map[color]:
                parents.add(parent)
    colors = colors.union(parents)

colors.remove('shiny gold')

print(len(colors))