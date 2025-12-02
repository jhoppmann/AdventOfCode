import math


def run():
    with open('input.txt') as file:
        ranges = file.readline().split(',')
    result_part_one = 0
    result_part_two = 0
    for line in ranges:
        start, end = line.split('-')
        start = int(start)
        end = int(end)
        for i in range(start, end + 1):
            string_value = str(i)
            if check_for_doubles(string_value):
                result_part_one += i
            if check_for_multiples(string_value):
                result_part_two += i

    print('Part 1: ', result_part_one)
    print('Part 2: ', result_part_two)


def check_for_doubles(string_value: str) -> bool:
    """Checks if a string value is the same substring twice"""
    if len(string_value) % 2 == 0:
        half = int(len(string_value) / 2)
        return string_value[0: half] == string_value[half:]
    else:
        return False

def check_for_multiples(string_value: str) -> bool:
    """Checks if a string value is the same substring multiple times"""
    length = len(string_value)
    if length == 1:
        return False
    for sublength in range(1, math.ceil(length / 2) + 1):
        break_now = False
        if length % sublength == 0:
            for part in range(1, math.ceil(length / sublength)):
                if string_value[0:sublength] != string_value[part*sublength:(part+1)*sublength]:
                    break_now = True
                    break
        else:
            continue
        if break_now:
            continue
        return True
    return False


if __name__ == '__main__':
    run()