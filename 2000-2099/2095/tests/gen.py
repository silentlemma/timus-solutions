"""A vacation [l; r] from a seed: mode 1 within the first thousand days, mode 2
anywhere up to 10^9, mode 3 a short vacation near 10^9."""

import random
import sys

SMALL = 1000
TOP = 10 ** 9
SHORT = 100


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 3:
        left = rng.randint(TOP - SHORT, TOP)
        right = rng.randint(left, TOP)
    else:
        top = SMALL if mode == 1 else TOP
        left, right = sorted(rng.randint(1, top) for _ in range(2))
    print(left, right)


main()
