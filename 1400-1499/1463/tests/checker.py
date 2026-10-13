"""Checker: the same joy as the reference, then the length of a route and
its cities: different cities, every two neighbours joined on the map, and
the joy of the cities and the flights adding up to the printed value."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n = data[0]
    joy = [0] + data[2 : 2 + n]
    link = {}
    rest = data[2 + n :]
    for a, b, c in zip(rest[0::3], rest[1::3], rest[2::3]):
        link[(a, b)] = link[(b, a)] = c
    want = int(open(expected).read().split()[0])
    got = [int(x) for x in open(output).read().split()]
    if len(got) < 2 or got[0] != want:
        fail("expected joy %d" % want)
    length, route = got[1], got[2:]
    if length != len(route) or length < 1:
        fail("the route length does not match its cities")
    if len(set(route)) != length or not all(1 <= v <= n for v in route):
        fail("the route must visit different cities")
    total = sum(joy[v] for v in route)
    for a, b in zip(route, route[1:]):
        if (a, b) not in link:
            fail("no flight between %d and %d" % (a, b))
        total += link[(a, b)]
    if total != want:
        fail("the route brings %d, not %d" % (total, want))


main()
