"""Sponsors from "MODE SEED": mode 1 a few sponsors and problems, mode 2
1000 sponsors with the total wish 2M, mode 3 two sponsors that want all
2000 problems, mode 4 random wishes with a total below 2M, mode 5 five
mixed wishes leaving three unused slots, mode 6 six sparse random wishes
with at least two more problems than mentions."""

import random
import sys

MAX_N = 1000
MAX_M = 2000
SMALL = 4


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        m = rng.randint(1, SMALL)
        n = rng.randint(1, min(SMALL, 2 * m))
        s = [rng.randint(1, m) for _ in range(n)]
        while sum(s) > 2 * m:
            s[rng.randrange(n)] = 1
    elif mode == 2:
        n, m = MAX_N, MAX_M
        s = [1] * n
        for _ in range(2 * m - n):
            s[rng.randrange(n)] += 1
    elif mode == 3:
        n, m = 2, MAX_M
        s = [m, m]
    elif mode == 5:
        n, m = 5, rng.randint(7, 9)
        s = [1] * n
        while sum(s) < 2 * m - 3:
            i = rng.randrange(n)
            if s[i] < m:
                s[i] += 1
    elif mode == 6:
        n, m = 6, rng.randint(14, 18)
        s = [rng.randint(1, 3) for _ in range(n)]
        while sum(s) > m - 2:
            i = rng.randrange(n)
            s[i] = max(1, s[i] - 1)
    else:
        n, m = MAX_N, MAX_M
        s = [rng.randint(1, 2 * 2 * m // n - 1) for _ in range(n)]
        while sum(s) > 2 * m:
            i = rng.randrange(n)
            s[i] = max(1, s[i] - 1)
    print(n, m)
    print(*s)


main()
