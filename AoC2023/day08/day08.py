from math import lcm


def run():
    with open('input.txt') as file:
        input_data = file.read().splitlines()
    instructions = input_data[0]

    nodes = {}
    for i in range(2, len(input_data)):
        line = input_data[i]
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]
        nodes[node] = (left, right)

    current_node = 'AAA'
    next_instruction = 0
    steps = 0

    while current_node != 'ZZZ':
        instruction = instructions[next_instruction]
        next_instruction = (next_instruction + 1) % len(instructions)
        if instruction == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        steps += 1
    print("Part 1:", steps)

    current_nodes = []
    for node in nodes.keys():
        if node[2] == 'A':
            current_nodes.append(node)
    cycle_lengths = []
    for node in current_nodes:
        next_instruction = 0
        steps = 0
        current_node = node
        while True:
            instruction = instructions[next_instruction % len(instructions)]
            next_instruction = (next_instruction + 1)
            for i in range(0, len(current_nodes)):
                if instruction == "L":
                    current_node = nodes[current_node][0]
                else:
                    current_node = nodes[current_node][1]
            steps += 1
            if current_node[2] == 'Z' and steps > 0 and steps % len(instructions) == 0:
                cycle_lengths.append(steps)
                break
    print("Part 2", lcm(*cycle_lengths))


if __name__ == '__main__':
    run()
