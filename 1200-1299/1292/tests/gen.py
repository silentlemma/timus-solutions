"""T queries: a seed and a mode. Mode 1 gives small N, so the chain is
often cut before 153, mode 2 any N, mode 3 33333 queries with the key
12558, the slowest to reach 153. Mode 4 sweeps every valid key at
N = 2; mode 5 mixes short chains at all lengths from 2 through 16 in
33333 queries with random keys. L is always below the gap,
which stops changing once it is 153."""

import random
import sys

LARGEST = 33333
SLOWEST = 12558
SHORT = 16
FIXED = 153


def cubes(x):
    return sum(int(c) ** 3 for c in str(x))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        t = LARGEST // 3
    elif mode == 5:
        t = LARGEST
    else:
        t = LARGEST if mode == 3 else rng.randint(2, 1000)
    print(t)
    for i in range(t):
        if mode == 4:
            n, k = 2, 3 * (i + 1)
        elif mode == 5:
            n = 2 + i % (SHORT - 1)
            k = 3 * rng.randint(1, LARGEST // 3)
        else:
            n = rng.randint(2, SHORT if mode == 1 else LARGEST)
            k = SLOWEST if mode == 3 else 3 * rng.randint(1, LARGEST // 3)
        gap = k
        for _ in range(n - 1):
            if gap == FIXED:
                break
            gap = cubes(gap)
        print(n, k, rng.randint(1, gap - 1))


main()
