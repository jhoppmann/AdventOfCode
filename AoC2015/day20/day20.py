from sympy import divisors


def run():
    target = 33100000
    i = 0
    while True:
        i += 1
        presents = sum(divisors(i))*10
        if presents >= target:
            break
    print(i)


if __name__ == '__main__':
    run()
