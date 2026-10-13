"""Checker: the faces form a valid chain of rolls from the base back to the
base, at most N of them; the printed distance is the distance of the final
centre from the point, to 3 decimals; that distance is the expected one, and
on a tie the number of rolls is not larger than the expected one."""

import math
import sys

SIDES = 4
TOLERANCE = 1e-6  # on the distance, against the expected answer
PRINTED = 1e-3  # on the printed distance
TIE = 1e-9


def fail(reason):
    print(reason)
    sys.exit(1)


def roll(face, v, nxt, s, t):
    """the corners of the face on the table after rolling from face onto nxt"""

    def cross(a, b, p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

    def away(a, b, q):
        dx, dy = b[0] - a[0], b[1] - a[1]
        length = math.hypot(dx, dy)
        nx, ny = -dy / length, dx / length
        if cross(a, b, (a[0] + nx, a[1] + ny)) * cross(a, b, q) > 0:
            nx, ny = -nx, -ny
        return nx, ny

    def reflect(p, a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        k = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
        return (2 * (a[0] + k * dx) - p[0], 2 * (a[1] + k * dy) - p[1])

    if face == 0:
        a, b = v[nxt - 1], v[nxt % SIDES]
        centre = (sum(p[0] for p in v) / SIDES, sum(p[1] for p in v) / SIDES)
        nx, ny = away(a, b, centre)
        return [a, b, ((a[0] + b[0]) / 2 + nx * t, (a[1] + b[1]) / 2 + ny * t)]
    if nxt == 0:
        a, b = v[0], v[1]
        nx, ny = away(a, b, v[2])
        corners = [a, b, (b[0] + nx * s, b[1] + ny * s), (a[0] + nx * s, a[1] + ny * s)]
        out = [None] * SIDES
        for i in range(SIDES):
            out[(face - 1 + i) % SIDES] = corners[i]
        return out
    if nxt == face % SIDES + 1:
        return [v[1], reflect(v[0], v[1], v[2]), v[2]]
    return [reflect(v[1], v[0], v[2]), v[0], v[2]]


def adjacent(a, b):
    if a == b:
        return False
    return a == 0 or b == 0 or (a - b) % 2 == 1


def play(faces, s, t):
    """the final centre after the rolls, or None if a roll is impossible"""
    v = [(-s / 2, s / 2), (s / 2, s / 2), (s / 2, -s / 2), (-s / 2, -s / 2)]
    for a, b in zip(faces, faces[1:]):
        if not (0 <= b <= SIDES and adjacent(a, b)):
            return None
        v = roll(a, v, b, s, t)
    return sum(p[0] for p in v) / SIDES, sum(p[1] for p in v) / SIDES


def main():
    path_in, path_expected, path_out = sys.argv[1:4]
    s, side, x, y, n = open(path_in).read().split()
    s, side, x, y, n = float(s), float(side), float(x), float(y), int(n)
    t = math.sqrt(side * side - s * s / 4)
    want = [int(f) for f in open(path_expected).read().split()[2:]]
    want_rolls = len(want) - 1
    wx, wy = play(want, s, t)
    want_dist = math.hypot(wx - x, wy - y)
    try:
        got = open(path_out).read().split()
        printed, rolls = float(got[0]), int(got[1])
        faces = [int(f) for f in got[2:]]
    except (ValueError, IndexError):
        fail("expected a distance, a number of rolls and the faces")
    if not 0 <= rolls <= n or len(faces) != rolls + 1:
        fail("the number of rolls does not fit")
    if faces[0] != 0 or faces[-1] != 0:
        fail("the pyramid must start and end on its base")
    end = play(faces, s, t)
    if end is None:
        fail("a roll goes between faces without a common edge")
    d = math.hypot(end[0] - x, end[1] - y)
    if abs(printed - d) > PRINTED:
        fail("printed %.3f, but the pyramid ends at distance %.6f" % (printed, d))
    if d > want_dist + TOLERANCE:
        fail("distance %.6f, the best is %.6f" % (d, want_dist))
    if d > want_dist - TIE and rolls > want_rolls:
        fail("%d rolls, the same distance takes %d" % (rolls, want_rolls))


main()
