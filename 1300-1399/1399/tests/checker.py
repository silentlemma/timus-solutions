"""Checker: a valid plan, every item delivered once, no trip over the
capacity, every trip a route from the depot back to it through the clients
of its items, the stated loads and lengths right, and a total no longer than
the expected one."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    m, n, cap = data[:3]
    pos = 3
    dist = [data[pos + i * (m + 1) : pos + (i + 1) * (m + 1)] for i in range(m + 1)]
    pos += (m + 1) ** 2
    weight = [data[pos + 2 * i] for i in range(n)]
    client = [data[pos + 2 * i + 1] for i in range(n)]
    want = int(open(expected).read().split()[-1])
    lines = [line.split() for line in open(output).read().splitlines()]
    lines = [line for line in lines if line]
    try:
        trips = int(lines[0][0])
        if len(lines) != 2 + 4 * trips:
            fail("expected %d blocks of four lines and a total" % trips)
        seen, total = set(), 0
        for t in range(trips):
            items, load, route, length = lines[1 + 4 * t : 5 + 4 * t]
            items = [int(x) for x in items]
            route = [int(x) for x in route]
            if (
                any(not 1 <= i <= n for i in items)
                or seen & set(items)
                or len(set(items)) != len(items)
            ):
                fail("trip %d: bad or repeated items" % (t + 1))
            seen |= set(items)
            mass = sum(weight[i - 1] for i in items)
            if mass != int(load[0]) or mass > cap:
                fail("trip %d: load %d, stated %s, capacity %d" % (t + 1, mass, load[0], cap))
            if len(route) < 3 or route[0] != 0 or route[-1] != 0 or 0 in route[1:-1]:
                fail("trip %d: the route must start and end at the depot only" % (t + 1))
            if any(not 1 <= c <= m for c in route[1:-1]):
                fail("trip %d: unknown client in the route" % (t + 1))
            if not {client[i - 1] for i in items} <= set(route):
                fail("trip %d: the route misses a client" % (t + 1))
            walk = sum(dist[a][b] for a, b in zip(route, route[1:]))
            if walk != int(length[0]):
                fail("trip %d: length %d, stated %s" % (t + 1, walk, length[0]))
            total += walk
        if len(seen) != n:
            fail("not every item is delivered")
        if total != int(lines[-1][0]):
            fail("total %d, stated %s" % (total, lines[-1][0]))
    except (ValueError, IndexError):
        fail("malformed output")
    if total > want:
        fail("total %d is worse than %d" % (total, want))


main()
