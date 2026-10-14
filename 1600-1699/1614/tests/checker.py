"""Checker: n lines of 2n stops each, numbers from 1 to 2n, such that every
two different stops are neighbours on some route."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    n = int(open(source).read().split()[0])
    stops = 2 * n
    lines = [line.split() for line in open(output).read().strip().split("\n")]
    if len(lines) != n:
        fail("expected %d routes, got %d" % (n, len(lines)))
    covered = set()
    for line in lines:
        if len(line) != stops or not all(t.isdigit() for t in line):
            fail("a route must list %d stops" % stops)
        route = [int(t) for t in line]
        if not all(1 <= x <= stops for x in route):
            fail("stops are numbered from 1 to %d" % stops)
        for a, b in zip(route, route[1:]):
            if a != b:
                covered.add((min(a, b), max(a, b)))
    need = n * (stops - 1)
    if len(covered) != need:
        fail("%d of the %d pairs of stops are neighbours on some route" % (len(covered), need))


main()
