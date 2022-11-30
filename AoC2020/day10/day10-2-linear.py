import math

with open('input.txt') as file:
    joltage = [int(x) for x in file.read().splitlines()]

joltage.append(0)
joltage.append(max(joltage) + 3)
joltage.sort()

print(joltage)


def find_variants(joltages: list) -> int:
    result = 1
    i = 0
    while i < len(joltages) - 1:
        block_size = 1
        while joltage[i + 1] - joltage[i] == 1:
            block_size += 1
            i += 1
        if block_size in (3, 4):
            result *= math.pow(2, block_size-2)
        if block_size == 5:
            result *= 7
        i += 1
    return int(result)


answer = find_variants(joltage)
print(answer)
