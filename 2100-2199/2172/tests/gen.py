"""Sponsors from "MODE SEED": mode 1 a few sponsors with small wishes,
mode 2 1000 sponsors and a random K with the total near 10^5, mode 3 one
sponsor that wants far more than the others, mode 4 K = 1."""

import random
import sys

MAX_N = 1000
MAX_S = 1000
MAX_TOTAL = 10 ** 5
SMALL = 6


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(1, SMALL), rng.randint(1, SMALL)
        s = [rng.randint(1, SMALL) for _ in range(n)]
    else:
        n = MAX_N
        k = 1 if mode == 4 else rng.randint(1, MAX_N)
        top = MAX_TOTAL // n
        s = [rng.randint(1, top) for _ in range(n)]
        if mode == 3:
            s[rng.randrange(n)] = MAX_S
            while sum(s) > MAX_TOTAL:
                i = rng.randrange(n)
                if s[i] > 1 and s[i] != MAX_S:
                    s[i] -= 1
    print(n, k)
    print(*s)


main()
