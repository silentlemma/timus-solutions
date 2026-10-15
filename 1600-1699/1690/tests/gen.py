"""One test from a seed and a mode: mode 1 a small army, mode 2 the
largest army over the whole square, mode 3 the largest army with the
four parity classes as even as possible, mode 4 houses crowded in a small
square."""

import random
import sys

MOST_N = 5000
LIMIT = 10000
PER_PLACE = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 5) if mode == 1 else MOST_N
    count = PER_PLACE * n
    top = 6 if mode == 1 else (150 if mode == 4 else LIMIT)
    houses = set()
    if mode == 3:
        # the classes (0,0), (0,1), (1,0), (1,1) in turn
        k = 0
        while len(houses) < count:
            x = 2 * rng.randint(-LIMIT // 2, LIMIT // 2 - 1) + k // 2
            y = 2 * rng.randint(-LIMIT // 2, LIMIT // 2 - 1) + k % 2
            if (x, y) not in houses:
                houses.add((x, y))
                k = (k + 1) % 4
    else:
        while len(houses) < count:
            houses.add((rng.randint(-top, top), rng.randint(-top, top)))
    houses = list(houses)
    rng.shuffle(houses)
    print(n)
    for x, y in houses:
        print(x, y)


main()
