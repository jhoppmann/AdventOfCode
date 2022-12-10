def pixel_for_cycle(cycle: int, x: int, screen: dict):
    row = int(cycle / 40)
    position = (cycle % 40)

    if abs(x - position) <= 1:
        screen[row].append('#')
    else:
        screen[row].append('.')


def run():
    with open('input.txt') as file:
        commands = file.read().splitlines()

    x = 1  # register x
    cycle = 0
    screen = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for command in commands:
        if command == 'noop':
            pixel_for_cycle(cycle, x, screen)
            cycle += 1
        else:
            command = command[5:]
            value = int(command)
            pixel_for_cycle(cycle, x, screen)
            cycle += 1
            pixel_for_cycle(cycle, x, screen)
            cycle += 1
            x += value

    for i in range(0, 6):
        print(' '.join(screen[i]))


if __name__ == '__main__':
    run()
