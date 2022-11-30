import time
with open('input.txt') as file:
    input_text = file.read().splitlines()[0]

previous_nums = {}
number = 0
for pos, number in enumerate([int(x) for x in input_text.split(',')]):
    previous_nums[number] = (1, pos + 1, pos+1)
target = 30_000_000
old_number = number

start = time.time()
for i in range(len(previous_nums.keys())-1, target):  # range is fine because no starting number is doubled in inputs
    current_index = i + 2
    if old_number in previous_nums and previous_nums[old_number][0] == 1:
        old_values = previous_nums[0]
        previous_nums[0] = (old_values[0] + 1, current_index, old_values[1])
        old_number = 0
    else:
        new_number = previous_nums[old_number][1] - previous_nums[old_number][2]
        if new_number not in previous_nums:
            previous_nums[new_number] = (0, 0, 0)
        old_values = previous_nums[new_number]
        previous_nums[new_number] = (old_values[0] + 1, current_index, old_values[1])
        old_number = new_number

    if current_index == target:
        print(old_number)
        break
print(time.time() - start)


