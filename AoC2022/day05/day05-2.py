import re


def run():
    with open('input.txt') as file:
        instructions = file.read().splitlines()

    stacks = []
    stacks.append(list('FTCLRPGQ'))
    stacks.append(list('NQHWRFSJ'))
    stacks.append(list('FBHWPMQ'))
    stacks.append(list('VSTDF'))
    stacks.append(list('QLDWVFZ'))
    stacks.append(list('ZCLS'))
    stacks.append(list('ZBMVDF'))
    stacks.append(list('TJB'))
    stacks.append(list('QNBGLSPH'))

    for i in range(10, len(instructions)):
        instruction = instructions[i]
        numbers = re.findall(r'\d+', instruction)

        crates = stacks[int(numbers[1]) - 1][-int(numbers[0]):]
        stacks[int(numbers[1]) - 1] = stacks[int(numbers[1]) - 1][:-int(numbers[0])]
        stacks[int(numbers[2]) - 1].extend(crates)
    print(calculate_top_row(stacks))


def calculate_top_row(stacks: list) -> str:
    result = ''
    for stack in stacks:
        result += stack[-1]

    return result


if __name__ == '__main__':
    run()
