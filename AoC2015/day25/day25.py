import re


def find_num_at_position(row, column):
    value = 1
    for i in range(1, row):
        value += i
    for i in range(1, column):
        value += row + i
    return value


def calculate_new_code(old_code: int) -> int:
    new_code = old_code * 252533
    new_code = new_code % 33554393
    return new_code


def run():
    manual_line = "To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083."
    numbers = re.findall(r"\d+", manual_line)
    numbers = [int(x) for x in numbers]
    num_at_position = find_num_at_position(numbers[0], numbers[1])

    code = 20151125
    for i in range(0, num_at_position - 1):
        code = calculate_new_code(code)
    print(code)


if __name__ == '__main__':
    run()
