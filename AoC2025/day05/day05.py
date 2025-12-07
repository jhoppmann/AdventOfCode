def run():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    id_ranges = []
    ids = []
    fresh_ingredients = 0
    for line in lines:
        if '-' in line:
            lower = int(line.split('-')[0])
            upper = int(line.split('-')[1])
            id_ranges.append((lower, upper))
        elif line:
            ids.append(int(line))
    id_ranges = merge_intervals(id_ranges)

    # Part 1
    for id in ids:
        for lower, upper in id_ranges:
            if lower <= id <= upper:
                fresh_ingredients += 1
                break

    # Part 2
    fresh_ingredient_id_num = 0
    for id_range in id_ranges:
        fresh_ingredient_id_num += id_range[1] - id_range[0] + 1

    print("Part 1:", fresh_ingredients)
    print("Part 2:", fresh_ingredient_id_num)


def merge_intervals(id_ranges: list[list]) -> list:
    id_ranges.sort()
    merged = []
    lower: int
    upper: int

    for lower, upper in id_ranges:
        if not merged:
            merged.append([lower, upper])
            continue

        last_lower, last_upper = merged[-1]
        if lower <= last_upper:
            merged[-1][1] = max(last_upper, upper)
        else:
            merged.append([lower, upper])
    return merged


if __name__ == '__main__':
    run()
