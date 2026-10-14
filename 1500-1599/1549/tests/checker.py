"""Checker: Atawazu exactly when expected; otherwise as many pieces as
expected, at most S straights and T turns, and laying them out from any
square must close the loop without two pieces on one square."""

import sys

STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    s, t = map(int, open(source).read().split())
    want = open(expected).read().split()
    got = open(output).read().split()
    if not got or (want[0] == "Atawazu") != (got[0] == "Atawazu"):
        fail("got %s, expected %s" % (got[:1], want[0]))
    if want[0] == "Atawazu":
        return
    if len(got) != 2 or not got[0].isdigit() or int(got[0]) != int(want[0]):
        fail("expected %s pieces" % want[0])
    path = got[1]
    if len(path) != int(got[0]) or set(path) - set("FLR"):
        fail("the path does not match its length or has other letters")
    if path.count("F") > s or len(path) - path.count("F") > t:
        fail("too many straights or turns")
    x = y = d = 0
    seen = set()
    for c in path:
        if (x, y) in seen:
            fail("two pieces on one square")
        seen.add((x, y))
        d = (d + {"F": 0, "L": 1, "R": 3}[c]) % 4
        x, y = x + STEPS[d][0], y + STEPS[d][1]
    if (x, y, d) != (0, 0, 0):
        fail("the path does not close")


main()
