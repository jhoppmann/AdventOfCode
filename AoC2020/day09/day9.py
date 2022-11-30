with open('input.txt') as file:
    cyphers_as_string = file.read().splitlines()


def find_pair(preamble, current_cypher, position):
    pair_found = False
    for i in range(position - preamble, position):
        if pair_found:
            break
        for j in range(position - preamble, position):
            if cyphers[i] + cyphers[j] == current_cypher:
                pair_found = True
                break

    return pair_found


cyphers = [int(x) for x in cyphers_as_string]

preamble_size = 25

for i in range(preamble_size, len(cyphers)):
    if not find_pair(preamble_size, cyphers[i], i):
        print(cyphers[i])
        break
