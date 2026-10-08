"""Checker: the route starts and ends at the given cells, every step rolls the
cube to a side neighbour on the board, and the sum of the bottom faces along
the route equals both the printed sum and the minimal one."""

import sys

from gen import BOTTOM, ROLLS, SIZE, cell, roll


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    start, end, values = data[0], data[1], [int(v) for v in data[2:]]
    best = int(open(expected).read().split()[0])
    out = open(output).read().split()
    if len(out) < 2 or not out[0].lstrip("-").isdigit():
        fail("expected a sum and a route")
    total, route = int(out[0]), out[1:]
    if route[0] != start or route[-1] != end:
        fail("the route must go from %s to %s" % (start, end))
    faces = tuple(range(len(values)))
    real = values[faces[BOTTOM]]
    prev = None
    for name in route:
        x, y = cell(name) if len(name) == 2 and name[1].isdigit() else (-1, -1)
        if not (0 <= x < SIZE and 0 <= y < SIZE):
            fail("%r is not a cell" % name)
        if prev is not None:
            step = (x - prev[0], y - prev[1])
            if step not in ROLLS:
                fail("%s does not touch the previous cell" % name)
            faces = roll(faces, step)
            real += values[faces[BOTTOM]]
        prev = (x, y)
    if real != total:
        fail("the route sums to %d, not %d" % (real, total))
    if total != best:
        fail("sum %d, the minimum is %d" % (total, best))


main()
