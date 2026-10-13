"""One test from a seed and a mode. Mode 1 is small random cubes, mode 2 the
largest cube with random events, mode 3 piles +20000 into a few sectors so
that sums come close to 2^31, mode 4 asks boxes with the longest Fenwick walks."""

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


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
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
