with open('input.txt') as file:
    input_text = file.read().splitlines()


def determine_rules(input_lines: list) -> dict:
    rules = {}
    for line in input_text:
        if line == '':
            break
        splitted = line.split(':')
        rule_name = splitted[0]
        ranges = splitted[1].strip().split(' or ')
        value = []
        for rule_range in ranges:
            split_range = rule_range.split('-')
            value.append((int(split_range[0]), int(split_range[1])))
        rules[rule_name] = value
    return rules


def read_tickets(input_lines: list) -> list:
    tickets = []
    i = 0
    for line in input_text:
        if line == 'nearby tickets:':
            break
        i += 1
    i += 1
    while i < len(input_lines):
        line = input_lines[i]
        tickets.append(tuple([int(x) for x in line.split(',')]))
        i += 1
    return tickets


def get_invalid_field(rules: dict, ticket: tuple) -> int:
    invalid_fields = 0
    for value in ticket:
        found_fitting_rule = False
        for rule in rules.values():
            found_fitting_rule = rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]
            if found_fitting_rule:
                break
        if not found_fitting_rule:
            invalid_fields += value
    return invalid_fields


def calculate_scan_failure_rate(rules: dict, tickets: list):
    failure_rate = 0
    for ticket in tickets:
        failure_rate += get_invalid_field(rules, ticket)
    return failure_rate


rules = determine_rules(input_text)
tickets = read_tickets(input_text)
print(calculate_scan_failure_rate(rules, tickets))
