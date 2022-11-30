import string

with open('input.txt') as file:
    questionnaire_data = file.read().splitlines()


def find_groups(data: list) -> list:
    groups = []
    group = []
    for line in data:
        if line == '':
            groups.append(group)
            group = []
        else:
            group.append(line)
    if len(group) > 0:
        groups.append(group)
    return groups


def find_answered(group: list) -> int:
    count = len(group)
    all_answers = ''
    result = 0
    for persons_answers in group:
        all_answers += persons_answers
    for char in string.ascii_lowercase:
        if all_answers.count(char) == count:
            result += 1
    return result


groups = find_groups(questionnaire_data)

result = 0

for group in groups:
    result += find_answered(group)

print(result)

