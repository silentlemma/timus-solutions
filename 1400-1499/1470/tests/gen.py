"""One test from a seed and a mode. Mode 1 is small random cubes, mode 2 the
largest cube with random events, mode 3 piles +20000 into a few sectors so
that sums come close to 2^31, mode 4 asks boxes with the longest Fenwick walks,
mode 5 repeatedly adds and removes objects in a sparse non-power-of-two cube."""

import random
import sys

RECORDS = 100000
LARGEST = 128
SMALL = 8
SMALL_RECORDS = 3000
SHIFT = 20000
LAST_ASKS = 100
CORNER_SHARE = 0.9
LONG_LOW, LONG_HIGH = 63, 126  # x1 = 63 and x2 + 1 = 127 both have many set bits


def sparse_changes(rng):
    n = LARGEST - 1
    boundaries = (0, 1, 7, 8, 63, 64, 125, 126)
    points = [tuple(rng.choice(boundaries) for _ in range(3)) for _ in range(16)]
    points += [tuple(rng.randrange(n) for _ in range(3)) for _ in range(16)]
    points = sorted(set(points))
    cells = dict.fromkeys(points, 0)
    lines = [str(n)]
    for step in range(RECORDS):
        cell = rng.choice(points)
        kind = step % 8
        if kind in (0, 1, 2, 5):
            if kind == 5:
                delta = -min(cells[cell], SHIFT)
            elif cells[cell] and rng.randrange(2):
                delta = -rng.randint(1, min(cells[cell], SHIFT))
            else:
                delta = rng.randint(0, SHIFT)
            cells[cell] += delta
            lines.append("1 %d %d %d %d" % (cell + (delta,)))
        else:
            if kind == 3:
                low, high = cell, cell
            elif kind == 4:
                low, high = [0, 0, 0], [n - 1, n - 1, n - 1]
                axis = rng.randrange(3)
                low[axis] = high[axis] = cell[axis]
            elif kind == 6:
                pairs = [sorted(rng.randrange(n) for _ in range(2)) for _ in range(3)]
                low = [pair[0] for pair in pairs]
                high = [pair[1] for pair in pairs]
            else:
                low, high = [0, 0, 0], [n - 1, n - 1, n - 1]
            lines.append("2 %d %d %d %d %d %d" % (*low, *high))
    lines.append("3")
    print("\n".join(lines))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        sparse_changes(rng)
        return
    n = rng.randint(1, SMALL) if mode == 1 else LARGEST
    total = SMALL_RECORDS if mode == 1 else RECORDS
    cells = {}
    lines = [str(n)]

    def box():
        x1, x2 = sorted(rng.randrange(n) for _ in range(2))
        y1, y2 = sorted(rng.randrange(n) for _ in range(2))
        z1, z2 = sorted(rng.randrange(n) for _ in range(2))
        return x1, y1, z1, x2, y2, z2

    for step in range(total):
        if mode == 3:
            if step < total - LAST_ASKS:
                corner = rng.random() < CORNER_SHARE
                cell = (0, 0, 0) if corner else (1, 1, 1)
                lines.append("1 %d %d %d %d" % (cell + (SHIFT,)))
            else:
                low = step % 2  # from 1 the partial sums go below -2^31
                lines.append("2 %d %d %d %d %d %d" % ((low,) * 3 + (n - 1,) * 3))
            continue
        if mode == 4:
            if step % 2 == 0:
                cell = tuple(rng.randint(LONG_LOW, LONG_HIGH) for _ in range(3))
                lines.append("1 %d %d %d %d" % (cell + (rng.randint(0, SHIFT),)))
            else:
                lines.append("2 %d %d %d %d %d %d" % ((LONG_LOW,) * 3 + (LONG_HIGH,) * 3))
            continue
        if rng.random() < 0.5:
            if cells and rng.random() < 0.3:
                cell = rng.choice(list(cells))
                k = -rng.randint(1, min(cells[cell], SHIFT))
            else:
                cell = (rng.randrange(n), rng.randrange(n), rng.randrange(n))
                k = rng.randint(0, SHIFT)
            cells[cell] = cells.get(cell, 0) + k
            if cells[cell] == 0:
                del cells[cell]
            lines.append("1 %d %d %d %d" % (cell + (k,)))
        else:
            lines.append("2 %d %d %d %d %d %d" % box())
    lines.append("3")
    print("\n".join(lines))


main()
