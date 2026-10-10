"""Checker: as many segments as the optimum, each taken from the input (with
its multiplicity), listed by increasing left end, no two sharing an inner
point. The optimum is a longest chain found by a quadratic DP over the
segments sorted by their left ends."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n = next(tok)
    segs = [(next(tok), next(tok)) for _ in range(n)]
    order = sorted(segs)
    best = [1] * n
    for i in range(n):
        for j in range(i):
            if order[j][1] <= order[i][0]:
                best[i] = max(best[i], best[j] + 1)
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if not got or len(got) != 1 + 2 * got[0]:
        fail("the count does not match the segments that follow")
    out = list(zip(got[1::2], got[2::2]))
    if len(out) != max(best):
        fail("%d segments kept, %d possible" % (len(out), max(best)))
    if Counter(out) - Counter(segs):
        fail("a segment that is not in the input")
    for (a, b), (c, d) in zip(out, out[1:]):
        if c < a:
            fail("segments not sorted by their left ends")
        if c < b:
            fail("segments %d %d and %d %d overlap" % (a, b, c, d))


main()
