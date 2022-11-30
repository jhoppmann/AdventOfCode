with open('input.txt') as file:
    input_content = file.read()

visited = set()
visited.add((0, 0))
x = 0
y = 0
for char in input_content[0::2]:
    if char == '>':
        x += 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    visited.add((x, y))

x = 0
y = 0

for char in input_content[1::2]:
    if char == '>':
        x += 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    visited.add((x, y))

print(len(visited))
