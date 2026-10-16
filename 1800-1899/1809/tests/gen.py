"""One test from a seed and a mode: four distinct cells. Mode 1 anywhere
on the board, mode 2 inside a 4 x 4 corner, so that many share lines,
mode 3 all on one row or column, mode 4 a valid layout with one potato
moved at random."""

import random
import sys

SIDE = 20
COUNT = 4
CORNER = 4


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    cells = set()
    while len(cells) < COUNT:
        if mode == 1:
            cells.add((rng.randint(1, SIDE), rng.randint(1, SIDE)))
        elif mode == 2:
            cells.add((rng.randint(1, CORNER), rng.randint(1, CORNER)))
        elif mode == 3:
            line = rng.randint(1, SIDE)
            cells = {(line, y) for y in rng.sample(range(1, SIDE + 1), COUNT)}
        else:
            x, y = rng.randint(1, SIDE - 1), rng.randint(1, SIDE - 1)
            cells = {(x, y), (x + 1, y)}
            while len(cells) < COUNT:
                a, b = rng.randint(1, SIDE), rng.randint(1, SIDE - 1)
                if all(a != cx and b != cy and b + 1 != cy for cx, cy in cells):
                    cells |= {(a, b), (a, b + 1)}
            cells = list(cells)
            cells[rng.randrange(COUNT)] = (rng.randint(1, SIDE), rng.randint(1, SIDE))
            cells = set(cells)
    cells = list(cells)
    rng.shuffle(cells)
    print("\n".join("%d %d" % c for c in cells))


main()
