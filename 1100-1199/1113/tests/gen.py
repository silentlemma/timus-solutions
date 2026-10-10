"""Random trips: a seed and a mode. Mode 0 draws any valid N and M, mode 1
takes M divisible by many small odd numbers, where the fuel is often an
exact integer, mode 2 takes the longest trip allowed for the capacity."""

import random
import sys

LIMIT = 31999
RATIO = 5
ODD = 3 * 5 * 7 * 9


def main():
    seed, mode = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        m = ODD * rng.randint(1, (LIMIT - 1) // ODD)
        n = rng.randint(m + 1, min(LIMIT, RATIO * m))
    elif mode == 2:
        m = rng.randint(1, LIMIT // RATIO)
        n = RATIO * m
    else:
        m = rng.randint(1, LIMIT - 1)
        n = rng.randint(m + 1, min(LIMIT, RATIO * m))
    sys.stdout.write("%d %d\n" % (n, m))


if __name__ == "__main__":
    main()
