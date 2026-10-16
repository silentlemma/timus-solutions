"""One test from a seed and a mode: mode 1 any k, n and counts, mode 2
counts that hover around k, so the jam keeps forming and clearing."""

import random
import sys

LIMIT = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    k, n = rng.randint(1, LIMIT), rng.randint(1, LIMIT)
    if mode == 1:
        cars = [rng.randint(0, LIMIT) for _ in range(n)]
    else:
        spread = rng.randint(1, LIMIT // 2)
        cars = [min(LIMIT, max(0, k + rng.randint(-spread, spread))) for _ in range(n)]
    print(k, n)
    print(*cars)


main()
