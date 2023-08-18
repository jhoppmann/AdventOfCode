def get_target_and_size(instruction: list, a: int, b: int) -> (int, int):
    target = 0
    if instruction[1].startswith('a'):
        target = a
    else:
        target = b

    size = int(instruction[2])
    return target, size


def run():
    with open('input.txt') as file:
        instructions = file.read().splitlines()
    a, b = run_program(instructions, 0, 0)
    print("Part 1:", a, b)
    a, b = run_program(instructions, 1, 0)
    print("Part 2:", a, b)


def run_program(instructions: list, a: int, b: int) -> (int, int):
    position = 0
    number_of_instructions = len(instructions)
    while position < number_of_instructions:
        instruction = instructions[position].split(' ')
        if instruction[0] == 'inc':
            if instruction[1] == 'a':
                a += 1
            elif instruction[1] == 'b':
                b += 1
            position += 1
        elif instruction[0] == 'hlf':
            if instruction[1] == 'a':
                a = int(a * 0.5)
            elif instruction[1] == 'b':
                b = int(b * 0.5)
            position += 1
        elif instruction[0] == 'tpl':
            if instruction[1] == 'a':
                a *= 3
            elif instruction[1] == 'b':
                b *= 3
            position += 1
        elif instruction[0] == 'jio':
            target, size = get_target_and_size(instruction, a, b)
            if target == 1:
                position += size
            else:
                position += 1
        elif instruction[0] == 'jie':
            target, size = get_target_and_size(instruction, a, b)
            if target % 2 == 0:
                position += size
            else:
                position += 1
        elif instruction[0] == 'jmp':
            jump_size = int(instruction[1])
            position += jump_size
    return a, b


if __name__ == '__main__':
    run()
