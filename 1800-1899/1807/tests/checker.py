"""Checker: at least two positive pocket sizes adding up to n, whose gcd
is the largest possible and whose lcm equals the lcm of the expected
answer, compared exactly."""

import sys
from functools import reduce
from math import gcd


class Bad(Exception):
    pass


def lcm(values):
    return reduce(lambda a, b: a * b // gcd(a, b), values, 1)


def check(source, expected, output):
    n = int(open(source).read())
    want = list(map(int, open(expected).read().split()))
    got = open(output).read().split()
    if len(got) < 2 or not all(w.isdigit() and int(w) > 0 for w in got):
        raise Bad("expected at least two positive numbers")
    got = list(map(int, got))
    if sum(got) != n:
        raise Bad("the pockets hold %d cartridges, not %d" % (sum(got), n))
    if reduce(gcd, got) != reduce(gcd, want):
        raise Bad("gcd %d, the largest is %d" % (reduce(gcd, got), reduce(gcd, want)))
    if lcm(got) != lcm(want):
        raise Bad("the lcm is not the largest for this gcd")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
