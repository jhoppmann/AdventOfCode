with open('input.txt') as file:
    input_content = file.read().splitlines()

sum_literals = 0
sum_encoded = 0
for line in input_content:
    sum_literals += len(line)
    sum_encoded += len(repr(line).replace('"', '\\"'))

print(sum_literals, sum_encoded, sum_encoded - sum_literals)
