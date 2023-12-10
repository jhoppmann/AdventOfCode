import re


def run():
    with open('input.txt') as file:
        config_lines: list = file.read().splitlines()

    running_total: int = 0

    for config_line in config_lines:
        digits = re.findall(r'\d', config_line)
        running_total += int(digits[0] + digits[-1])
    print(running_total)


if __name__ == '__main__':
    run()
