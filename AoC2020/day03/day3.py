with open('input.txt') as file:
    wood = file.read().splitlines()

line_length = len(wood[0])

x = 0  # raising this means "go right"
y = 0  # raising this means "go down"

trees = 0
while y < len(wood):
    if wood[y][x % line_length] == '#':
        trees += 1
    x += 3
    y += 1
print(trees)
