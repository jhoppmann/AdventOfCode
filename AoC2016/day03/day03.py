import copy
import re

def run():
    with open('input.txt') as file:
        triangles = file.read().splitlines()

    triangles = [[int(x) for x in re.findall('\\d+', y)] for y in triangles]

    valid_triangles_part_one = 0

    triangles_part_one = copy.deepcopy(triangles)
    for triangle in triangles_part_one:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            valid_triangles_part_one += 1

    print("Part 1:", valid_triangles_part_one)

    current_line = 0
    actual_triangles = []

    while current_line < len(triangles):
        for i in range(0, 3):
            actual_triangles.append([triangles[current_line][i], triangles[current_line + 1][i], triangles[current_line
                                                                                                           + 2][i]])
        current_line += 3

    valid_triangles_part_two = 0
    for triangle in actual_triangles:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            valid_triangles_part_two += 1

    print("Part 2:", valid_triangles_part_two)


if __name__ == '__main__':
    run()