def is_touching(head_pos: tuple, tail_pos: tuple) -> bool:
    if abs(head_pos[0] - tail_pos[0]) >= 2:
        return False
    if abs(head_pos[1] - tail_pos[1]) >= 2:
        return False
    return True


def run():
    with open('input.txt') as file:
        movements = file.read().splitlines()

    head_pos = (0, 0)
    tail_pos = (0, 0)

    tail_positions = set()
    for movement in movements:
        direction, length = movement.split(" ")
        length = int(length)
        for i in range(1, length + 1):

            if direction == 'R': # forward in x direction
                head_pos = (head_pos[0] + 1, head_pos[1])
                if not is_touching(head_pos, tail_pos):
                    tail_pos = (head_pos[0] - 1, head_pos[1])
            elif direction == 'L': # backward in x direction
                head_pos = (head_pos[0] - 1, head_pos[1])
                if not is_touching(head_pos, tail_pos):
                    tail_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == 'U': # forward in y direction
                head_pos = (head_pos[0], head_pos[1] + 1)
                if not is_touching(head_pos, tail_pos):
                    tail_pos = (head_pos[0], head_pos[1] - 1)
            elif direction == 'D': # backward in y direction
                head_pos = (head_pos[0], head_pos[1] - 1)
                if not is_touching(head_pos, tail_pos):
                    tail_pos = (head_pos[0], head_pos[1] + 1)

            tail_positions.add(tail_pos)

    print(len(tail_positions))


if __name__ == '__main__':
    run()
