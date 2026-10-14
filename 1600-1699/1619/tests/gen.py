"""One test from a seed and a mode:
1: 2004 random pairs; 2: 2004 nearly equal pairs; 3: a few small pairs;
4: 2004 pairs with a fixed combined total of 10000;
5: 2004 pairs with both amounts large and the elder never behind at the end;
6: 2004 pairs with probabilities just below, exactly at, or just above one half.
"""

import random
import sys

CASES = 2004
TOP = 10**4


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    for _ in range(rng.randint(1, 50) if mode == 3 else CASES):
        if mode == 1:
            k, m = rng.randint(0, TOP), rng.randint(0, TOP)
        elif mode == 2:
            k = rng.randint(0, TOP)
            m = max(0, min(TOP, k + rng.randint(-3, 1)))
        elif mode == 4:
            k = rng.randint(0, TOP)
            m = TOP - k
        elif mode == 5:
            k = rng.randint(7500, TOP)
            m = rng.randint(7500, k)
        elif mode == 6:
            k = 2 * rng.randint(3000, 4999) + 1
            m = (k + 1) // 2 + rng.randint(-1, 1)
        else:
            k, m = rng.randint(0, 10), rng.randint(0, 10)
        lines.append("%d %d" % (k, m))
    print(len(lines))
    print("\n".join(lines))


main()
