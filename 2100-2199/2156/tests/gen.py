"""Friends from "MODE SEED": mode 1 a few small values, mode 2 10^5
random values, mode 3 10^5 equal values, mode 4 10^5 values with many
equal neighbours."""

import random
import sys

MAX_N = 10 ** 5
MAX_A = 10 ** 9
SMALL_N = 8
SMALL_A = 4


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(3, SMALL_N)
        a = [rng.randint(1, SMALL_A) for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        a = [rng.randint(1, MAX_A) for _ in range(n)]
    elif mode == 3:
        n = MAX_N
        a = [rng.randint(1, MAX_A)] * n
    else:
        n = MAX_N
        a = []
        while len(a) < n:
            a += [rng.randint(1, MAX_A)] * rng.randint(1, SMALL_N)
        a = a[:n]
    print(n)
    print(*a)


main()
