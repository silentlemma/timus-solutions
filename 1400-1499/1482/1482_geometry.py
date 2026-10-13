import sys
from fractions import Fraction
from itertools import permutations
from math import atan2, degrees

DIGITS = 10
FULL_TURN = 360
VERTICES = 3


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def length2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def decimal(value):
    """A rational number with exactly DIGITS digits after the point."""
    scaled = round(value * 10**DIGITS)
    sign = "-" if scaled < 0 else ""
    whole, part = divmod(abs(scaled), 10**DIGITS)
    return "%s%d.%0*d" % (sign, whole, DIGITS, part)


def main():
    v = [int(x) for x in sys.stdin.read().split()]
    points = [(v[2 * i], v[2 * i + 1]) for i in range(2 * VERTICES)]
    target, token = points[:VERTICES], points[VERTICES:]

    # a correspondence works when the sides match and the turn is the same
    # (the token cannot be flipped over)
    fits = []
    for order in permutations(target):
        if all(
            length2(token[i], token[j]) == length2(order[i], order[j])
            for i, j in ((0, 1), (0, 2), (1, 2))
        ) and (cross(*token) > 0) == (cross(*order) > 0):
            fits.append(order)
    if not fits:
        print(0)
        return
    for order in fits:
        shifts = {(t[0] - s[0], t[1] - s[1]) for s, t in zip(token, order)}
        if len(shifts) == 1:
            dx, dy = shifts.pop()
            print(1, decimal(Fraction(dx)), decimal(Fraction(dy)))
            return

    order = fits[0]
    u = (token[1][0] - token[0][0], token[1][1] - token[0][1])
    w = (order[1][0] - order[0][0], order[1][1] - order[0][1])
    angle = degrees(atan2(u[0] * w[1] - u[1] * w[0], u[0] * w[0] + u[1] * w[1]))
    if angle < 0:
        angle += FULL_TURN

    # the centre is a vertex that stays, or it lies on the perpendicular
    # bisector of every vertex and its image: 2 d . c = |t|^2 - |s|^2
    centre = None
    for s, t in zip(token, order):
        if s == t:
            centre = (Fraction(s[0]), Fraction(s[1]))
    if centre is None:
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
            if det:
                centre = (Fraction(e1 * b2 - e2 * b1, det), Fraction(a1 * e2 - a2 * e1, det))
                break
    print(2, decimal(centre[0]), decimal(centre[1]), "%.*f" % (DIGITS, angle))


main()
