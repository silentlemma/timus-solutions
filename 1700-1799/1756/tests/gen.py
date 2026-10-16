"""One test from a seed and a mode: mode 1 small random numbers, mode 2
random numbers up to 10000, mode 3 all three numbers at 10000 or close."""

import random
import sys

FEW = 20
MOST = 10000
NEAR = 10


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, FEW) for _ in range(3)]
    elif mode == 2:
        values = [rng.randint(1, MOST) for _ in range(3)]
    else:
        values = [rng.randint(MOST - NEAR, MOST) for _ in range(3)]
    print(*values)


main()
