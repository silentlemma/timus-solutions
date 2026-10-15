"""One test from a seed and a mode: mode 1 small numbers, mode 2 numbers
up to 10^18, mode 3 y close to x, so that many separate intervals come
before they join, mode 4 x = y."""

import random
import sys

LIMIT = 10 ** 18
SMALL = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 1 else LIMIT
    x = rng.randint(1, top)
    if mode == 3:
        x = rng.randint(LIMIT // 2, LIMIT)
        y = x + rng.randint(0, 10)
    elif mode == 4:
        y = x
    else:
        y = rng.randint(x, top)
    y = min(y, LIMIT)
    low = rng.randint(1, top)
    high = rng.randint(low, top)
    print(x, y, low, high)


main()
