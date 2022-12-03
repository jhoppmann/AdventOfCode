def run():
    with open('input.txt') as file:
        packing_list = file.read().splitlines()

    priorities = 0
    for rucksack in packing_list:
        item_count = int(len(rucksack) / 2)
        compartment_one = set(rucksack[0:item_count])
        compartment_two = set(rucksack[item_count:])
        item = str(list(compartment_one.intersection(compartment_two))[0])
        if item.islower():
            priorities += ord(item) - 96
        else:
            priorities += ord(item) - 38
    print(priorities)


if __name__ == '__main__':
    run()
