"""Checker: when the expected answer is 0 the output must be 0 too.
Otherwise the output gives three centres, in the order of the radii,
and every plate must lie on the tray and no two may overlap. The
coordinates are printed with four decimals, so a small tolerance is
allowed."""

import math
import sys

TOL = 1e-3
PLATES = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    h, w, *radii = map(int, open(inp).read().split())
    expected = open(ans).read().split()
    got = open(output).read().split()
    if expected == ["0"]:
        if got != ["0"]:
            fail("expected 0")
        return
    if got == ["0"]:
        fail("a placement exists")
    if len(got) != 2 * PLATES:
        fail("expected six numbers")
    centres = [(float(got[2 * i]), float(got[2 * i + 1])) for i in range(PLATES)]
    tol = TOL + 1e-9 * (h + w)
    for (x, y), r in zip(centres, radii):
        if not (r - tol <= x <= h - r + tol and r - tol <= y <= w - r + tol):
            fail("a plate of radius %d sticks out of the tray" % r)
    for i in range(PLATES):
        for j in range(i):
            gap = math.dist(centres[i], centres[j]) - radii[i] - radii[j]
            if gap < -tol:
                fail("plates %d and %d overlap by %.6f" % (j + 1, i + 1, -gap))


if __name__ == "__main__":
    main()
