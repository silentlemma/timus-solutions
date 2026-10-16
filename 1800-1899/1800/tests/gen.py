"""One test from a seed and a mode: mode 1 any length, height and speed
up to 1000, mode 2 a toast longer than twice the height, mode 3 a fast
spin from a large height, mode 4 a slow spin."""

import random
import sys

LIMIT = 1000
SLOW = 20


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    length, height, turns = (rng.randint(1, LIMIT) for _ in range(3))
    if mode == 2:
        length = rng.randint(2, LIMIT)
        height = rng.randint(1, length // 2)
    elif mode == 3:
        height = rng.randint(LIMIT // 2, LIMIT)
        turns = rng.randint(LIMIT // 2, LIMIT)
    elif mode == 4:
        turns = rng.randint(1, SLOW)
    print(length, height, turns)


main()
