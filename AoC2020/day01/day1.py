with open('input.txt') as file:
    input_content = file.readlines()

input_content = [int(line) for line in input_content]

num_1 = 0
num_2 = 0

for first in input_content:
    for second in input_content:
        if first + second == 2020:
            num_1 = first
            num_2 = second
            break

print(num_1 * num_2)
