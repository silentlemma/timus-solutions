"""Checker: 0 exactly when no move works; a translation when one works,
its vector within 1e-6; otherwise a rotation whose centre and angle match
some working correspondence of the vertices (centre within 1e-6 relative,
angle within 1e-6 degrees, in [0, 360))."""

import sys
from fractions import Fraction
from itertools import permutations
from math import atan2, degrees

EPS = 1e-6
FULL_TURN = 360


def fail(reason):
    print(reason)
    sys.exit(1)


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def length2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def moves(token, target):
    """Every working correspondence as (translation or None, centre, angle)."""
    result = []
    for order in permutations(target):
        if not all(
            length2(token[i], token[j]) == length2(order[i], order[j])
            for i, j in ((0, 1), (0, 2), (1, 2))
        ) or (cross(*token) > 0) != (cross(*order) > 0):
            continue
        shifts = {(t[0] - s[0], t[1] - s[1]) for s, t in zip(token, order)}
        if len(shifts) == 1:
            result.append((shifts.pop(), None, None))
            continue
        u = (token[1][0] - token[0][0], token[1][1] - token[0][1])
        w = (order[1][0] - order[0][0], order[1][1] - order[0][1])
        angle = degrees(atan2(u[0] * w[1] - u[1] * w[0], u[0] * w[0] + u[1] * w[1])) % FULL_TURN
        centre = None
        for s, t in zip(token, order):
            if s == t:
                centre = (Fraction(s[0]), Fraction(s[1]))
        rows = [
            (2 * (t[0] - s[0]), 2 * (t[1] - s[1]), t[0] ** 2 + t[1] ** 2 - s[0] ** 2 - s[1] ** 2)
            for s, t in zip(token, order)
        ]
        for (a1, b1, e1), (a2, b2, e2) in (
            (rows[0], rows[1]),
            (rows[0], rows[2]),
            (rows[1], rows[2]),
        ):
            det = a1 * b2 - a2 * b1
            if centre is None and det:
                centre = (Fraction(e1 * b2 - e2 * b1, det), Fraction(a1 * e2 - a2 * e1, det))
        result.append((None, centre, angle))
    return result


def main():
    inp, _, output = sys.argv[1:4]
    v = [int(x) for x in open(inp).read().split()]
    target = [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]
    token = [(v[6], v[7]), (v[8], v[9]), (v[10], v[11])]
    options = moves(token, target)
    tokens = open(output).read().split()
    if not tokens:
        fail("empty output")
    kind = tokens[0]
    if not options:
        if tokens != ["0"]:
            fail("no single move works")
        return
    shifts = [shift for shift, _, _ in options if shift is not None]
    try:
        numbers = [float(x) for x in tokens[1:]]
    except ValueError:
        fail("not numbers")
    if shifts:
        if kind != "1" or len(numbers) != 2:
            fail("a translation works")
        dx, dy = shifts[0]
        if abs(numbers[0] - dx) > EPS or abs(numbers[1] - dy) > EPS:
            fail("wrong translation")
        return
    if kind != "2" or len(numbers) != 3:
        fail("a rotation is expected")
    x0, y0, a = numbers
    if not 0 <= a < FULL_TURN:
        fail("the angle must be in [0, 360)")
    for _, centre, angle in options:
        cx, cy = float(centre[0]), float(centre[1])
        scale = max(1.0, abs(cx), abs(cy))
        turn = abs(a - angle) % FULL_TURN
        if (
            abs(x0 - cx) <= EPS * scale
            and abs(y0 - cy) <= EPS * scale
            and min(turn, FULL_TURN - turn) <= EPS
        ):
            return
    fail("the rotation does not move the token onto the triangle")


main()
