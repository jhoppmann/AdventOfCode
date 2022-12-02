import sys
import multiprocessing

with open('testinput.txt') as file:
    notes = file.read().splitlines()
bus_table = [x for x in notes[1].split(',')]

times_tables = []

def find_times(starting_offset: int, busid: int, offset: int, threads: list):
    times = set()
    i = starting_offset
    departure = i * busid + offset
    while departure < maxsize:
        times.add(departure)
        i += 1
        departure = i * busid + offset
    threads.append(times)

busses = []
busses_and_offsets = {}

for i in range(len(bus_table)):
    if bus_table[i].isnumeric():
        busses_and_offsets[int(bus_table[i])] = i
        busses.append(int(bus_table[i]))

offsets = [busses_and_offsets[x] for x in busses]

results = set()
maxsize = 6000 # sys.maxsize - sum(busses)

threads = multiprocessing.Value('list', [])
for i in range(0, len(busses)):
    thread = multiprocessing.Process(target=find_times, args=(0, busses[i], offsets[i], threads))
    threads.append(thread)
    thread.start()
    print('Thread' + str(i) + ' started')

for index, thread in enumerate(threads):
    print(str(index) + ' joined')
    thread.join()
    print(str(index) + ' joined')
print(threads)

rest = set()
for i in range(0, len(times_tables) - 1):

    rest = set.intersection(times_tables[i], times_tables[i+1])
print(rest)
