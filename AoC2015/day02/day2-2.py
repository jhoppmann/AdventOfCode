with open('input.txt') as file:
    input_content = file.readlines()

ribbon = 0
for line in input_content:
    dimensions = [int(x) for x in line.rstrip().split('x')]
    dimensions.sort()
    bow = dimensions[0] * dimensions[1] * dimensions[2]
    ribbon += 2 * dimensions[0] + 2 * dimensions[1] + bow
print(ribbon)
