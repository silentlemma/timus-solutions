"""Check the answer by the rules of the statement: "No way" exactly when
the stored answer says so, and otherwise a point on the circle where the
angle of incidence equals the angle of reflection and both shots stay
outside the tank."""

import math
import sys

EPS = 1e-6
ARGS = 4


class Bad(Exception):
    pass


def check(source, expected, output):
    cx, cy, r, ax, ay, bx, by = map(int, open(source).read().split())
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["No", "way"]:
        if got != want:
            raise Bad("expected No way")
        return
    if len(got) != 2:
        raise Bad("expected two numbers")
    try:
        px, py = float(got[0]), float(got[1])
    except ValueError:
        raise Bad("expected two numbers")
    if not all(math.isfinite(v) for v in (px, py)):
        raise Bad("numbers must be finite")
    dist = math.hypot(px - cx, py - cy)
    if abs(dist - r) > EPS:
        raise Bad("the point is %.9f away from the circle" % abs(dist - r))
    nx, ny = (px - cx) / dist, (py - cy) / dist
    angles = []
    for x, y in ((ax, ay), (bx, by)):
        vx, vy = x - px, y - py
        length = math.hypot(vx, vy)
        cosine = (vx * nx + vy * ny) / length
        if cosine <= 0:
            raise Bad("a player is behind the tangent line")
        # a segment from the point to a player outside avoids the interior when
        # the player lies beyond the tangent line at the point
        if (x - cx) * nx + (y - cy) * ny < r - EPS:
            raise Bad("a shot passes through the tank")
        angles.append(math.acos(min(1.0, cosine)))
    if abs(angles[0] - angles[1]) > EPS:
        raise Bad("the angles differ by %.9f" % abs(angles[0] - angles[1]))
    # the two directions must lie on opposite sides of the normal
    cross_a = (ax - px) * ny - (ay - py) * nx
    cross_b = (bx - px) * ny - (by - py) * nx
    if cross_a * cross_b > 0:
        raise Bad("both players are on the same side of the normal")


def main():
    try:
        check(*sys.argv[1:ARGS])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
