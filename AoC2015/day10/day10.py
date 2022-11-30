puzzle_input = "3113322113"


def compute(value: str, times: int):
    for i in range(0, times):
        last = value[0]
        count = 1
        result = ''
        for i in range(1, len(value)):
            if value[i] == last:
                count += 1
            else:
                result += str(count) + str(last)
                last = value[i]
                count = 1
        result += str(count) + str(last)
        value = result
    return value


print(len(compute(puzzle_input, 40)))  # part one
print(len(compute(puzzle_input, 50)))  # part two
