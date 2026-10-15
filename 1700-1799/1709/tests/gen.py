"""One test from a seed and a mode: mode 1 a small random graph, mode 2
100 airports with a random density, mode 3 100 airports in a few dense
groups with no flights between them, mode 4 a random forest."""

import random
import sys

MOST = 100
PRICE = 10 ** 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode == 1 else MOST
    edges = set()
    if mode in (1, 2):
        p = rng.random()
        edges = {(i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < p}
    elif mode == 3:
        group = [rng.randrange(rng.randint(2, 6)) for _ in range(n)]
        edges = {(i, j) for i in range(n) for j in range(i + 1, n)
                 if group[i] == group[j] and rng.random() < 0.7}
    else:
        for v in range(1, n):
            if rng.random() < 0.9:
                edges.add((rng.randrange(v), v))
    d, a = rng.randint(1, PRICE), rng.randint(1, PRICE)
    print(n)
    print(d, a)
    for i in range(n):
        print("".join("1" if (min(i, j), max(i, j)) in edges else "0" for j in range(n)))


main()
