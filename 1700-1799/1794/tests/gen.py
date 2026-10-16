"""One test from a seed and a mode: mode 1 any wishes of a small class,
mode 2 any wishes of up to 100000 students, mode 3 a class where most
students agree on one start and the rest ask at random."""

import random
import sys

LIMIT = 100000
SMALL = 8


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL if mode == 1 else LIMIT)
    if mode == 3:
        start = rng.randint(1, n)
        share = rng.random()
        wants = [(i - start) % n + 1 if rng.random() < share else rng.randint(1, n)
                 for i in range(1, n + 1)]
    else:
        wants = [rng.randint(1, n) for _ in range(n)]
    print(n)
    print(*wants)


main()
