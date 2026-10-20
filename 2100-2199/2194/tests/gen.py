"""Boards from "MODE SEED [N]": mode 1 a small board with many snakes, mode 2
2 * 10^5 cells with sparse random snakes, mode 3 2 * 10^5 cells where only every
k-th cell is safe for some k from 2 to 5, mode 4 2 * 10^5 cells with
six snakes in a row somewhere, which no roll can cross. Mode 5 has one long
chain of length-one snakes back to the start; mode 6 requires a new turn for
each five-cell advance, with sixes looping to the same safe cell; mode 7 has
randomly spaced safe cells and random snakes between them. Modes 5-7 accept
N (2 <= N <= 200000), defaulting to 200000."""

import random
import sys

MAX_N = 2 * 10 ** 5
SMALL_N = 14
SAFE = 5
SPARSE = 20


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    if mode in (5, 6, 7):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else MAX_N
        if not 2 <= n <= MAX_N:
            raise ValueError("N must be between 2 and 200000")
        rng = random.Random(seed)
        if mode == 5:
            p = [1] * (n - 2)
        elif mode == 6:
            p = [min(6, i - 1) if (i - 1) % 5 == 1 else (i - 1) % 5
                 for i in range(2, n)]
        else:
            safe = {1}
            cell = 1
            while cell < n:
                cell += rng.randint(2, 5)
                safe.add(cell)
            p = [0 if i in safe else rng.randint(1, i - 1) for i in range(2, n)]
        print(n)
        print(*p)
        return
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
