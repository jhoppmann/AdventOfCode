with open('input.txt') as file:
    questionnaire_data = file.read().splitlines()


def find_groups(data: list) -> list:
    groups = []
    group = ''
    for line in data:
        if line == '':
            groups.append(group)
            group = ''
        else:
            group += line
    groups.append(group)
    return groups


def count_unique_answers(group: str) -> int:
    answers = set()
    for char in group:
        answers.add(char)
    return len(answers)


groups = find_groups(questionnaire_data)

result = 0
for group in groups:
    print(group)
    result += count_unique_answers(group)

print(result)

