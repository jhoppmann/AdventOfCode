def compute_distance(reindeer, target_seconds):
    travelled = 0
    completed = int(target_seconds / reindeer['cycle'])
    travelled += completed * reindeer['speed'] * reindeer['duration']
    remainder = target_seconds - completed * reindeer['cycle']
    remainder = min(remainder, reindeer['duration'])
    travelled += remainder * reindeer['speed']
    return travelled


def run():
    pass
    with open('input.txt') as file:
        input_content = file.read().splitlines()

    all_reindeer = []
    for line in input_content:
        split_line = line.split(" ")
        reindeer = {'name': split_line[0], 'speed': int(split_line[3]), 'duration': int(split_line[6]),
                    'rest': int(split_line[13]), 'cycle': int(split_line[6]) + int(split_line[13])}
        all_reindeer.append(reindeer)

    max_dist = 0
    target_seconds = 2503

    for reindeer in all_reindeer:
        max_dist = max(max_dist, compute_distance(reindeer, target_seconds))
    print(max_dist)


if __name__ == '__main__':
    run()