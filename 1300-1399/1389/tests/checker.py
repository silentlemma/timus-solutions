"""Checker: as many roads as the expected answer, each one a road of the
input written as there, listed in input order, no city on two of them."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    m = int(data[1])
    roads = {}
    for i in range(m):
        roads.setdefault((data[2 + 2 * i], data[3 + 2 * i]), i)
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit() or int(got[0]) != want:
        fail("expected %d roads" % want)
    if len(got) != 1 + 2 * want:
        fail("expected %d pairs of cities" % want)
    seen, last = set(), -1
    for k in range(want):
        pair = (got[1 + 2 * k], got[2 + 2 * k])
        if pair not in roads:
            fail("%s %s is not a road of the input as written" % pair)
        if roads[pair] <= last:
            fail("roads must follow the input order")
        last = roads[pair]
        if pair[0] in seen or pair[1] in seen:
            fail("a city has two closed roads")
        seen.update(pair)


main()
