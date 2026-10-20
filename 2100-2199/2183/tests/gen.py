"""Moods from "MODE SEED": mode 1 a few small values, mode 2 10^5 random
values over the whole range, mode 3 10^5 values with one deep negative
block, mode 4 10^5 values at the bounds."""

import random
import sys

MAX_N = 10 ** 5
LIMIT = 10 ** 9
SMALL_N = 7
SMALL_V = 5


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        a = [rng.randint(-SMALL_V, SMALL_V) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        a = [rng.randint(-LIMIT, LIMIT) for _ in range(n)]
    elif mode == 3:
        n = MAX_N
        a = [rng.randint(0, LIMIT) for _ in range(n)]
        start = rng.randrange(n)
        for i in range(start, min(n, start + rng.randint(1, n))):
            a[i] = -rng.randint(0, LIMIT)
    else:
        n = MAX_N
        a = [rng.choice([-LIMIT, LIMIT]) for _ in range(n)]
    if min(a) >= 0:
        a[rng.randrange(n)] = -rng.randint(1, SMALL_V)
    print(n)
    print(*a)


main()
