"""One test from a seed and a mode: mode 1 is 100000 knights with random
ranges, mode 2 gives every gift to everyone at the largest amount, mode 3
uses single-knight ranges, mode 4 is small, mode 5 repeats overlapping broad
ranges at maximum size, and mode 6 uses random short ranges at maximum size."""

import random
import sys

LARGEST = 100000
SMALL = 10
RICHEST = 10000


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 4 else LARGEST
    lines = [str(n)]
    for _ in range(n + 1):
        if mode == 2:
            a, b, c = 1, n, RICHEST
        elif mode == 3:
            a = b = rng.randint(1, n)
            c = rng.randint(1, RICHEST)
        elif mode == 5:
            a, b = rng.choice(
                [(1, n // 2), (n // 4, n), (1, 3 * n // 4), (n // 4, 3 * n // 4)]
            )
            c = rng.randint(1, RICHEST)
        elif mode == 6:
            a = rng.randint(1, n)
            b = min(n, a + rng.randint(1, 8))
            c = rng.randint(1, RICHEST)
        else:
            a, b = sorted(rng.randint(1, n) for _ in range(2))
            c = rng.randint(1, RICHEST)
        lines.append("%d %d %d" % (a, b, c))
    print("\n".join(lines))


main()
