"""Checker: if the expected answer is No solution the output must say so
too. Otherwise the output gives the same, minimal count and then that
many segments, each taken from the input (no segment more often than it
appears there), in order of their left ends, that together cover [0, M]."""

import sys
from collections import Counter

NO = "No solution"


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = open(inp).read().split()
    m = int(data[0])
    pool = Counter()
    for i in range(1, len(data) - 1, 2):
        pair = (int(data[i]), int(data[i + 1]))
        if pair == (0, 0):
            break
        pool[pair] += 1
    expected = open(ans).read().split()
    got = open(output).read().split()
    if expected[:2] == NO.split():
        if got != NO.split():
            fail("expected No solution")
        return
    if not got or not got[0].lstrip("-").isdigit():
        fail("expected a count")
    count = int(got[0])
    if count != int(expected[0]):
        fail("count %d, the minimum is %s" % (count, expected[0]))
    if len(got) != 1 + 2 * count:
        fail("expected %d segments" % count)
    chosen = [(int(got[1 + 2 * k]), int(got[2 + 2 * k])) for k in range(count)]
    used = Counter(chosen)
    for pair, times in used.items():
        if pool[pair] < times:
            fail("segment %d %d is not in the input" % pair)
    if any(a[0] > b[0] for a, b in zip(chosen, chosen[1:])):
        fail("segments are not ordered by left end")
    covered = 0
    for left, right in chosen:
        if left > covered:
            fail("the point %d is not covered" % covered)
        covered = max(covered, right)
    if covered < m:
        fail("only [0, %d] is covered" % covered)


if __name__ == "__main__":
    main()
