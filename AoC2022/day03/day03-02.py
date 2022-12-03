def run():
    with open('input.txt') as file:
        packing_list = file.read().splitlines()

    priorities = 0
    i = 0
    while i < len(packing_list):
        elfs = (packing_list[i], packing_list[i+1], packing_list[i+2])
        intersection_one = set(elfs[0]).intersection(set(elfs[1]))
        intersection_two = intersection_one.intersection(set(elfs[2]))
        item = str(list(intersection_two)[0])
        if item.islower():
            priorities += ord(item) - 96
        else:
            priorities += ord(item) - 38
        i += 3
    print(priorities)


if __name__ == '__main__':
    run()
