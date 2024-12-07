def run():
    with open('input.txt') as file:
        page_ordering = file.read().splitlines()

    rules = {}
    orderings = []
    for line in page_ordering:
        if '|' in line:
            (first, second) = line.split('|')
            if int(first) in rules:
                rules[int(first)].append(int(second))
            else:
                rules[int(first)] = [int(second)]
        if ',' in line:
            orderings.append([int(x) for x in line.split(',')])

    middles_sum = 0
    correct_orderings = process_rules(rules, orderings)
    for ordering in correct_orderings:
        middles_sum += ordering[int(len(ordering) / 2)]

    print("Part 1:", middles_sum)


def process_rules(rules: dict, orderings: list) -> list:
    correct_orderings = []
    for ordering in orderings:
        correct = process_rule(ordering, rules)
        if correct:
            correct_orderings.append(ordering)
    return correct_orderings


def process_rule(ordering: list, rules: dict) -> bool:
    correct = True
    for i in range(0, len(ordering)):
        if ordering[i] in rules:
            mappings = rules[ordering[i]]
            for mapping in mappings:
                if mapping in ordering and ordering.index(mapping) < i:
                    correct = False
    return correct


if __name__ == '__main__':
    run()
