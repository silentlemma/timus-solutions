"""One landing: a seed and a mode. Mode 1 draws h, d and alpha anywhere in
their ranges; mode 2 takes a narrow cone; mode 3 puts h just above a
multiple of d, so that almost a whole move of height must be lost."""

import random
import sys

SCALE = 10000


def draw(rng, lo, hi):
    return rng.randint(round(lo * SCALE), round(hi * SCALE)) / SCALE


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    d = draw(rng, 1, 5)
    if mode == 1:
        h, alpha = draw(rng, 0.5, 99.9999), draw(rng, 0.1, 2)
    elif mode == 2:
        h, alpha = draw(rng, 0.5, 99.9999), draw(rng, 0.1, 0.3)
    else:
        alpha = draw(rng, 0.1, 2)
        moves = rng.randint(1, int(99.9999 / d) - 1)
        h = moves * d + draw(rng, 0.0001, 0.05)
    sys.stdout.write("%.4f %.4f %.4f\n" % (h, d, alpha))


if __name__ == "__main__":
    main()
