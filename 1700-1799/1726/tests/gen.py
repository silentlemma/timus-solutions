"""One test from a seed and a mode: mode 1 a few houses on a small map,
mode 2 100000 houses anywhere, mode 3 100000 houses in the two far
corners, so that the sum of distances is as large as it gets, mode 4
100000 houses on one crossing, mode 5 100000 distinct houses on a shuffled
antidiagonal near the maximum coordinates."""

import random
import sys

LIMIT = 10 ** 6
MOST = 10 ** 5
FEW = 10
SMALL = 30


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, FEW)
        houses = [(rng.randint(1, SMALL), rng.randint(1, SMALL)) for _ in range(n)]
    elif mode == 2:
        houses = [(rng.randint(1, LIMIT), rng.randint(1, LIMIT)) for _ in range(MOST)]
    elif mode == 3:
        houses = [rng.choice(((1, 1), (LIMIT, LIMIT))) for _ in range(MOST)]
    elif mode == 5:
        houses = [(LIMIT - i, LIMIT - (MOST - 1 - i)) for i in range(MOST)]
        rng.shuffle(houses)
    else:
        spot = (rng.randint(1, LIMIT), rng.randint(1, LIMIT))
        houses = [spot] * MOST
    print(len(houses))
    print("\n".join("%d %d" % h for h in houses))


main()
