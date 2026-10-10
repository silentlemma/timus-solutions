"""Checker: M rows in input order, each a count and that many ship lengths
adding up to the row length, with every ship used exactly once."""

import sys
from collections import Counter


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n, m = next(tok), next(tok)
    ships = [next(tok) for _ in range(n)]
    rows = [next(tok) for _ in range(m)]
    if sum(ships) != sum(rows):
        fail("invalid test: the rows and the ships have different total lengths")
    try:
        got = iter(int(x) for x in open(output).read().split())
        used = []
        for r in range(m):
            count = next(got)
            row = [next(got) for _ in range(count)]
            if count < 1:
                fail("row %d has no ship" % (r + 1))
            if sum(row) != rows[r]:
                fail("row %d adds up to %d, not %d" % (r + 1, sum(row), rows[r]))
            used += row
    except (ValueError, StopIteration):
        fail("expected M rows of integers")
    if next(got, None) is not None:
        fail("extra output")
    if Counter(used) != Counter(ships):
        fail("the ships used are not exactly the given ones")


main()
