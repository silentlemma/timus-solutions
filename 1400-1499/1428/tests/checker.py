"""Checker: three whole numbers from 1 to 10^50 with X^A + Y^B = Z^C."""

import sys

TOP = 10**50


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    a, b, c = map(int, open(inp).read().split())
    got = open(output).read().split()
    if len(got) != 3:
        fail("expected three numbers")
    x, y, z = map(int, got)
    if not all(1 <= v <= TOP for v in (x, y, z)):
        fail("a number outside 1..10^50")
    if x**a + y**b != z**c:
        fail("X^A + Y^B differs from Z^C")


main()
