with open('input.txt') as file:
    input_terms = file.read().splitlines()


def evaluate(term: str) -> int:
    value = 0
    for char in term:
        if char == '*':
            operand = '*'

    pass


result = 0
for term in input_terms:
    sum += evaluate(term)
