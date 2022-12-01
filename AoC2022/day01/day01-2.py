def main():
    with open('input.txt') as file:
        calories = file.read().splitlines()

    elfs = []
    calorie_sum = 0
    for snack in calories:
        if not snack:
            elfs.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(snack)

    elfs.sort()
    print(sum(elfs[-1:-4:-1]))


if __name__ == '__main__':
    main()
