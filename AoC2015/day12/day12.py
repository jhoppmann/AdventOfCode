import re

with open('input.txt') as file:
    input_content = file.read().splitlines()

json_string = input_content[0]

numbers = [int(x) for x in re.findall('-?\\d+', json_string)]

print(sum(numbers))

