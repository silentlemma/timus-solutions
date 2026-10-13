"""Seeded vertex counts: SEED MODE.

Mode 1 chooses N uniformly from 11..24, exercising medium tree multisets.
Mode 2 chooses N uniformly from 27..41, exercising large exact counts.
"""

import random
import sys


def main():
    seed, mode = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randint(11, 24))
    elif mode == 2:
        print(rng.randint(27, 41))
    else:
        raise ValueError("mode must be 1 or 2")


if __name__ == "__main__":
    main()
