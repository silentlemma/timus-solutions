"""A park: a seed and a mode. Mode 1 scatters 100 trees in a large park;
mode 2 puts them on a coarse grid, so many squares tie; mode 3 crowds them
into a small park."""

import random
import sys

TREES = 100
BIG = 10000
GRID = 10
SMALL = 30


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        w, h = rng.randint(BIG // 2, BIG), rng.randint(BIG // 2, BIG)
        cells = set()
        while len(cells) < TREES:
            cells.add((rng.randint(0, w), rng.randint(0, h)))
    elif mode == 2:
        w, h = BIG, rng.randint(BIG // 2, BIG)
        cells = {(i * w // GRID, j * h // GRID) for i in range(GRID) for j in range(GRID)}
    else:
        w, h = rng.randint(SMALL // 2, SMALL), rng.randint(SMALL // 2, SMALL)
        cells = set()
        while len(cells) < TREES:
            cells.add((rng.randint(0, w), rng.randint(0, h)))
    trees = sorted(cells)
    rng.shuffle(trees)
    lines = ["%d %d %d" % (len(trees), w, h)] + ["%d %d" % t for t in trees]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
