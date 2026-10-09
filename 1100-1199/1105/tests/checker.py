"""Checker: distinct observer numbers whose time alone, the time covered by
exactly one of them, measured by a sweep over all their ends, is at least
2/3 of the whole span. The observers of every test cover the span, so an
answer always exists and 0 is never accepted."""

import sys

EPS = 1e-6
SHARE = 2 / 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = open(inp).read().split()
    t0, t1 = float(tok[0]), float(tok[1])
    n = int(tok[2])
    obs = [(float(tok[3 + 2 * i]), float(tok[4 + 2 * i])) for i in range(n)]
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("expected integers")
    if not got or got[0] != len(got) - 1:
        fail("the count does not match the numbers that follow")
    painted = got[1:]
    if not painted:
        fail("an answer always exists")
    if len(set(painted)) != len(painted) or not all(1 <= p <= n for p in painted):
        fail("observer numbers must be distinct and in range")
    events = []
    for p in painted:
        events.append((obs[p - 1][0], 1))
        events.append((obs[p - 1][1], -1))
    events.sort()
    alone, depth = 0.0, 0
    for k, (x, d) in enumerate(events):
        if depth == 1:
            alone += x - events[k - 1][0]
        depth += d
    if alone < SHARE * (t1 - t0) - EPS:
        fail("alone for %.9f of %.9f" % (alone, t1 - t0))


main()
