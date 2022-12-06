def run():
    with open('input.txt') as file:
        databuffer = file.read().splitlines()[0]

    # Part 1
    for index in range(0, len(databuffer) - 13):
        if len(set(databuffer[index:index+4])) == 4:
            print(index + 4)
            break

    # Part 2
    for index in range(0, len(databuffer) - 13):
        if len(set(databuffer[index:index+14])) == 14:
            print(index + 14)
            break


if __name__ == '__main__':
    run()