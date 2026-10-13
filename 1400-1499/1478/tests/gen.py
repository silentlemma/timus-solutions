"""One input from a seed and a mode, always with different objects in a
test. Mode 1 is one test of 629 random objects, mode 2 is 1000 tests of 5
objects with small coordinates (many equal distances), mode 3 is one test
of nested clusters, mode 4 is a 25 x 25 grid, mode 5 is a few dozen small
random tests."""

import random
import sys

REACH = 10000
LARGEST = 629  # the largest N with N^3 within 250 000 000
SMALL_TESTS = 1000
SMALL = 5
NEAR = 4
GRID = 25
FEW = 40
LEVELS = 4  # mode 3: clusters of clusters, each level 8 times wider
SPREAD = 8


def distinct(rng, count, reach):
    points = set()
    while len(points) < min(count, (2 * reach + 1) ** 2):
        points.add((rng.randint(-reach, reach), rng.randint(-reach, reach)))
    return list(points)


def clusters(rng):
    centres = [(0, 0)]
    size = REACH // SPREAD**LEVELS
    for level in range(LEVELS):
        step = size * SPREAD ** (LEVELS - level)
        centres = [
            (x + rng.randint(-step, step) // 2, y + rng.randint(-step, step) // 2)
            for x, y in centres
            for _ in range(rng.randint(2, 4))
        ]
    points = set()
    while len(points) < LARGEST:
        x, y = rng.choice(centres)
        points.add((x + rng.randint(-size, size), y + rng.randint(-size, size)))
    return list(points)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        tests = [distinct(rng, LARGEST, REACH)]
    elif mode == 2:
        tests = [distinct(rng, SMALL, NEAR) for _ in range(SMALL_TESTS)]
    elif mode == 3:
        tests = [clusters(rng)]
    elif mode == 4:
        tests = [[(x, y) for x in range(GRID) for y in range(GRID)]]
        rng.shuffle(tests[0])
    else:
        tests = [distinct(rng, rng.randint(1, 30), rng.choice([2, 5, 50])) for _ in range(FEW)]
    blocks = ["%d\n%s" % (len(t), "\n".join("%d %d" % p for p in t)) for t in tests]
    print("\n\n".join(blocks + ["0"]))


main()
