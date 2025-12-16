def run():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    coordinates = [(int(x[0]), int(x[1])) for x in (l.split(',') for l in lines)]

    rectangles = calculate_sizes(coordinates)
    ordered_rectangles = sorted(rectangles, key=lambda x: x[2], reverse=True)
    print('Part 1:', ordered_rectangles[0][2])

def calculate_sizes(coordinates: list) -> set:
    rectangles = set()
    for point1 in coordinates:
        for point2 in coordinates:
            if point1 != point2:
                size = abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)
                rectangles.add((min(point1, point2), max(point1, point2), size))

    return rectangles


if __name__ == '__main__':
    run()