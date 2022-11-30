with open('input.txt') as file:
    input_content = file.readlines()


def is_nice_string(test_string: str) -> bool:
    if test_string is None:
        return False
    if 'ab' in test_string or 'cd' in test_string or 'xy' in test_string or 'pq' in test_string:
        return False

    vowels = 0
    doubles = False
    for i in range(0, len(test_string)):

        if i != len(test_string)-1 and test_string[i] == test_string[i + 1]:
            doubles = True
        if test_string[i] in 'aeiou':
            vowels += 1

    return vowels >= 3 and doubles


niceStrings = 0
for line in input_content:
    if is_nice_string(line):
        niceStrings += 1

print(niceStrings)
