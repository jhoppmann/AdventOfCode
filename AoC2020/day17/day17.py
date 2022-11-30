from pprint import pprint

with open('input.txt') as file:
    input_text = file.read().splitlines()


def pad(volume: dict) -> list:
    global padding
    padding += 1
    for z, layer in volume.items():
        for i in range(0, len(layer)):
            layer[i] = '.' + layer[i] + '.'
        layer.append('.' * len(layer[0]))
        layer.insert(0, '.' * len(layer[0]))
    x = len(volume[0][0])
    y = len(volume[0])
    new_layer = []
    for i in range(0, y):
        new_layer.append(x*'.')
    volume[0-padding] = new_layer.copy()
    volume[padding] = new_layer.copy()
    return volume


def calculate(x: int, y: int, z: int, current_volume: dict) -> str:
    active_neighbors = 0
    is_active = False
    for z_shift in range(-1, 2):
        for y_shift in range(-1, 2):
            for x_shift in range(-1, 2):
                if x_shift == 0 and y_shift == 0 and z_shift == 0:
                    is_active = current_volume[z][y][x] == '#'
                else:
                    if current_volume[z + z_shift][y+y_shift][x+x_shift] == '#':
                        active_neighbors += 1

    if is_active and 2 <= active_neighbors <= 3:
        return '#'
    if not is_active and active_neighbors == 3:
        return '#'

    return '.'


def cycle(volume: dict) -> dict:
    volume = pad(volume)
    new_volume = {}
    for z, layer in volume.items():
        if abs(z) == padding:
            new_volume[z] = volume[z].copy()
        else:
            new_layer = [layer[0]]
            for y in range(1, len(layer) - 1):
                new_x_row = '.'
                for x in range(1, len(layer[0])-1):
                    new_x_row += calculate(x, y, z, volume)
                new_x_row += '.'
                new_layer.append(new_x_row)
            new_layer.append(layer[0])
            new_volume[z] = new_layer
    return new_volume


def count_active(volume: dict) -> int:
    actives = 0
    for layer in volume.values():
        for row in layer:
            actives += row.count('#')
    return actives


cycles = 6
padding = 0

layer = [x for x in input_text]
volume = {0: layer}

volume = pad(volume)  # initial padding for size after first cycle
for i in range(0, cycles):
    volume = cycle(volume)

print(count_active(volume))



