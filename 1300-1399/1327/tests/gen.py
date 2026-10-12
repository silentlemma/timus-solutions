"""A seed and a mode, sampling two distinct days and printing them in order.

Mode 1: random endpoints from 1000 through 9000.
Mode 2: random three-digit endpoints from 100 through 999.
Mode 3: random endpoints near the upper limit, from 9900 through 9998.
"""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        low, high = 1000, 9000
    elif mode == 2:
        low, high = 100, 999
    elif mode == 3:
        low, high = 9900, 9998
    else:
        raise ValueError("mode must be 1, 2 or 3")
    a, b = sorted(rng.sample(range(low, high + 1), 2))
    sys.stdout.buffer.write(f"{a}\n{b}\n".encode("ascii"))


main()
