"""Checker: "No" exactly when expected; otherwise five distinct hills that
form a convex pentagon listed counterclockwise, which holds when every
other hill lies strictly to the left of every side."""

import sys

SIDES = 5


def fail(reason):
    print(reason)
    sys.exit(1)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n = int(data[0])
    points = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n)]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if not got or got[0] != want:
        fail("got %s, expected %s" % (got[:1], want))
    if want == "No":
        return
    try:
        order = [int(v) for v in got[1:]]
    except ValueError:
        fail("not numbers")
    if len(order) != SIDES or len(set(order)) != SIDES or not all(1 <= v <= n for v in order):
        fail("expected five distinct hills, got %s" % order)
    corners = [points[v - 1] for v in order]
    for i in range(SIDES):
        a, b = corners[i], corners[(i + 1) % SIDES]
        for j in range(SIDES):
            if j not in (i, (i + 1) % SIDES) and cross(a, b, corners[j]) <= 0:
                fail(
                    "hill %d is not to the left of side %d-%d"
                    % (order[j], order[i], order[(i + 1) % SIDES])
                )


main()
