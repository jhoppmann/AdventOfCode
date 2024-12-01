def run():
    with open('input.txt') as file:
        location_ids = file.read().splitlines()

    list_left = []
    list_right = []

    for line in location_ids:
        # is the number of whitespaces constant in all inputs? Don't know, don't care
        numbers = line.split(" ")
        list_left.append(int(numbers[0]))
        list_right.append(int(numbers[-1]))

    list_left.sort()
    list_right.sort()
    distance_sum = 0
    similarity_score = 0

    for i in range(0, len(list_left)):
        distance_sum += abs(list_left[i] - list_right[i])

        similarity_score += list_left[i] * list_right.count(list_left[i])

    print("Part 1:", distance_sum)
    print("Part 2:", similarity_score)


if __name__ == '__main__':
    run()
