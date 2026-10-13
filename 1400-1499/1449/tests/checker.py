"""Checker: n non-negative integers for the firms and n for the banks,
every credit A[i][j] at most BR[i] + BC[j], and the same total of bribes
as the reference."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n = data[0]
    a = [data[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    want = sum(int(x) for x in open(expected).read().split())
    got = open(output).read().split()
    if len(got) != 2 * n:
        fail("expected %d numbers" % (2 * n))
    try:
        values = [int(x) for x in got]
    except ValueError:
        fail("the bribes must be integers")
    rows, cols = values[:n], values[n:]
    if min(values) < 0:
        fail("a bribe is negative")
    for i in range(n):
        for j in range(n):
            if a[i][j] > rows[i] + cols[j]:
                fail("credit %d %d is not covered" % (i + 1, j + 1))
    if sum(values) != want:
        fail("total %d, expected %d" % (sum(values), want))


main()
