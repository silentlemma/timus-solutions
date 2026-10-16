"""Checker: four loads, none negative, no bridge over its capacity, and
together as large as the expected plan, all within 1e-3."""

import sys

LIMIT = 1e-3
ROUTES = 4
PAIRS = ((0, 3), (0, 2), (2, 3), (1, 2), (1, 3), (0, 1))


class Bad(Exception):
    pass


def check(source, expected, output):
    caps = [int(w) for w in open(source).read().split()]
    want = [float(w) for w in open(expected).read().split()]
    got = open(output).read().split()
    if len(got) != ROUTES:
        raise Bad("expected %d loads, got %d" % (ROUTES, len(got)))
    try:
        loads = [float(w) for w in got]
    except ValueError:
        raise Bad("a load is not a number")
    if min(loads) < -LIMIT:
        raise Bad("a negative load")
    for k, ((i, j), cap) in enumerate(zip(PAIRS, caps)):
        if loads[i] + loads[j] > cap + LIMIT:
            raise Bad("bridge %d carries %.3f over its %d" % (k + 1, loads[i] + loads[j], cap))
    if sum(loads) < sum(want) - LIMIT:
        raise Bad("%.3f in all, but %.3f is possible" % (sum(loads), sum(want)))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
