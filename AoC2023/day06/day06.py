import re
from numpy import prod


def run():
    with open('input.txt') as file:
        race_data = file.read().splitlines()

    times = [int(x) for x in re.findall(r'\d+', race_data[0])]
    distances = [int(x) for x in re.findall(r'\d+', race_data[1])]

    races = list(zip(times, distances))
    ways_to_win_by_race = []
    for race in races:
        distance = race[1]
        ways_to_win = 0
        for i in range(0, race[0] + 1):
            if i * (race[0] - i) > distance:
                ways_to_win += 1
        ways_to_win_by_race.append(ways_to_win)

    print('Part 1:', prod(ways_to_win_by_race))

    time = int(''.join(re.findall(r'\d+', race_data[0])))
    distance = int(''.join(re.findall(r'\d+', race_data[1])))
    ways_to_win = 0
    for i in range(0, time + 1):
        if i * (time - i) > distance:
            ways_to_win += 1

    print('Part 2:', ways_to_win)


if __name__ == '__main__':
    run()
