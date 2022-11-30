with open('input.txt') as file:
    state = file.read().splitlines()

new_state = []


def count_occupied(i: int, j: int) -> int:
    count = 0
    # go up
    x, y = i - 1, j
    while x >= 0 and state[x][y] == '.':
        x -= 1
    if x >= 0 and state[x][y] == '#':
        count += 1
    # go down
    x, y = i + 1, j
    while x < len(state) - 1 and state[x][y] == '.':
        x += 1
    if x < len(state) and state[x][y] == '#':
        count += 1
    # go left
    x, y = i, j-1
    while y >= 0 and state[x][y] == '.':
        y -= 1
    if y >= 0 and state[x][y] == '#':
        count += 1
    # go right
    x, y = i, j + 1
    while y < len(state[x]) - 1 and state[x][y] == '.':
        y += 1
    if y < len(state[x]) and state[x][y] == '#':
        count += 1
    # go diagonal up / left
    x, y = i - 1, j - 1
    while x >= 0 and y >= 0 and state[x][y] == '.':
        x -= 1
        y -= 1
    if x >= 0 and y >= 0 and state[x][y] == '#':
        count += 1
    # go diagonal down / right
    x, y = i + 1, j + 1
    while x < len(state) - 1 and y < len(state[x]) - 1 and state[x][y] == '.':
        x += 1
        y += 1
    if x < len(state) and y < len(state[x]) and state[x][y] == '#':
        count += 1
    # go diagonal up / right
    x, y = i - 1, j + 1
    while x >= 0 and y < len(state[x]) - 1 and state[x][y] == '.':
        x -= 1
        y += 1
    if x >= 0 and y < len(state[x]) and state[x][y] == '#':
        count += 1
    # go diagonal down / left
    x, y = i + 1, j - 1
    while x < len(state) - 1 and y >= 0 and state[x][y] == '.':
        x += 1
        y -= 1
    if x < len(state) and y >= 0 and state[x][y] == '#':
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
                if count_occupied(i, j) >= 5:
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
