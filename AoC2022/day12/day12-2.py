from pprint import pprint
from queue import PriorityQueue


def run():
    with open('input.txt') as file:
        heights = file.read().splitlines()

    for y in range(0, len(heights)):
        heights[y] = [ord(x) - 97 for x in heights[y]]
    start = (0, 0)
    end = (0, 0)
    for y in range(0, len(heights)):
        for x in range(0, len(heights[y])):
            if heights[y][x] == -14:
                start = (x, y)
                heights[y][x] = 0
            elif heights[y][x] == -28:
                end = (x, y)
                heights[y][x] = 25

    steps = dijkstra(heights, start, end)[end]

    for y in range(0, len(heights)):
        for x in range(0, len(heights[y])):
            if heights[y][x] == 0:
                dijkstra_step_dict = dijkstra(heights, (x, y), end)
                if end in dijkstra_step_dict:
                    steps = min(steps, dijkstra_step_dict[end])

    print(steps)


def dijkstra(grid: list, starting_point: tuple, target: tuple) -> dict:
    frontier = PriorityQueue()
    frontier.put((grid[starting_point[1]][starting_point[0]], starting_point))
    cost = {starting_point: 0}
    steps = {starting_point: 0}
    while not frontier.empty():
        current = frontier.get()
        if current[1] == target:
            break
        for neighbor in get_neighbors(grid, *current[1], grid[current[1][1]][current[1][0]]):
            new_cost = cost[current[1]] + grid[neighbor[1]][neighbor[0]]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                frontier.put((new_cost, neighbor))
                steps[neighbor] = steps[current[1]] + 1
    return steps


def get_neighbors(grid: list, x: int, y: int, current_val) -> list:
    neighbors = []
    if x != 0:
        if grid[y][x - 1] - current_val <= 1:
            neighbors.append((x - 1, y))
    if x < len(grid[0]) - 1:
        if grid[y][x + 1] - current_val <= 1:
            neighbors.append((x + 1, y))
    if y != 0:
        if grid[y - 1][x] - current_val <= 1:
            neighbors.append((x, y - 1))
    if y < len(grid) - 1:
        if grid[y + 1][x] - current_val <= 1:
            neighbors.append((x, y + 1))
    return neighbors


if __name__ == '__main__':
    run()
