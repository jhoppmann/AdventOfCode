with open('input.txt') as file:
    instruction_list = file.readlines()
instruction_list = [x.strip() for x in instruction_list]

value_by_instruction = {}
values = {}
for line in instruction_list:
    (v, k) = line.split("->")
    value_by_instruction[k.strip()] = v.strip()
value_by_instruction['b'] = '46065'

def sb_bin_string(val: int) -> str:
    val = str(bin(val))[2:]
    return val.rjust(16, '0')


def b_or(val1: str, val2: str) -> str:
    result = ""
    for i in range(0, len(val1)):
        if val1[i] == '1' or val2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result


def b_and(val1: str, val2: str) -> str:
    result = ""
    for i in range(0, len(val1)):
        if val1[i] == '1' and val2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result


def b_not(val1: str) -> str:
    result = ""
    for i in range(0, len(val1)):
        if val1[i] == '0':
            result += '1'
        else:
            result += '0'
    return result


def unary(splits):
    op = splits[0]
    val = splits[1]
    if op == 'NOT':
        return b_not(values[val])
    raise ValueError(op)


def b_rshift(val, places):
    result = val
    for i in range(0, places):
        result = '0' + result[:-1]
    return result


def b_lshift(val, places):
    result = val
    for i in range(0, places):
        result = result[1:] + '0'
    return result


def binary(splits):
    val1 = sb_bin_string(int(splits[0])) if splits[0].isnumeric() else values[splits[0]]
    val2 = sb_bin_string(int(splits[2])) if splits[2].isnumeric() else values[splits[2]]
    operator = splits[1]
    if operator == 'AND':
        return b_and(val1, val2)
    elif operator == 'OR':
        return b_or(val1, val2)
    elif operator == 'RSHIFT':
        return b_rshift(val1, int(val2, 2))
    elif operator == 'LSHIFT':
        return b_lshift(val1, int(val2, 2))
    raise ValueError(operator)


def evaluate():
    global value_by_instruction
    while value_by_instruction:
        new_dict = {}
        for k, v in value_by_instruction.items():
            splits = v.split()
            if len(splits) == 1:
                if splits[0].isnumeric():
                    values[k] = sb_bin_string(int(v))
                elif splits[0] in values.keys():
                    values[k] = values[splits[0]]
                else:
                    new_dict[k] = v
            elif len(splits) == 2:
                if splits[1] in values.keys():
                    values[k] = unary(splits)
                else:
                    new_dict[k] = v
            elif len(splits) == 3:
                if (splits[0].isnumeric() or splits[0] in values.keys()) and (
                        splits[2].isnumeric() or splits[2] in values.keys()):
                    values[k] = binary(splits)
                else:
                    new_dict[k] = v
        value_by_instruction = new_dict
    print(values)



evaluate()
result_dict = {k: int(v, 2) for k, v in values.items()}
print(result_dict)
