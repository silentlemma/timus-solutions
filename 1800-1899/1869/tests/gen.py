"""A ticket matrix from a seed and a mode: mode 1 a few stations, 2 the
most stations with random counts, 3 the most stations with every count
1000, 4 the most stations with all tickets for the westbound train,
5 the most stations, nearly all counts 0."""

import random
import sys

MOST = 100
FEW = 5
LARGEST = 1000


def count(rng, mode, i, j):
    if i == j or (mode == 4 and i < j):
        return 0
    if mode == 3:
        return LARGEST
    if mode == 5:
        return rng.randint(0, LARGEST) if rng.random() < 0.01 else 0
    return rng.randint(0, LARGEST)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW) if mode == 1 else MOST
    print(n)
    for i in range(n):
        print(" ".join(str(count(rng, mode, i, j)) for j in range(n)))


main()
