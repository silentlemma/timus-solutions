"""One test from a seed and a mode: mode 1 a small army, mode 2 the
largest army over the whole square, mode 3 the largest army with the
four parity classes as even as possible, mode 4 houses crowded in a small
square, mode 5 the largest army entirely in the negative even-x odd-y class,
mode 6 the largest army on the boundary of the coordinate square, mode 7
an almost maximal army on the parallel lines y = x - 1 and y = x + 1."""

import random
import sys

MOST_N = 5000
LIMIT = 10000
PER_PLACE = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        n = MOST_N - 1 if mode == 7 else MOST_N
        count = PER_PLACE * n
        if mode == 5:
            houses = set()
            while len(houses) < count:
                x = 2 * rng.randint(-LIMIT // 2, -1)
                y = 2 * rng.randint(-LIMIT // 2, -1) + 1
                houses.add((x, y))
            houses = sorted(houses)
            rng.shuffle(houses)
        elif mode == 6:
            houses = []
            for position in rng.sample(range(8 * LIMIT), count):
                side, offset = divmod(position, 2 * LIMIT)
                if side == 0:
                    point = (-LIMIT + offset, -LIMIT)
                elif side == 1:
                    point = (LIMIT, -LIMIT + offset)
                elif side == 2:
                    point = (LIMIT - offset, LIMIT)
                else:
                    point = (-LIMIT, LIMIT - offset)
                houses.append(point)
        else:
            houses = []
            for position in rng.sample(range(2 * (2 * LIMIT - 1)), count):
                offset, line = divmod(position, 2)
                x = -LIMIT + 1 + offset
                houses.append((x, x + (1 if line else -1)))
        print(n)
        for x, y in houses:
            print(x, y)
        return
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
