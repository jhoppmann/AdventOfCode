import re

with open('input.txt') as file:
    program = file.read().splitlines()

mask = ''
memory = {}


def apply_mask(value) -> str:
    value_as_string = str(bin(value))[2:]
    value_as_string = value_as_string.rjust(36, '0')
    result_string = ''
    for i in range(0, 36):
        if mask[i] != 'X':
            result_string += mask[i]
        else:
            result_string += value_as_string[i]
    return result_string


def save_mem(line) -> None:
    line = line.split(' = ')
    address = int(re.findall('\\d+', line[0])[0])
    value = int(line[1])
    bin_value = apply_mask(value)
    memory[address] = bin_value
    pass


def set_new_mask(line) -> None:
    global mask
    mask = line[6:].strip()


def handle_input(init_program: list) -> None:
    for line in init_program:
        if line.startswith('mask'):
            set_new_mask(line)
        else:
            save_mem(line)


def sum_up_memory() -> int:
    sum_of_values = 0
    for value in memory.values():
        sum_of_values += int(value, 2)
    return sum_of_values


handle_input(program)
result = sum_up_memory()
print(result)
