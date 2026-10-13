"""One dot from a seed and a mode: 1 anywhere with the smallest radius,
2 anywhere with a radius drawn log-uniformly from 1e-4 to 1, 3 on a random
side of the square with the smallest radius, 4 with x0 within 1e-6 of -1
or 1 (where asin is steepest), 5 with y0 within 1e-6 of -1 or 1 (the same
for acos), 6 a radius from 1 to 3 that covers much of the square."""

import math
import random
import sys

SMALLEST = 1e-4
NEAR = 1e-6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    x, y = rng.uniform(-1, 1), rng.uniform(-1, 1)
    eps = SMALLEST
    if mode == 2:
        eps = math.exp(rng.uniform(math.log(SMALLEST), 0))
    elif mode == 3:
        side = rng.randrange(4)
        if side < 2:
            x = (-1, 1)[side]
        else:
            y = (-1, 1)[side - 2]
    elif mode == 4:
        x = rng.choice((-1, 1)) * (1 - rng.uniform(0, NEAR))
    elif mode == 5:
        y = rng.choice((-1, 1)) * (1 - rng.uniform(0, NEAR))
    elif mode == 6:
        eps = rng.uniform(1, 3)
    print("%.10f %.10f" % (x, y))
    print("%.10f" % eps)


main()
