"""Checker: as many elements as the expected answer, given by distinct
positions of distinct values that form an increasing arithmetic
progression once sorted."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = open(inp).read().split()
    n = int(data[0])
    s = [int(x) for x in data[1 : 1 + n]]
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if not got or got[0] != want:
        fail("expected %d elements" % want)
    pos = got[1:]
    if len(pos) != want:
        fail("expected %d positions" % want)
    if len(set(pos)) != want or any(not 1 <= p <= n for p in pos):
        fail("positions must be distinct and between 1 and N")
    values = sorted(s[p - 1] for p in pos)
    if len(set(values)) != want:
        fail("the values must be distinct")
    steps = {b - a for a, b in zip(values, values[1:])}
    if len(steps) > 1:
        fail("the values do not form an arithmetic progression")


main()
