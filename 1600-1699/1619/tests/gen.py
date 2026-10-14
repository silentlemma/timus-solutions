"""One test from a seed and a mode: mode 1 the most cases with random sums,
mode 2 the most cases with sums close to each other, mode 3 small sums."""

import random
import sys

CASES = 2004
TOP = 10**4


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    for _ in range(CASES if mode < 3 else rng.randint(1, 50)):
        if mode == 1:
            k, m = rng.randint(0, TOP), rng.randint(0, TOP)
        elif mode == 2:
            k = rng.randint(0, TOP)
            m = max(0, min(TOP, k + rng.randint(-3, 1)))
        else:
            k, m = rng.randint(0, 10), rng.randint(0, 10)
        lines.append("%d %d" % (k, m))
    print(len(lines))
    print("\n".join(lines))


main()
