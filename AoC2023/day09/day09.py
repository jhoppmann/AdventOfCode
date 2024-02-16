def calculate_differences(sequence: list) -> list:
    differences = []
    for i in range(0, len(sequence) - 1):
        differences.append(sequence[i + 1] - sequence[i])
    return differences


def calculate_next_element(sequence: list) -> int:
    differences = calculate_differences(sequence)
    if differences.count('0') == len(differences):
        return 0
    return sequence[-1] + calculate_next_element(differences)


def calculate_previous_element(sequence: list) -> int:
    differences = calculate_differences(sequence)
    if differences.count('0') == len(differences):
        return 0
    return sequence[0] - calculate_previous_element(differences)


def run():
    with open('input.txt') as file:
        histories = file.read().splitlines()

    value_aggregate_next = 0
    value_aggregate_prev = 0
    for history in histories:
        history_entries = history.split(' ')
        history_entries = [int(x) for x in history_entries]
        value_aggregate_next += calculate_next_element(history_entries)
        value_aggregate_prev += calculate_previous_element(history_entries)
    print('Part 1:', value_aggregate_next)
    print('Part 2:', value_aggregate_prev)


if __name__ == '__main__':
    run()
