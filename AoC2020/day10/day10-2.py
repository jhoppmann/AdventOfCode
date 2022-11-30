with open('input.txt') as file:
    joltage = [int(x) for x in file.read().splitlines()]

joltage.sort()

memoization = {}


def find_ways(position: int) -> int:
    if position < len(joltage) - 1:
        result = 0
        i = position + 1
        while i < len(joltage) and joltage[i] - joltage[position] <= 3:
            if i not in memoization:
                variations = find_ways(i)
                memoization[i] = variations
            result += memoization[i]
            i += 1
        return result
    else:
        return 1


answer = 0
pos = 0
while joltage[pos] <= 3:
    answer += find_ways(pos)
    pos += 1
print(answer)
