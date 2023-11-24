def run():
    with open("input.txt") as file:
        room_list = file.read().splitlines()
    room_list = [(x[0:-11], x[-7:], int(x[-10:-7])) for x in room_list]
    correct_rooms_sums = 0
    correct_rooms = []
    for room in room_list:
        room_name = room[0].replace('-', '')
        counts = {x: room_name.count(x) for x in room_name}
        clustered_counts = {}
        for key, val in counts.items():
            if val not in clustered_counts:
                clustered_counts[val] = [key]
            else:
                clustered_counts[val].append(key)
        checksum = ''
        for i in range(max(clustered_counts.keys()), 0, -1):
            if i in clustered_counts:
                chars = sorted(clustered_counts[i])
                for character in chars:
                    checksum += character
            if len(checksum) >= 5:
                checksum = checksum[0:5]
                if checksum == room[1][1:6]:
                    correct_rooms_sums += room[2]
                    correct_rooms.append(room)
                break
    print("Part 1:", correct_rooms_sums)

    for room in correct_rooms:
        result = ''
        for c in room[0]:
            if c != '-':
                shift = (ord(c) - 96 + room[2]) % 26
                if shift == 0:
                    shift = 26
                new_character = chr(shift + 96)
            else:
                new_character = c
            result += new_character
        if result == 'northpole-object-storage':
            print("Part 2:", room[2])


if __name__ == '__main__':
    run()
