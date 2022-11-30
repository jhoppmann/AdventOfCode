import json
from numbers import Number


def run():
    with open('input.txt') as file:
        input_content = file.read().splitlines()

    json_string = input_content[0]

    json_tree = json.loads(json_string)
    result = 0
    result = walk(json_tree)

    print(result)


def walk(node):
    result = 0
    if isinstance(node, list):
        for item in node:
            if isinstance(item, Number):
                result += item
            else:
                result += walk(item)
    elif isinstance(node, dict):
        if 'red' in node.values():
            return 0
        for key, item in node.items():
            if isinstance(item, Number):
                result += item
            else:
                result += walk(item)
    return result


if __name__ == '__main__':
    run()