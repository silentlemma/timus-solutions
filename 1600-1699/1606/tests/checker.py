"""Checker: the largest number of flags and a list of that many distinct
flags with falling y, turning at every flag: the x steps between
consecutive flags alternate in direction. Any such list is accepted."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    pts = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not all(w.isdigit() for w in got):
        fail("expected numbers")
    count, order = int(got[0]), [int(w) for w in got[1:]]
    if count != want:
        fail("%d flags instead of %d" % (count, want))
    if len(order) != count or len(set(order)) != count or not all(1 <= f <= n for f in order):
        fail("bad list of flags")
    path = [pts[f - 1] for f in order]
    for a, b in zip(path, path[1:]):
        if b[1] >= a[1]:
            fail("the skier must go down")
    for a, b, c in zip(path, path[1:], path[2:]):
        if (b[0] - a[0] > 0) == (c[0] - b[0] > 0):
            fail("no turn at a flag")


main()
