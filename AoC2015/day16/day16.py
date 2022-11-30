def find_sue(values: dict, sues: dict) -> str:
    for sue, known_things in sues.items():
        found_sue = True
        for key in known_things.keys():
            if known_things[key] != values[key]:
                found_sue = False
        if found_sue:
            return sue


def run():
    with open("input.txt") as file:
        input_content = file.read().splitlines()

    values = {'children': 3,
              'cats': 7,
              'samoyeds': 2,
              'pomeranians': 3,
              'akitas': 0,
              'vizslas': 0,
              'goldfish': 5,
              'trees': 3,
              'cars': 2,
              'perfumes': 1}
    sues = {}
    for line in input_content:
        line = line.replace(":", "")
        line = line.replace(",", "")
        split_lines = line.split(" ")
        key = split_lines[1]
        known_things = {}
        for i in range(0, 3):
            known_things[split_lines[2+2*i]] = int(split_lines[3+2*i])
        sues[key] = known_things
    sue = find_sue(values, sues)
    print(sue)


if __name__ == '__main__':
    run()
