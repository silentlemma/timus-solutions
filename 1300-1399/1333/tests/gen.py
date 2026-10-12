"""Ten bombs: a seed and a mode. Mode 1 gives random bombs, mode 2 small
bombs, mode 3 bombs near the corners and edges that reach outside the
square, mode 4 nested and repeated bombs."""

import random
import sys

N = 10
SMALL = 0.1  # the largest radius in mode 2


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    bombs = []
    for _ in range(N):
        if mode == 2:
            bombs.append((rng.random(), rng.random(), rng.uniform(0, SMALL)))
        elif mode == 3:
            bombs.append((rng.choice([0, 1, rng.random()]), rng.choice([0, 1]), rng.random()))
        elif mode == 4 and bombs:
            x, y, r = rng.choice(bombs)
            bombs.append((x, y, r * rng.choice([1, rng.random()])))
        else:
            bombs.append((rng.random(), rng.random(), rng.random()))
    print(N)
    for x, y, r in bombs:
        print("%.6f %.6f %.6f" % (x, y, r))


main()
