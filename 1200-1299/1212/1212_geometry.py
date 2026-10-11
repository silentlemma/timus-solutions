import sys
from collections import namedtuple

# the cells a ship may not use: rows top..bottom, columns left..right
Zone = namedtuple("Zone", "top bottom left right")


def count_lines(rows, cols, zones, k):
    """Places for a ship lying along the rows of a rows x cols board."""
    edges = {z.top for z in zones} | {z.bottom + 1 for z in zones}
    cuts = sorted({1, rows + 1} | {e for e in edges if 1 < e <= rows})
    total = 0
    # rows between two cuts meet the same zones, so they count the same
    for top, below in zip(cuts, cuts[1:]):
        spans = sorted((z.left, z.right) for z in zones if z.top <= top <= z.bottom)
        free, start = 0, 1
        for left, right in spans + [(cols + 1, cols + 1)]:
            if left > start:
                free += max(0, left - start - k + 1)
            start = max(start, right + 1)
        total += free * (below - top)
    return total


def main():
    it = iter(sys.stdin.read().split())
    n, m, ships = int(next(it)), int(next(it)), int(next(it))
    zones = []
    for _ in range(ships):
        col, row, size, way = int(next(it)), int(next(it)), int(next(it)), next(it)
        bottom, right = (row + size - 1, col) if way == "V" else (row, col + size - 1)
        # no other ship may touch this one, even at a corner
        zones.append(Zone(row - 1, bottom + 1, col - 1, right + 1))
    k = int(next(it))
    total = count_lines(n, m, zones, k)
    if k > 1:
        flipped = [Zone(z.left, z.right, z.top, z.bottom) for z in zones]
        total += count_lines(m, n, flipped, k)
    print(total)


main()
