"""Checker: the expected number of gluings, then the first order, each
next order made from the one before by one split and glue, and the cars
in order at the end. An order comes from the one before by a split and
glue exactly when the old places of its cars rise in at most two runs."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    start = [int(v) for v in data[1 : 1 + n]]
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not words or not words[0].lstrip("-").isdigit() or int(words[0]) != want:
        fail("the number of gluings is not %d" % want)
    if len(words) != 1 + (want + 1) * n or not all(w.isdigit() for w in words[1:]):
        fail("expected %d orders of %d cars" % (want + 1, n))
    orders = [[int(w) for w in words[1 + i * n : 1 + (i + 1) * n]] for i in range(want + 1)]
    if orders[0] != start:
        fail("the first order is not the given one")
    if orders[-1] != list(range(1, n + 1)):
        fail("the cars are not in order at the end")
    for step in range(want):
        before, after = orders[step], orders[step + 1]
        if sorted(after) != list(range(1, n + 1)):
            fail("order %d is not a permutation" % (step + 2))
        where = {car: i for i, car in enumerate(before)}
        places = [where[car] for car in after]
        drops = sum(places[i + 1] < places[i] for i in range(n - 1))
        if drops > 1:
            fail("order %d does not come from one split and glue" % (step + 2))


main()
