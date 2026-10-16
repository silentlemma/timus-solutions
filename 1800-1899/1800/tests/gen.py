"""One test from a seed and a mode: mode 1 any length, height and speed
up to 1000, mode 2 a toast at least twice the height, mode 3 a fast
spin from a large height, mode 4 a slow spin."""

from math import isqrt
import random
import sys

LIMIT = 1000
SLOW = 20
GRAVITY = 981


def upright(length, height, turns):
    # At upright contact t = 15*n/turns for a positive odd integer n.
    square, remainder = divmod((2 * height - length) * turns * turns,
                               GRAVITY * 15 * 15)
    if remainder or square <= 0:
        return False
    n = isqrt(square)
    return n * n == square and n % 2 == 1


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        length, height, turns = (rng.randint(1, LIMIT) for _ in range(3))
        if mode == 2:
            length = rng.randint(2, LIMIT)
            height = rng.randint(1, length // 2)
        elif mode == 3:
            height = rng.randint(LIMIT // 2, LIMIT)
            turns = rng.randint(LIMIT // 2, LIMIT)
        elif mode == 4:
            turns = rng.randint(1, SLOW)
        if not upright(length, height, turns):
            break
    print(length, height, turns)


main()
