"""Checker: the output is three different whole numbers A, B and C
between N^2 and (N + 1)^2 with A^2 + B^2 divisible by C. A triple always
exists, so No solution is never right."""

import sys

COUNT = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    got = open(output).read().split()
    if len(got) != COUNT or not all(x.lstrip("-").isdigit() for x in got):
        fail("expected three whole numbers")
    a, b, c = map(int, got)
    if len({a, b, c}) != COUNT:
        fail("the numbers are not different")
    if not all(n * n <= v <= (n + 1) ** 2 for v in (a, b, c)):
        fail("a number lies outside [%d, %d]" % (n * n, (n + 1) ** 2))
    if (a * a + b * b) % c != 0:
        fail("%d^2 + %d^2 is not divisible by %d" % (a, b, c))


if __name__ == "__main__":
    main()
