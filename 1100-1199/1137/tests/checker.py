"""Checker: the count k equals the number of old segments, then k + 1 stops
that start and end at the same stop, and the k segments between
neighbouring stops are exactly the old segments, counted with
multiplicity. The stops are always connected and every route is a cycle,
so 0 is rejected."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n = next(tok)
    segments = Counter()
    for _ in range(n):
        m = next(tok)
        stops = [next(tok) for _ in range(m + 1)]
        segments.update(zip(stops, stops[1:]))
    got = open(output).read().split()
    if not got or not all(t.isdigit() for t in got):
        fail("expected numbers")
    k = int(got[0])
    total = sum(segments.values())
    if k != total:
        fail("expected %d segments, got %d" % (total, k))
    route = [int(t) for t in got[1:]]
    if len(route) != k + 1 or route[0] != route[-1]:
        fail("expected %d stops ending where they start" % (k + 1))
    if Counter(zip(route, route[1:])) != segments:
        fail("the segments differ from the old ones")


if __name__ == "__main__":
    main()
