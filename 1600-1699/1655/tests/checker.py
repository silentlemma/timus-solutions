"""Checker: Impossible exactly when expected; otherwise the expected least
time within 1e-3, and an order of all ships that, turning the shortest
way between consecutive targets, shoots each one in time and finishes
within that time."""

import sys

FULL = 360.0
MINUTES = 60.0
TOLERANCE = 1e-3
FIELDS = 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    a, w, n = float(data[0]), float(data[1]), int(data[2])
    ships = [[float(x) for x in data[FIELDS + FIELDS * k : FIELDS * (k + 2)]] for k in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["Impossible"] or got == ["Impossible"]:
        if got != want:
            fail("expected %s" % want[0])
        return
    if len(got) != n + 1:
        fail("expected the time and %d ships" % n)
    try:
        time = float(got[0])
        order = [int(x) for x in got[1:]]
    except ValueError:
        fail("not a number")
    if abs(time - float(want[0])) > TOLERANCE:
        fail("time %s, expected %s" % (got[0], want[0]))
    if sorted(order) != list(range(1, n + 1)):
        fail("not every ship exactly once")
    speed = FULL * w
    at, clock = a, 0.0
    for k in order:
        b, d, v = ships[k - 1]
        turn = abs(b - at) % FULL
        clock += min(turn, FULL - turn) / speed
        if clock > (d - 1) / v * MINUTES + TOLERANCE:
            fail("ship %d comes within a mile first" % k)
        at = b
    if clock > float(want[0]) + TOLERANCE:
        fail("the order takes %.3f minutes" % clock)


main()
