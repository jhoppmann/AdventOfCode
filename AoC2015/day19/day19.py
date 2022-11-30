import re


def run():
    with open('input.txt') as file:
        input_lines = file.readlines()
    rules = []
    for line in input_lines[0:-2]:
        elements = line.split(" => ")
        rules.append((elements[0], elements[1][0:-1]))

    molecule = input_lines[-1]
    print(len(step(molecule, rules)))


def step(molecule: str, rules: list) -> set:
    result = set()
    for rule in rules:
        element, replacement = rule
        indices = [m.start() for m in re.finditer(element, molecule)]
        for indice in indices:
            new_molecule = molecule[0:indice] + replacement
            if indice < (len(molecule)):
                new_molecule += molecule[indice + len(element):]
            result.add(new_molecule)
    return result


if __name__ == '__main__':
    run()
