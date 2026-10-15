"""Checker: an n x n table holding exactly the given heights, each row and
column at its largest in the middle and never growing towards the ends."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def good(line):
    mid = len(line) // 2
    left = all(line[k] >= line[k - 1] for k in range(1, mid + 1))
    right = all(line[k] >= line[k + 1] for k in range(mid, len(line) - 1))
    return left and right


def main():
    source, _, output = sys.argv[1:4]
    data = list(map(int, open(source).read().split()))
    n, heights = data[0], data[1:]
    got = open(output).read().split()
    if len(got) != n * n or not all(w.isdigit() for w in got):
        fail("expected %d numbers" % (n * n))
    table = [[int(w) for w in got[r * n : (r + 1) * n]] for r in range(n)]
    if sorted(sum(table, [])) != sorted(heights):
        fail("the table does not hold exactly the given soldiers")
    for k in range(n):
        if not good(table[k]):
            fail("row %d is out of order" % (k + 1))
        if not good([table[r][k] for r in range(n)]):
            fail("column %d is out of order" % (k + 1))


main()
