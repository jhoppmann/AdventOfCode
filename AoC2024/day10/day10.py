def walk_up(x, y, topography_map, visited: set) -> int:
    current_height = topography_map[y][x]
    if current_height == 9 and (x, y) not in visited:
        visited.add((x, y))
        return 1
    score = 0
    for neighbor in get_neighbors(x, y, topography_map):
        if topography_map[neighbor[1]][neighbor[0]] == (current_height + 1):
            score += walk_up(neighbor[0], neighbor[1], topography_map, visited)
    return score


def get_neighbors(x, y, topography_map):
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < (len(topography_map[y]) - 1):
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < (len(topography_map) - 1):
        neighbors.append((x, y + 1))
    return neighbors


def run() -> None:
    with open('input.txt') as file:
        topography_map = file.read().splitlines()

    for i in range(0, len(topography_map)):
        topography_map[i] = [int(x) for x in topography_map[i]]

    trailhead_score_sum = 0
    for y in range(0, len(topography_map)):
        for x in range(0, len(topography_map[y])):
            if topography_map[y][x] == 0:
                visited = set()
                trailhead_score_sum += walk_up(x, y, topography_map, visited)

    print('Part 1:', trailhead_score_sum)


if __name__ == '__main__':
    run()
