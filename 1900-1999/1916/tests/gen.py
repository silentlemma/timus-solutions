"""seed mode:1 small random,2 stable,3 aliases,4 flat max,5 repeated,
6 uniform doubling,7 alternating doubling,8 disjoint periods,9 random max,
10 many boundaries,11 width two,12 shared aliases,13 duplicate occurrences,
14 high symbol IDs,15 deep forward chain,16 ternary periodic expansion.
"""

import random
import sys

MAX_TYPES = 100
MAX_EDGES = 100
MAX_WIDTH = 100
MAX_LITERAL = 1000000
STABLE = 2
ALIASES = 3
FLAT = 4
REPEATED = 5
DOUBLING = 6
ALTERNATING = 7
DISJOINT = 8
RANDOM_MAX = 9
BOUNDARIES = 10
WIDTH_TWO = 11
SHARED = 12
OCCURRENCES = 13
HIGH_SYMBOLS = 14
FORWARD = 15
TERNARY = 16
PERMUTE_SALT = 571


def make_base_case(seed, mode):
    rng = random.Random(seed)
    count = rng.randint(2, 10) if mode == 1 else MAX_TYPES
    rules = [None] * count
    width = MAX_WIDTH
    if mode == 1:
        width = rng.randint(2, 12)
        for vertex in range(1, count):
            if rng.randrange(3):
                rules[vertex] = [
                    rng.randrange(vertex) for _ in range(rng.randint(1, 3))
                ]
    elif mode == STABLE:
        pass
    elif mode == ALIASES:
        width = 2
        for vertex in range(1, count):
            rules[vertex] = [vertex - 1]
    elif mode == FLAT:
        rules[-1] = list(range(count - 1)) + [0]
    elif mode in (REPEATED, OCCURRENCES):
        width = MAX_WIDTH if mode == REPEATED else 2
        rules[-1] = [0] * MAX_EDGES
    elif mode == DOUBLING:
        for vertex in range(1, MAX_EDGES // 2 + 1):
            rules[vertex] = [vertex - 1, vertex - 1]
    elif mode == ALTERNATING:
        rules[2] = [0, 1]
        for vertex in range(3, MAX_EDGES // 2 + 2):
            rules[vertex] = [vertex - 1, vertex - 1]
    elif mode == DISJOINT:
        rules[4], rules[5] = [0, 1], [2, 3]
        for vertex in range(6, 52):
            rules[vertex] = [vertex - 2, vertex - 2]
    elif mode in (RANDOM_MAX, WIDTH_TWO):
        width = 2 if mode == WIDTH_TWO else MAX_WIDTH
        lengths = [1] * count
        for vertex in range(count // 2, count):
            other = rng.randrange(vertex)
            if lengths[vertex - 1] + lengths[other] > MAX_LITERAL:
                other = rng.randrange(count // 2)
            rules[vertex] = [vertex - 1, other]
            lengths[vertex] = lengths[vertex - 1] + lengths[other]
    elif mode == BOUNDARIES:
        rules[50], rules[51] = [0] * 30, [1] * 30
        rules[52] = [50, 51, 0, 1, 50, 51]
    elif mode == SHARED:
        width = 40
        rules[49] = list(range(49))
        for vertex in range(50, count):
            rules[vertex] = [vertex - 1]
    elif mode == HIGH_SYMBOLS:
        rules[0] = [99, 98]
        for vertex in range(1, MAX_EDGES // 2):
            rules[vertex] = [vertex - 1, vertex - 1]
    elif mode == FORWARD:
        width = 2
        rules[0] = [1, 1]
        for vertex in range(1, count - 1):
            rules[vertex] = [vertex + 1]
        return width, rules
    elif mode == TERNARY:
        rules[3] = [0, 1, 2]
        for vertex in range(4, 36):
            rules[vertex] = [vertex - 1] * 3
    else:
        raise ValueError("unknown generator mode")
    return width, rules


def make_case(seed, mode):
    width, rules = make_base_case(seed, mode)
    if mode in (HIGH_SYMBOLS, FORWARD):
        return width, rules
    permutation = list(range(len(rules)))
    random.Random(seed ^ PERMUTE_SALT).shuffle(permutation)
    result = [None] * len(rules)
    for vertex, children in enumerate(rules):
        result[permutation[vertex]] = (
            None if children is None else [permutation[child] for child in children]
        )
    return width, result


def main():
    width, rules = make_case(int(sys.argv[1]), int(sys.argv[2]))
    print(len(rules), width)
    for children in rules:
        if children is None:
            print(-1)
        else:
            print(len(children), *(child + 1 for child in children))


if __name__ == "__main__":
    main()
