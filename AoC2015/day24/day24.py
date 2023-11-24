from functools import reduce
from itertools import combinations
from operator import mul
from typing import List, Dict, Any


def run(num_groups: int) -> int:
    with open('input.txt') as file:
        present_weights = [int(x) for x in file.read().splitlines()]
    required_size = int(sum(present_weights) / num_groups)

    for i in range(len(present_weights)):
        possible_combinations: list = [reduce(mul, combination) for combination in combinations(present_weights, i)
                                       if sum(combination) == required_size]
        if possible_combinations:
            return min(possible_combinations)


if __name__ == '__main__':
    print(run(3))
    print(run(4))
