with open('input.txt') as file:
    input_content = file.read()

up = input_content.count('(')
down = input_content.count(')')

print(up - down)