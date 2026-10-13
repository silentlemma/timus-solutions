"""Checker: a 2^n by 2^n board with 0 at the given cell only and every
other number from 1 to (4^n - 1) / 3 on exactly three cells that form an
L inside a 2 by 2 square."""

import sys
from collections import defaultdict


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n, x, y = map(int, open(inp).read().split()[:3])
    size, pieces = 1 << n, (4**n - 1) // 3
    words = open(output).read().split()
    if len(words) != size * size:
        fail("expected %d numbers" % (size * size))
    cells = defaultdict(list)
    for k, w in enumerate(words):
        v = int(w)
        if v == 0:
            if divmod(k, size) != (x - 1, y - 1):
                fail("0 must stand only at the removed cell")
        elif not 1 <= v <= pieces:
            fail("piece number %d out of range" % v)
        else:
            cells[v].append(divmod(k, size))
    if int(words[(x - 1) * size + y - 1]) != 0:
        fail("the removed cell must hold 0")
    if len(cells) != pieces:
        fail("expected %d pieces" % pieces)
    for v, group in cells.items():
        rows = {r for r, _ in group}
        cols = {c for _, c in group}
        if (
            len(group) != 3
            or len(rows) != 2
            or len(cols) != 2
            or max(rows) - min(rows) != 1
            or max(cols) - min(cols) != 1
        ):
            fail("piece %d is not an L of three cells" % v)


main()
