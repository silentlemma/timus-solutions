"""Checker: the expected maximum flow, then every pipe exactly once with a
flow from 0 up to its capacity, flow kept at every transit station and
the total leaving station 1."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    m = int(data[2 * n + 1])
    rest = [int(w) for w in data[2 * n + 2:2 * n + 2 + 3 * m]]
    pipes = {}
    for i in range(m):
        a, b, c = rest[3 * i:3 * i + 3]
        pipes[(min(a, b), max(a, b))] = c
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if len(words) != 1 + 3 * m:
        fail("expected %d numbers, got %d" % (1 + 3 * m, len(words)))
    try:
        nums = [int(w) for w in words]
    except ValueError:
        fail("not an integer")
    if nums[0] != want:
        fail("flow %d, expected %d" % (nums[0], want))
    seen = set()
    net = [0] * (n + 1)
    for i in range(m):
        a, b, c = nums[1 + 3 * i:4 + 3 * i]
        key = (min(a, b), max(a, b))
        if key not in pipes or key in seen:
            fail("pipe %d %d is unknown or repeated" % (a, b))
        seen.add(key)
        if not 0 <= c <= pipes[key]:
            fail("flow %d on pipe %d %d is out of range" % (c, a, b))
        net[a] -= c
        net[b] += c
    if any(net[v] for v in range(2, n)):
        fail("flow is lost at a transit station")
    if -net[1] != want or net[n] != want:
        fail("the flow out of station 1 is not %d" % want)


main()
