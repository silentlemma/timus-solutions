"""Checker: n and m distinct positive masses up to 10^9 such that no two
neighbours can get one box of each kind of the same total weight; such
masses always exist, so "It is a lie!" is never right."""

import sys

LIMIT = 10 ** 9


class Bad(Exception):
    pass


def check(source, output):
    n, m = (int(w) for w in open(source).read().split())
    lines = open(output).read().strip().split("\n")
    if len(lines) != 2:
        raise Bad("expected two lines of masses")
    try:
        first, second = ([int(w) for w in line.split()] for line in lines)
    except ValueError:
        raise Bad("expected integers")
    if len(first) != n or len(second) != m:
        raise Bad("expected %d and %d masses" % (n, m))
    masses = first + second
    if any(not 0 < x <= LIMIT for x in masses) or len(set(masses)) != n + m:
        raise Bad("the masses are not distinct positive numbers up to 10^9")
    # two gifts of equal weight share no box, so all the sums a + b must
    # differ: a repeated sum with a common box would mean equal boxes
    sums = [a + b for a in first for b in second]
    if len(set(sums)) != len(sums):
        raise Bad("two neighbours can get gifts of the same weight")


def main():
    try:
        check(sys.argv[1], sys.argv[3])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
