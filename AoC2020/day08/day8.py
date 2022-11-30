with open('input.txt') as file:
    program = file.read().splitlines()

acc = 0
next_line = 0
visited_lines = []

while next_line not in visited_lines:
    visited_lines.append(next_line)
    line = program[next_line]
    op = line[:3]
    val = int(line[4:])
    if op == 'acc':
        acc += val
        next_line += 1
    if op == 'jmp':
        next_line += val
    if op == 'nop':
        next_line += 1

print(acc)
