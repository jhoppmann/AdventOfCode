from pprint import pprint

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


def is_ticket_valid(rules: dict, ticket: tuple) -> bool:
    valid_fields = 0
    for value in ticket:
        for rule in rules.values():
            if rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]:
                valid_fields += 1
                break
    return valid_fields == len(ticket)


def calculate_remaining_tickets(rules: dict, tickets: list):
    return [x for x in tickets if is_ticket_valid(rules, x)]


def read_my_ticket(input_lines: list) -> tuple:
    tickets = []
    i = 0
    for line in input_text:
        if line == 'your ticket:':
            break
        i += 1
    i += 1
    line = input_lines[i]
    return tuple([int(x) for x in line.split(',')])


def calculate_possible_fields(rules: dict, tickets: list) -> dict:
    possible_rules_for_field = {}
    for field in range(0, len(tickets[0])):
        fields = []
        for ticket in tickets:
            value = ticket[field]
            possible_fields = []
            for rule_name, rule in rules.items():
                if rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]:
                    possible_fields.append(rule_name)
            fields.append(possible_fields)
        possible_rules_for_field[field] = fields
    return possible_rules_for_field


rules = determine_rules(input_text)
my_ticket = read_my_ticket(input_text)
tickets = read_tickets(input_text)
print(rules, '\n', tickets)
tickets = calculate_remaining_tickets(rules, tickets)
possible_fields = calculate_possible_fields(rules, tickets)

