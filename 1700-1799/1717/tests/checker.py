"""Checker: two ranges of integers from 0 to 10^9 that admit at least two
teams, with the same total satisfaction as the expected ranges."""

import sys

LIMIT = 10 ** 9
FIELDS = 3
BOUNDS = 4


class Bad(Exception):
    pass


def admitted(teams, bounds):
    a_lo, a_hi, f_lo, f_hi = bounds
    inside = [s for a, f, s in teams if a_lo <= a <= a_hi and f_lo <= f <= f_hi]
    return len(inside), sum(inside)


def check(source, expected, output):
    data = [int(w) for w in open(source).read().split()]
    n = data[0]
    teams = [tuple(data[1 + FIELDS * i:1 + FIELDS * (i + 1)]) for i in range(n)]
    want = [int(w) for w in open(expected).read().split()]
    try:
        got = [int(w) for w in open(output).read().split()]
    except ValueError:
        raise Bad("expected four integers")
    if len(got) != BOUNDS:
        raise Bad("expected four integers")
    if any(not 0 <= x <= LIMIT for x in got) or got[0] > got[1] or got[2] > got[3]:
        raise Bad("the ranges are not within 0 .. 10^9 or are reversed")
    count, total = admitted(teams, got)
    best = admitted(teams, want)[1]
    if count < 2:
        raise Bad("fewer than two teams are admitted")
    if total != best:
        raise Bad("the total is %d, the best is %d" % (total, best))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
