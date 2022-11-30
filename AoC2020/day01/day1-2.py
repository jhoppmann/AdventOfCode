with open('input.txt') as file:
    input_content = file.readlines()

input_content = [int(line) for line in input_content]

num_1 = 0
num_2 = 0
num_3 = 0

for first in input_content:
    for second in input_content:
        for third in input_content:
            if first + second + third == 2020:
                num_1 = first
                num_2 = second
                num_3 = third
                break

print(num_1 * num_2 * num_3)
