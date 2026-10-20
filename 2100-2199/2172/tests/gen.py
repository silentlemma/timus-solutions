"""Sponsors from "MODE SEED": mode 1 a few sponsors with small wishes,
mode 2 1000 sponsors and a random K with the total near 10^5, mode 3 one
sponsor that wants far more than the others, mode 4 K = 1, mode 5 maximal
N and K with equal wishes and total 10^5, mode 6 K = 1 and total 10^5,
mode 7 seeded random wishes with total 10^5 and K = 3."""

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
    elif mode in (5, 6, 7):
        n = MAX_N
        k = {5: MAX_N, 6: 1, 7: 3}[mode]
        s = [MAX_TOTAL // n] * n
        if mode == 7:
            s = [1] * n
            slots = rng.sample(range(n * (MAX_S - 1)), MAX_TOTAL - n)
            for slot in slots:
                s[slot // (MAX_S - 1)] += 1
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
