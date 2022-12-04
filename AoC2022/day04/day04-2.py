def run():
    with open('input.txt') as file:
        assignments = file.read().splitlines()

    overlaps = 0
    for pair in assignments:
        split_pair = pair.split(",")
        elfs = []
        split_pair[0] = split_pair[0].split("-")
        split_pair[1] = split_pair[1].split("-")
        elfs.append((int(split_pair[0][0]), int(split_pair[0][1])))
        elfs.append((int(split_pair[1][0]), int(split_pair[1][1])))

        elf_one_range = {*range(elfs[0][0], elfs[0][1] + 1, 1)}
        elf_two_range = {*range(elfs[1][0], elfs[1][1] + 1, 1)}
        overlapping_fields = elf_one_range.intersection(elf_two_range)

        if overlapping_fields:
            overlaps += 1

    print(overlaps)


if __name__ == '__main__':
    run()
