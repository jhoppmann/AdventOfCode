def check_cycle(cycle: int, x: int) -> int:
    if (cycle - 20) % 40 == 0:
        print(cycle)
        return cycle * x
    return 0


def run():
    with open('input.txt') as file:
        commands = file.read().splitlines()

    x = 1  # register x
    cycle = 0
    signal_strength_sum = 0

    for command in commands:
        if command == 'noop':
            cycle += 1
            signal_strength_sum += check_cycle(cycle, x)
        else:
            command = command[5:]
            value = int(command)
            cycle += 1
            signal_strength_sum += check_cycle(cycle, x)
            cycle += 1
            signal_strength_sum += check_cycle(cycle, x)
            x += value

    print(signal_strength_sum)


if __name__ == '__main__':
    run()
