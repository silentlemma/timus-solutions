"""Checker: OK and n different candidates such that every two houses have
a lattice point strictly between them, that is gcd(|dx|, |dy|) >= 2.
Houses of one parity class always do, which keeps the usual case fast;
otherwise every pair is checked."""

import sys
from math import gcd

PER_PLACE = 5


class Bad(Exception):
    pass


def check(source, expected, output):
    data = [int(w) for w in open(source).read().split()]
    n = data[0]
    houses = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(PER_PLACE * n)]
    words = open(output).read().split()
    if not words or words[0] != "OK":
        raise Bad("expected OK")
    picked = [int(w) for w in words[1:]]
    if len(picked) != n or len(set(picked)) != n:
        raise Bad("need %d different candidates, got %d numbers" % (n, len(picked)))
    if not all(1 <= i <= len(houses) for i in picked):
        raise Bad("a candidate number is out of range")
    chosen = [houses[i - 1] for i in picked]
    if len({(x % 2, y % 2) for x, y in chosen}) == 1:
        return
    for a in range(n):
        for b in range(a + 1, n):
            (x1, y1), (x2, y2) = chosen[a], chosen[b]
            if gcd(abs(x1 - x2), abs(y1 - y2)) < 2:
                raise Bad("candidates %d and %d do not respect each other" % (picked[a], picked[b]))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
