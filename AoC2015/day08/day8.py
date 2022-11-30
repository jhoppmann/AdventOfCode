with open('input.txt') as file:
    input_content = file.read().splitlines()

sum_literals = 0
sum_chars = 0
for line in input_content:
    sum_literals += len(line)
    sum_chars += len(eval(line))

print(sum_literals, sum_chars, sum_literals - sum_chars)
