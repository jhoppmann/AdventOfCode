def run() -> None:
    with open('input.txt') as file:
        calibration_equations = file.read().splitlines()

    result_sum_p1 = 0
    result_sum_p2 = 0
    operators_part1 = ['*', '+']
    operators_part2 = ['*', '+', '||']
    for line in calibration_equations:
        solution, operands = line.split(": ")
        operands = [int(x) for x in operands.split(' ')]
        solution = int(solution)
        if solution in evaluate(operands, operators_part1, 0):
            result_sum_p1 += solution
        if solution in evaluate(operands, operators_part2, 0):
            result_sum_p2 += solution

    print('Part 1:', result_sum_p1)
    print('Part 2:', result_sum_p2)


def evaluate(operands: list, operators: list, total: int) -> list:
    result = []
    if len(operands) == 1:
        result = [total * operands[0], total + operands[0]]
        if '||' in operators:
            result.append(int(str(total) + str(operands[0])))
        return result
    else:
        for operator in operators:
            if operator == '*':
                result.extend(evaluate(operands[1::], operators, total * operands[0]))
            elif operator == '+':
                result.extend(evaluate(operands[1::], operators, total + operands[0]))
            elif operator == '||':
                new_total = int(str(total) + str(operands[0]))
                result.extend(evaluate(operands[1::], operators, new_total))
        return result


if __name__ == '__main__':
    run()
