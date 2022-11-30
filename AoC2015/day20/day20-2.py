from sympy import divisors


def run():
    target = 33100000
    house = 0
    elves_delivered = {}
    while True:
        house += 1
        divisor_list = divisors(house)
        presents = 0
        for divisor in divisor_list:
            if divisor not in elves_delivered:
                elves_delivered[divisor] = 0
            elves_delivered[divisor] += 1
            if elves_delivered[divisor] <= 50:
                presents += divisor * 11

        if presents >= target:
            break
    print(house)


if __name__ == '__main__':
    run()
