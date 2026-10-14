"""Checker: N queens on distinct cells of the N x N board, no two on one
row, column or diagonal."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    n = int(open(source).read())
    try:
        values = [int(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(values) != 2 * n:
        fail("expected %d queens, got %d numbers" % (n, len(values)))
    seen = [set(), set(), set(), set()]
    for k in range(n):
        x, y = values[2 * k], values[2 * k + 1]
        if not (1 <= x <= n and 1 <= y <= n):
            fail("queen (%d, %d) is off the board" % (x, y))
        for lines, key in zip(seen, (x, y, x + y, x - y)):
            if key in lines:
                fail("queen (%d, %d) is attacked" % (x, y))
            lines.add(key)


main()
