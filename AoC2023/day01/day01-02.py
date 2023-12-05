from typing import Any

import re


def run():
    with open('input.txt') as file:
        config_lines: list = file.read().splitlines()

    running_total: int = 0

    for config_line in config_lines:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', config_line)
        running_total += int(str(string_to_value(digits[0])) + str(string_to_value(digits[-1])))

    print(running_total)


def string_to_value(number_string: str) -> int:
    if number_string.isnumeric():
        return int(number_string)
    elif number_string == 'one':
        return 1
    elif number_string == 'two':
        return 2
    elif number_string == 'three':
        return 3
    elif number_string == 'four':
        return 4
    elif number_string == 'five':
        return 5
    elif number_string == 'six':
        return 6
    elif number_string == 'seven':
        return 7
    elif number_string == 'eight':
        return 8
    elif number_string == 'nine':
        return 9


if __name__ == '__main__':
    run()
