"""Checker: the height must equal the expected one, or both answers must be
-1. The route must list as many roads as it claims, lead from s to f
road by road, pay at most b tolls, take at most t minutes and use no road
higher than the answer."""

import sys

FIELDS = 5


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = list(map(int, open(source).read().split()))
    n, m, s, f, budget, limit = data[:6]
    roads = [data[6 + FIELDS * i : 6 + FIELDS * (i + 1)] for i in range(m)]
    want = int(open(expected).read().split()[0])
    try:
        values = [int(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if not values or values[0] != want:
        fail("height %s, expected %d" % (values[:1], want))
    if want == -1:
        if len(values) != 1:
            fail("nothing may follow -1")
        return
    if len(values) < 2 or len(values) != 2 + values[1]:
        fail("the route length does not match the roads listed")
    city, paid, time = s, 0, 0
    for idx in values[2:]:
        if not 1 <= idx <= m:
            fail("no road %d" % idx)
        u, v, c, t, h = roads[idx - 1]
        if u != city:
            fail("road %d does not start in city %d" % (idx, city))
        if h > want:
            fail("road %d is higher than %d" % (idx, want))
        city, paid, time = v, paid + c, time + t
    if city != f:
        fail("the route ends in city %d, not %d" % (city, f))
    if paid > budget or time > limit:
        fail("the route costs %d tolls and %d minutes" % (paid, time))


main()
