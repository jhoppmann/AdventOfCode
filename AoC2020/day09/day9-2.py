with open('input.txt') as file:
    cyphers_as_string = file.read().splitlines()

cyphers = [int(x) for x in cyphers_as_string]

first_part_output = 20874512

for i in range(0, len(cyphers)):
    result = cyphers[i]
    first = cyphers[i]
    for j in range(i+1, len(cyphers)):
        result += cyphers[j]
        if result == first_part_output:
            print(cyphers[i] + cyphers[j])
        if result > first_part_output:
            break
