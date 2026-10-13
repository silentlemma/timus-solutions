"""Checker: the size must equal the expected largest one; for a positive
size, two different top-left corners inside the matrix whose squares are
equal letter by letter."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2 : 2 + n]
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if not got or got[0] != want:
        fail("expected size %d" % want)
    if want == 0:
        if len(got) != 1:
            fail("only 0 is expected")
        return
    if len(got) != 5:
        fail("expected the size and two corners")
    k = want
    r1, c1, r2, c2 = got[1:]
    for r, c in ((r1, c1), (r2, c2)):
        if not (1 <= r <= n - k + 1 and 1 <= c <= m - k + 1):
            fail("a square leaves the matrix")
    if (r1, c1) == (r2, c2):
        fail("the squares coincide")
    for t in range(k):
        if grid[r1 - 1 + t][c1 - 1 : c1 - 1 + k] != grid[r2 - 1 + t][c2 - 1 : c2 - 1 + k]:
            fail("the squares differ")


main()
