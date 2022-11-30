with open('input.txt') as file:
    input_content = file.readlines()

material = 0
for line in input_content:
    dimensions = [int(x) for x in line.rstrip().split('x')]
    side1 = dimensions[0] * dimensions[1]
    side2 = dimensions[1] * dimensions[2]
    side3 = dimensions[0] * dimensions[2]
    extra = min(side1, side2, side3)
    material += 2*side1+2*side2+2*side3+extra

print(material)
