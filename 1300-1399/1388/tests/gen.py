"""Trees on both banks: a seed and a mode. Mode 1 is 100 000 random trees,
mode 2 a bank and its image under the shear (x, y) -> (x + y, y), mode 3
its image under a map that sends one direction of the run to the river,
mode 4 few directions with many trees hidden behind others, mode 5 two
rows of trees in arithmetic progression, mode 6 a matching run in a narrow
sector on each bank with random trees in all other directions."""

import random
import sys
from math import gcd

TOP = 20000
TREES = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    trees = set()
    if mode == 1:
        while len(trees) < TREES:
            x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
            if y:
                trees.add((x, y))
    elif mode in (2, 3, 6):
        half = TOP // 2 if mode == 2 else TOP // 3
        upper = set()
        while len(upper) < (TREES // 2 if mode != 6 else TREES // 8):
            y = rng.randint(1, half)
            # mode 6 keeps 0 <= x / y <= 1, so the image lies in 1 <= x / y <= 2
            upper.add((rng.randint(0, y) if mode == 6 else rng.randint(-half, half), y))
        a, b, c, d = (2, 1, 1, 1) if mode == 3 else (1, 1, 0, 1)
        for x, y in upper:
            u, v = a * x + b * y, c * x + d * y
            if v > 0:
                u, v = -u, -v
            if v < 0:
                trees.add((u, v))
        trees |= upper
        if mode == 6:
            while len(trees) < TREES:
                x, y = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
                if y and not -y <= 2 * x * (1 if y > 0 else -1) <= 5 * abs(y):
                    trees.add((x, y))
    elif mode == 4:
        rays = set()
        while len(rays) < 300:
            x, y = rng.randint(-30, 30), rng.choice((-1, 1)) * rng.randint(1, 30)
            g = gcd(x, y)
            rays.add((x // g, y // g))
        rays = sorted(rays)
        while len(trees) < TREES:
            x, y = rng.choice(rays)
            k = rng.randint(1, TOP // 30)
            trees.add((k * x, k * y))
    else:
        for i in range(-TOP, TOP + 1, 1):
            trees.add((i, 1))
        for i in range(-TOP + 1, TOP, 2):
            trees.add((i, -3))
    trees = list(trees)
    rng.shuffle(trees)
    print("\n".join("%d %d" % t for t in trees))
    print("0 0")


main()
