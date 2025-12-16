def run():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    devices = {}

    # Part 1
    starting_device = 'you'
    for line in lines:
        device, connected = line.split(': ')
        devices[device] = [x for x in connected.split(' ')]
    num_paths = calc_num_paths(starting_device, devices)
    print('Part 1:', num_paths)

def calc_num_paths(node, devices) -> int:
    if node == 'out':
        return 1
    else:
        children = devices[node]
        paths = 0
        for child in children:
            paths += calc_num_paths(child, devices)
        return paths

def calc_paths(node, devices, current_path, paths) -> None:
    if node == 'out':
        paths.append(current_path)
    else:
        children = devices[node]
        for child in children:
            path = current_path.copy()
            path.append(child)
            calc_paths(child, devices, path, paths)



if __name__ == '__main__':
    run()