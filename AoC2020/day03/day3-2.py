with open('input.txt') as file:
    wood = file.read().splitlines()

line_length = len(wood[0])

movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = []
for x_inc, y_inc in movements:
    trees_on_route = 0
    x = 0  # raising this means 'go right'
    y = 0  # raising this means 'go down'
    while y < len(wood):
        if wood[y][x % line_length] == '#':
            trees_on_route += 1
        x += x_inc
        y += y_inc
    trees.append(trees_on_route)
result = 1
for tree_number in trees:
    result *= tree_number

print(result)
