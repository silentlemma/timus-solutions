"""Print a from a seed: mode 1 random up to 10^18; mode 2 small up to 1000;
mode 3 near 10^18; mode 4 just above the signed 32-bit input limit;
mode 5 an odd integer between 2^53 and 2^54 that binary64 cannot represent.
"""

import random
import sys

TOP = 10 ** 18
SMALL = 1000
NEAR = 10 ** 6


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        a = rng.randint(1, TOP)
    elif mode == 2:
        a = rng.randint(1, SMALL)
    elif mode == 3:
        a = TOP - rng.randint(0, NEAR)
    elif mode == 4:
        a = 2 ** 31 + rng.randint(0, NEAR)
    elif mode == 5:
        a = 2 ** 53 + 2 * rng.randrange(2 ** 52) + 1
    else:
        raise ValueError("mode must be between 1 and 5")
    print(a)


main()
