"""Checker: the count must be the length of the longest chain, found here
by a memoised search over all segments, and the listed segments must be
different and each strictly inside the next one, with no common ends."""

import sys
from functools import lru_cache


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n = data[0]
    seg = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]

    def inside(a, b):
        return seg[b][0] < seg[a][0] and seg[a][1] < seg[b][1]

    @lru_cache(maxsize=None)
    def longest(a):
        return 1 + max((longest(b) for b in range(n) if inside(a, b)), default=0)

    sys.setrecursionlimit(10000)
    want = max(longest(a) for a in range(n))
    try:
        got = list(map(int, open(output).read().split()))
    except ValueError:
        fail("non-integer token")
    if not got or got[0] != want:
        fail("expected a chain of %d segments" % want)
    chain = got[1:]
    if len(chain) != want:
        fail("the chain lists %d segments" % len(chain))
    if not all(1 <= x <= n for x in chain):
        fail("a segment number is out of range")
    for a, b in zip(chain, chain[1:]):
        if not inside(a - 1, b - 1):
            fail("segment %d is not strictly inside segment %d" % (a, b))


main()
