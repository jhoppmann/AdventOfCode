import re

with open('input.txt') as file:
    program = file.read().splitlines()

mask = ''
memory = {}


def replace_with(param, address: str):
    result_list = []
    if 'X' not in address:
        result_list.append(address)
    else:
        for i in range(0, len(address)):
            if address[i] == 'X':
                prefix = address[0:i]
                zeroes = replace_with(0, address[i+1:])
                for line in zeroes:
                    result_list.append(prefix + str(param) + line)
                ones = replace_with(1, address[i + 1:])
                for line in ones:
                    result_list.append(prefix + str(param) + line)
                break
    return result_list


def find_variants(address: str) -> list:
    result_list = []
    if 'X' in address:
        result_list += replace_with(0, address)
        result_list += replace_with(1, address)
    else:
        result_list.append(address)
    result_list = set(result_list)
    return result_list


def apply_mask(value: int) -> list:
    addresses = []
    addressresult = ''
    value = str(bin(value))[2:].rjust(36, '0')
    for i in range(1, len(value) + 1):
        if mask[-i] == 'X':
            addressresult = 'X' + addressresult
        elif mask[-i] == '0':
            addressresult = value[-i] + addressresult
        else:
            addressresult = '1' + addressresult
    addresses += find_variants(addressresult)
    return addresses


def save_mem(line) -> None:
    line = line.split(' = ')
    address_value = int(re.findall('\\d+', line[0])[0])
    value = line[1]
    addresses = apply_mask(address_value)
    for address in addresses:
        memory[int(address, 2)] = int(value)
        pass


def set_new_mask(line) -> None:
    global mask
    mask = line[5:].strip()


def handle_input(init_program: list) -> None:
    for line in init_program:
        if line.startswith('mask'):
            set_new_mask(line)
        else:
            save_mem(line)


def sum_up_memory() -> int:
    return memory.values()


handle_input(program)
result = sum_up_memory()
print(result)
