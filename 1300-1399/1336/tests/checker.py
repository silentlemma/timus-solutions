"""Checker: the output is two whole numbers m and k from 1 to 10^100
with m^2 = k^3 * n."""

import sys

TOP = 10**100


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    got = open(output).read().split()
    if len(got) != 2 or not all(x.isdigit() for x in got):
        fail("expected two whole numbers")
    m, k = map(int, got)
    if not (1 <= m <= TOP and 1 <= k <= TOP):
        fail("m and k must be from 1 to 10^100")
    if m * m != k**3 * n:
        fail("m^2 is not k^3 * n")


if __name__ == "__main__":
    main()
