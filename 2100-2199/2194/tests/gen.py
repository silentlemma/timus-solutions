"""Boards from "MODE SEED": mode 1 a small board with many snakes, mode 2
2 * 10^5 cells with sparse random snakes, mode 3 2 * 10^5 cells where only every
k-th cell is safe for some k from 2 to 5, mode 4 2 * 10^5 cells with
six snakes in a row somewhere, which no roll can cross."""

import random
import sys

MAX_N = 2 * 10 ** 5
SMALL_N = 14
SAFE = 5
SPARSE = 20


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL_N) if mode == 1 else MAX_N
    p = [0] * (n + 1)
    spacing = rng.randint(2, SAFE)
    for i in range(2, n):
        if mode == 1:
            chance = rng.randint(0, 2)
            p[i] = rng.randint(1, i - 1) if chance else 0
        elif mode == 2:
            p[i] = 0 if rng.randint(0, SPARSE) else rng.randint(1, i - 1)
        elif mode == 3:
            p[i] = 0 if (i - 1) % spacing == 0 else rng.randint(1, min(i - 1, SAFE))
        else:
            p[i] = 0 if rng.randint(0, 1) else rng.randint(1, i - 1)
    if mode == 4:
        start = rng.randint(2, n - SAFE - 2)
        for i in range(start, start + SAFE + 1):
            p[i] = rng.randint(1, i - 1)
    print(n)
    print(*p[2:n])


main()
