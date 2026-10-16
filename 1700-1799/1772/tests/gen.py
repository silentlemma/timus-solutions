"""One test from a seed and a mode: mode 1 up to 9 lanes and 8 fallen
robots, mode 2 100 000 lanes and robots blocking random stretches,
mode 3 100 000 lanes and robots blocking all lanes but the first or
all but the last in turn, mode 4 100 000 lanes and robots blocking
short stretches."""

import random
import sys

FEW_LANES = 9
FEW_ROBOTS = 8
MOST = 100000
SHORT = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, FEW_LANES) if mode == 1 else MOST
    k = rng.randint(0, FEW_ROBOTS) if mode == 1 else MOST
    s = rng.randint(1, n)
    robots = []
    for i in range(k):
        if mode == 3:
            robots.append((2, n) if i % 2 == 0 else (1, n - 1))
            continue
        while True:
            lo = rng.randint(1, n)
            hi = min(n, lo + rng.randint(0, SHORT)) if mode == 4 else rng.randint(lo, n)
            if (lo, hi) != (1, n):
                break
        robots.append((lo, hi))
    lines = ["%d %d %d" % (n, s, k)] + ["%d %d" % r for r in robots]
    sys.stdout.write("\n".join(lines) + "\n")


main()
