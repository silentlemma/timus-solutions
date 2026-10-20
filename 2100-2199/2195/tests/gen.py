"""Generate deterministic pairs of binary trees, keeping root zero fixed."""

import random
import sys

MIN_SIZE = 2
SMALL_SIZE = 40
MEDIUM_SIZE = 250
MAX_SIZE = 1000
ARGUMENT_COUNT = 3
MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_RANDOM_MAX = 3
MODE_CHAIN_BALANCED = 4
MODE_BALANCED_CHAIN = 5
MODE_COMB_BALANCED = 6
MODE_BALANCED_COMB = 7
MODE_ISOMORPHIC = 8
MODE_CHAIN_ISOMORPHIC = 9
MODE_BROOM = 10
MODE_TWO_CHAINS = 11


def random_tree(n, rng):
    parents = [-1] * n
    available = [0]
    degree = [0] * n
    for vertex in range(1, n):
        position = rng.randrange(len(available))
        parent = available[position]
        parents[vertex] = parent
        degree[parent] += 1
        if degree[parent] == 2:
            available[position] = available[-1]
            available.pop()
        available.append(vertex)
    return parents


def chain(n):
    return [-1] + list(range(n - 1))


def balanced(n):
    return [-1] + [(vertex - 1) // 2 for vertex in range(1, n)]


def comb(n):
    return [-1] + [2 * ((vertex - 1) // 2) for vertex in range(1, n)]


def broom(n):
    stem = n // 2
    return [-1] + [
        vertex - 1 if vertex <= stem else stem + (vertex - stem - 1) // 2 for vertex in range(1, n)
    ]


def two_chains(n):
    return [-1] + [0 if vertex <= 2 else vertex - 2 for vertex in range(1, n)]


def relabel(parents, rng):
    n = len(parents)
    labels = list(range(1, n))
    rng.shuffle(labels)
    labels = [0] + labels
    result = [-1] * n
    for vertex in range(1, n):
        result[labels[vertex]] = labels[parents[vertex]]
    return result


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL:
        n = rng.randint(MIN_SIZE, SMALL_SIZE)
        first, second = random_tree(n, rng), random_tree(n, rng)
    elif mode == MODE_MEDIUM:
        n = rng.randint(SMALL_SIZE, MEDIUM_SIZE)
        first, second = random_tree(n, rng), random_tree(n, rng)
    else:
        n = MAX_SIZE
        if mode == MODE_RANDOM_MAX:
            first, second = random_tree(n, rng), random_tree(n, rng)
        elif mode == MODE_CHAIN_BALANCED:
            first, second = chain(n), balanced(n)
        elif mode == MODE_BALANCED_CHAIN:
            first, second = balanced(n), chain(n)
        elif mode == MODE_COMB_BALANCED:
            first, second = comb(n), balanced(n)
        elif mode == MODE_BALANCED_COMB:
            first, second = balanced(n), comb(n)
        elif mode == MODE_ISOMORPHIC:
            first = random_tree(n, rng)
            second = first[:]
        elif mode == MODE_CHAIN_ISOMORPHIC:
            first, second = chain(n), chain(n)
        elif mode == MODE_BROOM:
            first, second = broom(n), comb(n)
        elif mode == MODE_TWO_CHAINS:
            first, second = two_chains(n), random_tree(n, rng)
        else:
            raise ValueError("unknown generator mode")
    return relabel(first, rng), relabel(second, rng)


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: gen.py MODE SEED")
    first, second = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(len(first))
    print(*first[1:])
    print(*second[1:])


if __name__ == "__main__":
    main()
