"""Checker: "No" exactly when the expected output says so; otherwise "Yes" and
one winner per pair, a team of that pair, no team winning twice."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    data = list(map(int, open(source).read().split()))
    n = data[0]
    ends = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[0] == "No":
        if got != ["No"]:
            raise Bad("expected No")
        return
    if len(got) != n + 1 or got[0] != "Yes" or not all(w.isdigit() for w in got[1:]):
        raise Bad("expected Yes and %d winners" % n)
    winners = [int(w) for w in got[1:]]
    for i, w in enumerate(winners):
        if w not in ends[i]:
            raise Bad("pair %d: team %d does not play in it" % (i + 1, w))
    if len(set(winners)) != n:
        raise Bad("a team wins twice")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
