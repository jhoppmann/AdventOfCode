with open('input.txt') as file:
    input_text = file.read().splitlines()[0]

numbers = [int(x) for x in input_text.split(',')]
target = 2020

for i in range(len(numbers)-1, target):
    if numbers.count(numbers[i]) == 1:
        numbers.append(0)
    else:
        current_index = i + 1
        last_index = len(numbers) - numbers[-2::-1].index(numbers[i]) - 1
        new_number = current_index - last_index
        numbers.append(new_number)

print(numbers[target - 1])
