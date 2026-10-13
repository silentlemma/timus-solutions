"""A tree of 50 000 branches: a seed and a mode. Mode 1 gives a random
tree, mode 2 a path of the dearest edges, the largest sum, mode 3 a
star, mode 4 random trees with edges given in random direction and
order."""

import random
import sys

COUNT = 50000
DEAREST = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = COUNT
    label = list(range(1, n + 1))
    rng.shuffle(label)
    edges = []
    for v in range(1, n):
        if mode == 2:
            edges.append((label[v - 1], label[v], DEAREST))
        elif mode == 3:
            edges.append((label[0], label[v], rng.randint(0, DEAREST)))
        else:
            edges.append((label[rng.randrange(v)], label[v], rng.randint(0, DEAREST)))
    if mode == 4:
        rng.shuffle(edges)
        edges = [(b, a, c) if rng.random() < 0.5 else (a, b, c) for a, b, c in edges]
    print(n)
    for e in edges:
        print(*e)


main()
