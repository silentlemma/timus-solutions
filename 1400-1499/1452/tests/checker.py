"""Checker: the same count as the reference, then that many different
element numbers whose values, sorted, are different and form an
arithmetic progression with a positive difference."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    n, s = data[0], data[1:]
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or int(got[0]) != want:
        fail("expected %d elements" % want)
    idx = [int(x) for x in got[1:]]
    if len(idx) != want or len(set(idx)) != want or not all(1 <= i <= n for i in idx):
        fail("expected %d different element numbers" % want)
    values = sorted(s[i - 1] for i in idx)
    steps = {b - a for a, b in zip(values, values[1:])}
    if len(steps) > 1 or (steps and min(steps) <= 0):
        fail("the values do not form an increasing progression")


main()
