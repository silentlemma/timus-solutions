"""Checker: N distinct fence cells listed around the region, each next to
the one before it (the last next to the first) by side or corner, that
shut the goat at (0, 0) into exactly K cells, with N as small as
possible: no K cells have fewer than sqrt(8 K - 4) + 2 neighbours."""

import math
import sys

STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    k = int(open(inp).read())
    got = open(output).read().split()
    if not got or not got[0].lstrip("-").isdigit():
        fail("no fence size")
    n = int(got[0])
    if n != math.isqrt(8 * k - 5) + 1 + 2:
        fail("fence of %d cells, the least is %d" % (n, math.isqrt(8 * k - 5) + 3))
    if len(got) != 1 + 2 * n:
        fail("expected %d coordinates" % (2 * n))
    cells = [(int(got[1 + 2 * i]), int(got[2 + 2 * i])) for i in range(n)]
    fence = set(cells)
    if len(fence) != n:
        fail("a fence cell is listed twice")
    for i in range(n):
        a, b = cells[i], cells[(i + 1) % n]
        if max(abs(a[0] - b[0]), abs(a[1] - b[1])) != 1:
            fail("cells %d and %d are not neighbours" % (i + 1, (i + 1) % n + 1))
    if (0, 0) in fence:
        fail("the goat stands on the fence")
    # cells outside the box of the fence are outside the region
    xs, ys = [c[0] for c in cells], [c[1] for c in cells]
    x_lo, x_hi, y_lo, y_hi = min(xs), max(xs), min(ys), max(ys)
    seen, stack = {(0, 0)}, [(0, 0)]
    while stack:
        x, y = stack.pop()
        if not (x_lo < x < x_hi and y_lo < y < y_hi):
            fail("the goat walks out")
        for dx, dy in STEPS:
            c = (x + dx, y + dy)
            if c not in fence and c not in seen:
                seen.add(c)
                stack.append(c)
    if len(seen) != k:
        fail("the goat gets %d cells instead of %d" % (len(seen), k))


if __name__ == "__main__":
    main()
