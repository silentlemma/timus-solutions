"""Checker: two lines, each a permutation of 1 ... N starting with 1; the
round trip of the first must cost as little as the expected first line,
the second as much as the expected second line."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def cost(order):
    return sum(a * b for a, b in zip(order, order[1:] + order[:1]))


def main():
    source, expected, output = sys.argv[1:4]
    n = int(open(source).read().split()[0])
    want = [
        list(map(int, line.split())) for line in open(expected).read().splitlines() if line.strip()
    ]
    lines = [line for line in open(output).read().splitlines() if line.strip()]
    if len(lines) != len(want):
        fail("expected %d lines, got %d" % (len(want), len(lines)))
    for name, line, target in zip(("cheapest", "dearest"), lines, want):
        try:
            order = [int(v) for v in line.split()]
        except ValueError:
            fail("not numbers")
        if sorted(order) != list(range(1, n + 1)) or order[0] != 1:
            fail("the %s order is not a permutation of 1 ... %d from 1" % (name, n))
        if cost(order) != cost(target):
            fail("the %s order costs %d, expected %d" % (name, cost(order), cost(target)))


main()
