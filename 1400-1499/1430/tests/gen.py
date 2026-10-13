"""Purchase inputs: a seed and a mode.

Mode 1: random prices from 2 to 100 and a budget from 1 to 500.
Mode 2: random prices from 300000000 to 800000000 and a budget
from 1900000000 to 2000000000, allowing only a few purchases.
"""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        a, b = (rng.randint(2, 100) for _ in range(2))
        n = rng.randint(1, 500)
    elif mode == 2:
        a, b = (rng.randint(300_000_000, 800_000_000) for _ in range(2))
        n = rng.randint(1_900_000_000, 2_000_000_000)
    else:
        raise ValueError("mode must be 1 or 2")
    print(a, b, n)


if __name__ == "__main__":
    main()
