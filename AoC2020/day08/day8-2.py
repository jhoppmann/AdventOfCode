with open('input.txt') as file:
    program = file.read().splitlines()


changed = set()
found = False

while not found:
    program_copy = program.copy()
    acc = 0
    next_line = 0
    visited_lines = []
    for i in range(0, len(program)):
        if program_copy[i].startswith('nop'):
            if i not in changed:
                changed.add(i)
                program_copy[i] = program_copy[i].replace('nop', 'jmp')
                break
        if program_copy[i].startswith('jmp'):
            if i not in changed:
                changed.add(i)
                program_copy[i] = program_copy[i].replace('jmp', 'nop')
                break

    while next_line not in visited_lines:
        visited_lines.append(next_line)
        line = program_copy[next_line]
        op = line[:3]
        val = int(line[4:])
        if op == 'acc':
            acc += val
            next_line += 1
        elif op == 'jmp':
            next_line += val
        elif op == 'nop':
            next_line += 1
        if next_line >= len(program):
            print(acc)
            found = True
            break
