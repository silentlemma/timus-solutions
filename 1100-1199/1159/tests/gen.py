"""Fence blocks: a seed, N and a mode. Mode 0 draws lengths from 1 to 100,
mode 1 makes all blocks equal, mode 2 adds one block almost as long as
all the others together, so that the centre of the circle lies outside,
mode 3 adds one block longer than all the others together."""

import random
import sys

TOP = 100


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        sides = [rng.randint(1, TOP)] * n
    else:
        sides = [rng.randint(1, TOP) for _ in range(n)]
        if mode in (2, 3):
            others = sides[1:]
            small = [rng.randint(1, 2) for _ in others]
            sides = [min(TOP, sum(small) - 1 if mode == 2 else sum(small) + 1)] + small
    rng.shuffle(sides)
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(map(str, sides))))


if __name__ == "__main__":
    main()
