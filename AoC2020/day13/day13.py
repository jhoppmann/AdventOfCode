with open('input.txt') as file:
    notes = file.read().splitlines()

current_min = int(notes[0])

busses = [int(x) for x in notes[1].split(',') if x.isnumeric()]
minimal_time_diff = max(busses) + 1

print(current_min, busses)
bus_to_take = 0

for bus in busses:
    i = 1
    while i * bus < current_min:
        i += 1
    if i*bus-current_min < minimal_time_diff:
        minimal_time_diff = i*bus-current_min
        bus_to_take = bus


print(minimal_time_diff*bus_to_take)