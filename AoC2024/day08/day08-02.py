import math


def run() -> None:
    with open('input.txt') as file:
        signal_map = file.read().splitlines()

    signal_coords = parse_antenna_coords(signal_map)

    antinodes_set = set()
    for (signal, antennas) in signal_coords.items():
        for i in range(0, len(antennas) - 1):
            current_antenna = antennas[i]
            for antenna in antennas[i + 1::]:
                delta = (antenna[0] - current_antenna[0], antenna[1] - current_antenna[1])
                delta_step_divisor = math.gcd(delta[0], delta[1])
                delta = (int(delta[0] / delta_step_divisor), int(delta[1] / delta_step_divisor))
                i = 0
                while in_bounds(current_antenna[0] - i * delta[0], current_antenna[1] - i * delta[1], signal_map):
                    antinodes_set.add((current_antenna[0] - i * delta[0], current_antenna[1] - i * delta[1]))
                    i += 1
                i = 0
                while in_bounds(current_antenna[0] + i * delta[0], current_antenna[1] + i * delta[1], signal_map):
                    antinodes_set.add((current_antenna[0] + i * delta[0], current_antenna[1] + i * delta[1]))
                    i += 1

    print(len(antinodes_set))


def parse_antenna_coords(signal_map):
    signal_coords = {}
    for y in range(0, len(signal_map)):
        for x in range(0, len(signal_map[y])):
            current = signal_map[y][x]
            if current != '.':
                if current in signal_coords:
                    signal_coords[current].append((x, y))
                else:
                    signal_coords[current] = [(x, y)]
    return signal_coords


def in_bounds(x: int, y: int, map: list) -> bool:
    # make use of short-circuiting and operator
    return 0 <= y < len(map) and 0 <= x < len(map[y])


if __name__ == '__main__':
    run()
