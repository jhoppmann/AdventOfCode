import sys
from itertools import permutations

with open('input.txt') as file:
    input_content = file.read().splitlines()

distances = {}
destinations = set()
for line in input_content:
    split = line.split(' ')
    distances[(split[0], split[2])] = int(split[4])
    destinations.add(split[0])
    destinations.add(split[2])

routes = list(permutations(destinations))

minimum = sys.maxsize

for route in routes:
    length = 0
    location = 0
    while location <= len(route) - 2:
        dirOne = (route[location], route[location+1])
        dirTwo = (route[location+1], route[location])
        if dirOne in distances:
            length += distances[dirOne]
        elif dirTwo in distances:
            length += distances[dirTwo]
        location += 1
    if length <= minimum:
        minimum = length

print(minimum)

