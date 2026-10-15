"""One test from a seed and a mode: mode 1 small parameters, mode 2 large
ones, mode 3 nearly a multiple of an orthogonal matrix (the two singular
values almost equal, where the textbook formula cancels), mode 4 a matrix
of rank one."""

import random
import sys

LARGEST = 10**6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        a1, b1, a2, b2 = (rng.randint(0, 10) for _ in range(4))
    elif mode == 2:
        a1, b1, a2, b2 = (rng.randint(0, LARGEST) for _ in range(4))
    elif mode == 3:
        big = rng.randint(LARGEST // 2, LARGEST)
        a1, b2 = big, big - rng.randint(0, 2)
        b1, a2 = rng.randint(0, 2), rng.randint(0, 2)
        if rng.random() < 0.5:
            a1, b1, a2, b2 = b1, a1, b2, a2
    else:
        a1, b1 = rng.randint(0, 1000), rng.randint(0, 1000)
        k = rng.randint(0, 1000)
        a2, b2 = a1 * k, b1 * k
    print(a1, b1)
    print(a2, b2)


main()
