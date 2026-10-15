"""One test from a seed and a mode: a random walk over a few vertices
(mode 1 short, mode 2 100000 vertices over 30, mode 3 100000 over 10000,
mode 4 a walk that ends where it starts)."""

import random
import sys

MOST = 100000
TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 12) if mode == 1 else MOST
    labels = {1: 5, 2: 30, 3: TOP, 4: 6}[mode]
    chain = [rng.randint(1, labels)]
    while len(chain) < n:
        v = rng.randint(1, labels)
        if v != chain[-1]:
            chain.append(v)
    if mode == 4:
        # close the walk: the last vertex repeats the first, and the one
        # before differs from both of its neighbours
        first = chain[0]
        chain[-1] = first
        before = chain[-3]
        chain[-2] = next(v for v in range(1, labels + 1) if v not in (first, before))
    print(n)
    for i in range(0, n, 20):
        print(*chain[i : i + 20])


main()
