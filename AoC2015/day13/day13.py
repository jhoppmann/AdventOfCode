import itertools


def run():
    with open('input.txt') as file:
        input_content = file.read().splitlines()

    seating_happiness = method_name(input_content)

    print(calculate_permutation_values(seating_happiness))



def method_name(input_content):
    seating_happiness = {}
    for line in input_content:
        split_line = line.split(" ")
        value = int(split_line[3])
        if split_line[2] == 'lose':
            value *= -1
        who = split_line[0]
        next_to = split_line[10][0:-1]
        if who not in seating_happiness:
            seating_happiness[who] = {}
        seating_happiness[who][next_to] = value
    return seating_happiness


def determine_value(perm, seating_happiness):
    value = 0
    for i in range(0, len(perm)):
        if i + 1 <= len(perm) - 1:
            value += seating_happiness[perm[i]][perm[i+1]]
            value += seating_happiness[perm[i+1]][perm[i]]
        else:
            value += seating_happiness[perm[-1]][perm[0]]
            value += seating_happiness[perm[0]][perm[-1]]
    print(perm, value)
    return value


def calculate_permutation_values(seating_happiness):
    participants = [list(seating_happiness.keys())[0]]
    participants.extend(list(seating_happiness[participants[0]].keys()))
    list(itertools.permutations(participants))
    permutations = [x for x in list(itertools.permutations(participants)) if x[0] == participants[0]]
    print(len(permutations))
    highest_value = 0
    for perm in permutations:
        highest_value = max(highest_value, determine_value(perm, seating_happiness))
    return highest_value


if __name__ == '__main__':
    run()
