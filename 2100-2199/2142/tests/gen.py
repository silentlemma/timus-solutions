"""Lands and costs from a seed: mode 1 small random numbers, mode 2 large
random numbers, mode 3 costs exactly equal to the lands or one more."""

import random
import sys

SMALL = 6
TOP = 10 ** 9


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        lands = [rng.randint(0, SMALL) for _ in "abc"]
        costs = [rng.randint(0, SMALL) for _ in "xyz"]
    elif mode == 2:
        lands = [rng.randint(0, TOP) for _ in "abc"]
        costs = [rng.randint(0, TOP) for _ in "xyz"]
    else:
        a, b, c = (rng.randint(0, TOP - 1) for _ in "abc")
        x = rng.randint(0, min(a + c, TOP))
        y = rng.randint(0, min(b + (a + c - x), TOP))
        z = a + b + c - x - y + rng.randint(0, 1)
        lands, costs = [a, b, c], [x, y, min(z, TOP)]
    print(*lands)
    print(*costs)


main()
