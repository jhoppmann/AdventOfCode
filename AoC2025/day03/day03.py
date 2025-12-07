def run():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    batteries = []
    for line in lines:
        batteries.append([x for x in line])
    part_one = 0

    for joltages in batteries:
        max_value = max(joltages)
        max_val_index = joltages.index(max_value)
        if max_val_index == len(joltages) - 1:
            first = max(joltages[:-1:])
            part_one += int(str(first) + str(max_value))
        else:
            second = max(joltages[max_val_index + 1:])
            part_one += int(str(max_value) + str(second))

    print('Part 1: ', part_one)


if __name__ == '__main__':
    run()
