import re


def run():
    with open('input.txt') as file:
        instructions = file.read()

    expressions = re.findall('don\'t\(\)|do\(\)|mul\(\d+,\d+\)', instructions)
    result_sum = 0
    enabled = True

    for expression in expressions:
        if expression == 'do()':
            enabled = True
        elif expression == 'don\'t()':
            enabled = False
        elif enabled:
            expression = expression[4:-1:]
            factors = expression.split(',')
            result_sum += int(factors[0]) * int(factors[1])

    print(result_sum)


if __name__ == '__main__':
    run()
