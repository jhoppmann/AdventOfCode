with open('input.txt') as file:
    input_content = file.readlines()


def is_nice_string(test_string: str) -> bool:
    if test_string is None:
        return False

    doubles = False
    repeating_with_letter_between = False
    for i in range(0, len(test_string)):
        char = test_string[i]
        if i != len(test_string)-1 and test_string.count(char + test_string[i + 1]) >= 2:
            doubles = True

        if i < len(test_string)-2 and char == test_string[i + 2]:
            repeating_with_letter_between = True

    return repeating_with_letter_between and doubles


niceStrings = 0
for line in input_content:
    if is_nice_string(line):
        niceStrings += 1

print(niceStrings)
