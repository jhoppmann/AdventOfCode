from File import Dir, File


def run():
    with open('input.txt') as file:
        input_data = file.read().splitlines()
    space = 70_000_000

    topDir = Dir('/', None)
    currentDir = topDir
    for line in input_data[1:]:
        if line.startswith('$'):
            parts = line.split(' ')
            if parts[1] == 'cd':
                if parts[2] == '..':
                    currentDir = currentDir.parent
                else:
                    currentDir = currentDir.children[parts[2]]
        elif line.startswith('dir'):
            name = line.split(' ')[1]
            currentDir.add_child(Dir(name, currentDir))
        else:
            size, name = line.split(' ')
            size = int(size)
            currentDir.add_child(File(name, size, currentDir))

    sizes = []
    used_space = calculate_size(topDir, sizes, )
    unsed_space = space - used_space
    to_clean = 30_000_000 - unsed_space
    dir_size = max(sizes)
    for size in sizes:
        if size >= to_clean:
            dir_size = min(dir_size, size)
    print('Part 1:', sum([x for x in sizes if x <= 100_000]))
    print('Part 2:', dir_size)


def calculate_size(directory: Dir, sizes: list) -> int:
    size = 0
    for key, value in directory.children.items():
        if isinstance(value, File):
            size += value.size
        else:
            size += calculate_size(value, sizes)
    sizes.append(size)
    return size


if __name__ == '__main__':
    run()
