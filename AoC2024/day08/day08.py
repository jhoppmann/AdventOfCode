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
                antinode1: tuple[int, int] = (antenna[0] + delta[0], antenna[1] + delta[1])
                antinode2 = (current_antenna[0] - delta[0], current_antenna[1] - delta[1])
                if in_bounds(antinode1, signal_map):
                    antinodes_set.add(antinode1)
                if in_bounds(antinode2, signal_map):
                    antinodes_set.add(antinode2)

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


def in_bounds(pos: tuple[int, int], map: list) -> bool:
    # make use of short-circuiting and operator
    return 0 <= pos[1] < len(map) and 0 <= pos[0] < len(map[pos[1]])


if __name__ == '__main__':
    run()
