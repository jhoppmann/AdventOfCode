def run():
    with open('input.txt') as file:
        databuffer = file.read().splitlines()[0]

    # Part 1
    print(find_different_character_substring(4, databuffer))

    # Part 2
    print(find_different_character_substring(14, databuffer))


def find_different_character_substring(length: int, databuffer) -> int:
    for index in range(0, len(databuffer) - length):
        if len(set(databuffer[index:index + length])) == length:
            return index + length


if __name__ == '__main__':
    run()
