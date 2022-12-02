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
        split_line = line.split(' ')
        reindeer = {'name': split_line[0], 'speed': int(split_line[3]), 'duration': int(split_line[6]),
                    'rest': int(split_line[13]), 'cycle': int(split_line[6]) + int(split_line[13])}
        all_reindeer.append(reindeer)
    target_seconds = 2503

    reindeer_points = {}
    for sec in range(1, target_seconds + 1):
        reindeer_positions = {}
        for reindeer in all_reindeer:
            reindeer_positions[reindeer['name']] = compute_distance(reindeer, sec)
        max_dist = max(reindeer_positions.values())
        for key, value in reindeer_positions.items():
            if value == max_dist:
                if key in reindeer_points:
                    reindeer_points[key] += 1
                else:
                    reindeer_points[key] = 1

    print(max(reindeer_points.values()))


if __name__ == '__main__':
    run()
