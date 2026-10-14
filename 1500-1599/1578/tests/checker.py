"""Checker: YES and an order of all points in which every turn is acute,
that is, the two segments at each inner point make an angle below 90
degrees, 0 included."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    total = int(data[0]) + 2
    pts = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(total)]
    got = open(output).read().split()
    if not got or got[0] != "YES":
        fail("expected YES")
    if len(got) != 1 + total or not all(w.isdigit() for w in got[1:]):
        fail("expected %d point numbers" % total)
    order = [int(w) - 1 for w in got[1:]]
    if sorted(order) != list(range(total)):
        fail("not every point once")
    for i in range(1, total - 1):
        a, b, c = pts[order[i - 1]], pts[order[i]], pts[order[i + 1]]
        dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
        if dot <= 0:
            fail("the turn at point %d is not acute" % (order[i] + 1))


main()
