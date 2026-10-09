"""Checker: T must equal M - N + (number of components), the most cycles
that can each own a road; every tour must be a cycle of K > 2 different
cities joined by roads, and must have a road used by no other tour."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n, m = data[0], data[1]
    roads = set()
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    parts = n
    for i in range(m):
        a, b = data[2 + 2 * i], data[3 + 2 * i]
        roads.add((min(a, b), max(a, b)))
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            parts -= 1
    want = m - n + parts
    try:
        got = list(map(int, open(output).read().split()))
    except ValueError:
        fail("non-integer token")
    if not got or got[0] != want:
        fail("expected %d tours" % want)
    pos = 1
    tours = []
    for t in range(want):
        if pos >= len(got):
            fail("tour %d is missing" % (t + 1))
        k = got[pos]
        cities = got[pos + 1 : pos + 1 + k]
        pos += 1 + k
        if k <= 2 or len(cities) != k or len(set(cities)) != k:
            fail("tour %d is not a cycle of more than two different cities" % (t + 1))
        edges = []
        for a, b in zip(cities, cities[1:] + cities[:1]):
            e = (min(a, b), max(a, b))
            if e not in roads:
                fail("tour %d uses %d-%d, which is not a road" % (t + 1, a, b))
            edges.append(e)
        tours.append(edges)
    if pos != len(got):
        fail("extra output")
    used = Counter(e for edges in tours for e in edges)
    for t, edges in enumerate(tours):
        if all(used[e] > 1 for e in edges):
            fail("every road of tour %d belongs to another tour too" % (t + 1))


main()
