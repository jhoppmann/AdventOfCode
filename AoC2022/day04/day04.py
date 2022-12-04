def run():
    with open('input.txt') as file:
        assignments = file.read().splitlines()

    inclusions = 0
    for pair in assignments:
        split_pair = pair.split(",")
        elfs = []
        split_pair[0] = split_pair[0].split("-")
        split_pair[1] = split_pair[1].split("-")
        elfs.append((int(split_pair[0][0]), int(split_pair[0][1])))
        elfs.append((int(split_pair[1][0]), int(split_pair[1][1])))

        if elfs[0][0] <= elfs[1][0] and elfs[0][1] >= elfs[1][1]:
            inclusions += 1
        elif elfs[0][0] >= elfs[1][0] and elfs[0][1] <= elfs[1][1]:
            inclusions += 1

    print(inclusions)


if __name__ == '__main__':
    run()
