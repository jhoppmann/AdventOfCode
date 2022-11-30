import math
import sys

with open('testinput.txt') as file:
    notes = file.read().splitlines()

current_min = int(notes[0])


bus_table = [x for x in notes[1].split(',')]
busses = []
offsets = []
busses_and_offsets = {}
for i in range(len(bus_table)):
    if bus_table[i].isnumeric():
        busses_and_offsets[int(bus_table[i])] = i
        busses.append(int(bus_table[i]))


for bus in busses:
    offsets.append(busses_and_offsets[bus])

def find_for_busses_and_offsets(busses:list, offsets:list) -> int:
    timestamp = 1
    for j in range(0, len(busses)):
        offset = offsets[j]
        bus = busses[j]
        multiplier = 1
        while multiplier <= sys.maxsize:
            if (multiplier * timestamp + offset) % bus == 0:
                timestamp *= multiplier
                print("bus " + str(bus), str(timestamp))
                break
            multiplier += 1
    return timestamp

print(offsets, busses)
result = find_for_busses_and_offsets(busses, offsets)
print(result)
