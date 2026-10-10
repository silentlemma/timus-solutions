"""Checker: the printed longest cable, then P cables that are all possible
connections, join every hub, and have that longest length; it must be the
smallest possible, found here by binary search over the lengths with a
connectivity test."""

import sys


def connected(n, cables):
    parent = list(range(n + 1))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    parts = n
    for a, b in cables:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            parts -= 1
    return parts == 1


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = list(map(int, open(inp).read().split()))
    n, m = tok[0], tok[1]
    length = {}
    for k in range(m):
        a, b, c = tok[2 + 3 * k : 5 + 3 * k]
        length[a, b] = length[b, a] = c
    values = sorted(set(length.values()))
    lo, hi = 0, len(values) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if connected(n, [e for e, c in length.items() if c <= values[mid]]):
            hi = mid
        else:
            lo = mid + 1
    best = values[lo]
    got = open(output).read().split()
    try:
        told, p = int(got[0]), int(got[1])
        cables = [(int(got[2 + 2 * k]), int(got[3 + 2 * k])) for k in range(p)]
    except (IndexError, ValueError):
        fail("expected the length, P and P cables")
    if len(got) != 2 + 2 * p:
        fail("extra output")
    if any(c not in length for c in cables):
        fail("a cable that cannot be laid")
    if not connected(n, cables):
        fail("the hubs are not all connected")
    if told != max(length[c] for c in cables):
        fail("the printed length is not the longest cable used")
    if told != best:
        fail("the longest cable %d could be %d" % (told, best))


if __name__ == "__main__":
    main()
