import re

with open('input.txt') as file:
    bag_regulations = file.read().splitlines()


def find_children(regulations: list) -> dict:
    colors_with_parents = {}

    for regulation in regulations:
        contents = regulation.split('contain')
        parent = contents[0].replace('bags', '').replace('bag', '').strip()
        for child in contents[1].split(','):
            color = child.replace('bags', '').replace('bag', '').replace('.', '').strip()
            if color != 'no other':
                if parent not in colors_with_parents:
                    colors_with_parents[parent] = []
                colors_with_parents[parent].append(color)

    return colors_with_parents


def count_children(bag_color: str, regulations: dict) -> int:
    size = 1
    if bag_color in regulations:
        for child in regulations[bag_color]:
            child_color = re.sub('\\d+', '', child).strip()
            child_size = int(re.findall('\\d+', child)[0])
            size += child_size * count_children(child_color, regulations)
    return size


color_map = find_children(bag_regulations)
result = count_children('shiny gold', color_map)

print(result - 1)  # remove the shiny gold bag itself
