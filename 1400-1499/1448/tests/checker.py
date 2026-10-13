"""Checker: N digits 0 and 1 such that on every stretch the number of
lamps on differs from L b / 100 by at most 2. With prefix counts P, that
holds exactly when 100 P(k) - k b spans at most 200 over all k."""

import sys

FULL = 100
SLACK = 2


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n, b = (int(x) for x in open(inp).read().split())
    got = open(output).read().split()
    if len(got) != 1 or len(got[0]) != n or set(got[0]) - set("01"):
        fail("expected one line of %d digits 0 and 1" % n)
    value = low = high = 0
    for c in got[0]:
        value += FULL * (c == "1") - b
        low, high = min(low, value), max(high, value)
    if high - low > SLACK * FULL:
        fail("some stretch is off by more than %d lamps" % SLACK)


main()
