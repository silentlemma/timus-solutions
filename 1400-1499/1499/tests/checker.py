"""Checker: exactly N - 3 - K new cuts, each a real diagonal (two vertices
that are neither equal nor neighbours) not cut already, and no two of
all the cuts crossing; N - 3 non-crossing diagonals triangulate the
polygon."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n, k = data[0], data[1]
    given = [tuple(sorted(data[2 + 2 * i : 4 + 2 * i])) for i in range(k)]
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if not got or got[0] != n - 3 - k:
        fail("expected %d new cuts" % (n - 3 - k))
    if len(got) != 1 + 2 * got[0]:
        fail("expected %d pairs" % got[0])
    new = [tuple(sorted(got[1 + 2 * i : 3 + 2 * i])) for i in range(got[0])]
    for a, b in new:
        if not (1 <= a < b <= n) or b - a == 1 or (a, b) == (1, n):
            fail("%d-%d is not a diagonal" % (a, b))
    cuts = given + new
    if len(set(cuts)) != len(cuts):
        fail("a cut is made twice")
    # non-crossing cuts nest like intervals: sorted by start and then by
    # decreasing end, each cut lies inside the open one before it or after it
    stack = []
    for a, b in sorted(cuts, key=lambda c: (c[0], -c[1])):
        while stack and stack[-1] <= a:
            stack.pop()
        if stack and b > stack[-1]:
            fail("two cuts cross")
        stack.append(b)


main()
