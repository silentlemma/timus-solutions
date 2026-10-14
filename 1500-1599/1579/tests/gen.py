"""One test from a seed and a mode: sorted coat sizes. Mode 1 is 100000
random sizes up to 10^9, mode 2 many equal sizes with R = 0, mode 3
sizes in steps of exactly R, mode 4 a few coats."""

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
    else:
        r = rng.randint(0, TOP // 1000)
        sizes = [rng.randint(0, TOP) for _ in range(n)]
    sizes.sort()
    print(n, r)
    print(*sizes)


main()
