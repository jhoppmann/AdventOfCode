with open('input.txt') as file:
    state = file.read().splitlines()

new_state = []


def count_occupied(i: int, j: int) -> int:
    count = 0
    if i != 0 and state[i - 1][j] == '#':
        count += 1
    if i < len(state) - 1 and state[i + 1][j] == '#':
        count += 1
    if i < len(state) - 1 and j < len(state[i]) - 1 and state[i + 1][j + 1] == '#':
        count += 1
    if i < len(state) - 1 and j != 0 and state[i + 1][j - 1] == '#':
        count += 1
    if j != 0 and state[i][j - 1] == '#':
        count += 1
    if j < len(state[i]) - 1 and state[i][j + 1] == '#':
        count += 1
    if i != 0 and j != 0 and state[i - 1][j - 1] == '#':
        count += 1
    if i != 0 and j < len(state[i]) - 1 and state[i - 1][j + 1] == '#':
        count += 1
    return count


def calculate_new_state():
    for i in range(0, len(state)):
        new_line = ''
        for j in range(0, len(state[0])):
            if state[i][j] == '.':
                new_line += '.'
            if state[i][j] == 'L':
                if count_occupied(i, j) == 0:
                    new_line += '#'
                else:
                    new_line += 'L'
            if state[i][j] == '#':
                if count_occupied(i, j) >= 4:
                    new_line += 'L'
                else:
                    new_line += '#'
        new_state.append(new_line)


def calculate_occupied_in_state(state: list) -> int:
    result = 0
    for line in state:
        result += line.count('#')
    return result


def compare_states(state: list, new_state: list) -> bool:
    equal = True
    if len(state) != len(new_state):
        return False
    for i in range(0, len(state)):
        if state[i] != new_state[i]:
            return False
    return equal


while True:
    calculate_new_state()
    if compare_states(new_state, state):
        print(calculate_occupied_in_state(new_state))
        break
    else:
        state = new_state
        new_state = []
