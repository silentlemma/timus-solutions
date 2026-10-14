"""One test from a seed and a mode: sorted coat sizes.

Mode 1: 100000 random sizes up to 10^9.
Mode 2: many equal sizes with R = 0.
Mode 3: sizes in steps of exactly R.
Mode 4: a few coats.
Mode 5: 100000 distinct sizes with R = 0, including both size limits.
Mode 6: 100000 distinct sizes with R = 10^9 - 1, all mutually incompatible.
Mode 7: 100000 coats in random clusters with gaps of R and R + 1.
"""

import random
import sys

COATS = 100000
TOP = 10**9
FEW = 8


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 4 else COATS
    if mode == 2:
        r = 0
        sizes = [rng.randint(0, 50) for _ in range(n)]
    elif mode == 3:
        r = rng.randint(1, 1000)
        sizes = [r * rng.randint(0, 1000) for _ in range(n)]
    elif mode == 4:
        r = rng.randint(0, 5)
        sizes = [rng.randint(0, 20) for _ in range(n)]
    elif mode == 5:
        r = 0
        sizes = [0, TOP] + rng.sample(range(1, TOP), n - 2)
    elif mode == 6:
        r = TOP - 1
        sizes = rng.sample(range(1, TOP + 1), n)
    elif mode == 7:
        r = rng.randint(5, 50)
        sizes = [0, TOP] + [
            rng.randrange(200) * (4 * r + 4) + rng.choice([0, r, r + 1, 2 * r + 1])
            for _ in range(n - 2)
        ]
    else:
        r = rng.randint(0, TOP // 1000)
        sizes = [rng.randint(0, TOP) for _ in range(n)]
    sizes.sort()
    print(n, r)
    print(*sizes)


main()
