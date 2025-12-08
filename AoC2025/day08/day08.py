from math import sqrt


def run():
    with open('input.txt') as file:
        lines = file.read().splitlines()

    points = [(int(x[0]), int(x[1]), int(x[2])) for x in (l.split(',') for l in lines)]

    distances = calc_distances(points)
    sorted_distances = sorted(distances, key=lambda x: x[2])

    circuits = []
    last_point1 = None
    last_point2 = None
    for i in range(len(sorted_distances)):
        if i == 1000:
            circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
            top_three_size_product = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
            print('Part 1:', top_three_size_product)
        point1, point2, d = sorted_distances[i]
        circ1 = find_circuit(point1, circuits)
        circ2 = find_circuit(point2, circuits)
        if circ1 != circ2:
            if circ1 in circuits: circuits.remove(circ1)
            if circ2 in circuits: circuits.remove(circ2)
            circ1.extend(circ2)
            circuits.append(circ1)
        last_point1 = point1
        last_point2 = point2
        if len(circuits[0]) == len(points):
            break
    print('Part 2:', last_point1[0] * last_point2[0])


def calc_distances(points: list) -> set:
    distances = set()
    for point1 in points:
        for point2 in points:
            if point1 != point2:
                d = sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2 )
                distances.add((min(point1, point2), max(point1, point2), d))
    return distances


def find_circuit(point, circuits) -> list:
    for circuit in circuits:
        if point in circuit:
            return circuit
    return [point]


if __name__ == '__main__':
    run()