"""One test from a seed and a mode, N = 50000 unless small. Mode 1 spreads
the trees over the whole square, mode 2 puts them on one vertical line,
mode 3 on one horizontal line, mode 4 crowds them into distinct points of
a 301 x 301 square, mode 5 puts them on a coarse lattice, so many
triangles tie, mode 6 is small, mode 7 repeats a few spread points many
times. Mode 8 repeats each point of a rectangular lattice exactly twice,
mode 9 interleaves two vertical columns with offset heights, and mode 10
spreads 64 distinct trees over the whole square. Modes 1 to 4, 9 and 10
keep the points distinct. Arguments: seed mode."""

import random
import sys

LARGEST = 50000
REACH = 10**6
CROWD = 150
STEP = 1000
SMALL = 8


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(3, SMALL) if mode == 6 else LARGEST
    if mode == 8:
        pts = [(STEP * (i % 250 - 125), STEP * (i // 250 - 50))
               for i in range(n // 2) for _ in range(2)]
        rng.shuffle(pts)
    elif mode == 9:
        rows = range(-249999, 250000)
        pts = [(-1, 4 * y) for y in rng.sample(rows, n // 2)]
        pts += [(1, 4 * y + 1) for y in rng.sample(rows, n // 2)]
        rng.shuffle(pts)
    elif mode == 10:
        n = 64
        pts = rng.sample(range((2 * REACH + 1) ** 2), n)
        pts = [(p % (2 * REACH + 1) - REACH, p // (2 * REACH + 1) - REACH)
               for p in pts]
    elif mode == 2:
        pts = [(0, y) for y in rng.sample(range(-REACH, REACH + 1), n)]
    elif mode == 3:
        pts = [(x, -REACH) for x in rng.sample(range(-REACH, REACH + 1), n)]
    elif mode == 4:
        side = 2 * CROWD + 1
        pts = [(c % side - CROWD, c // side - CROWD) for c in rng.sample(range(side * side), n)]
    elif mode == 5:
        cells = REACH // STEP
        pts = [
            (STEP * rng.randint(-cells, cells), STEP * rng.randint(-cells, cells)) for _ in range(n)
        ]
    elif mode == 7:
        spots = [(rng.randint(-REACH, REACH), rng.randint(-REACH, REACH)) for _ in range(SMALL)]
        pts = [rng.choice(spots) for _ in range(n)]
    else:
        spread = set()
        while len(spread) < n:
            spread.add((rng.randint(-REACH, REACH), rng.randint(-REACH, REACH)))
        pts = list(spread)
        rng.shuffle(pts)
    print(n)
    print("\n".join("%d %d" % p for p in pts))


main()
