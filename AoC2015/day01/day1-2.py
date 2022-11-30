with open('input.txt') as file:
    input_content = file.read()

position = 0
for pos, char in enumerate(input_content, start=1):
    if char == ')':
        position -= 1
    else:
        position += 1
    if position < 0:
        print(pos)
        break