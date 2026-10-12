import math
import sys

TURN = 2 * math.pi
EPS = 1e-9
FIELDS = 6


def ahead(angle):
    """An arc angle in [0, 2 pi), with angles a hair below a full turn
    taken as no turn at all."""
    angle %= TURN
    return 0.0 if angle > TURN - EPS else angle


def circle_cross(ax, ay, ra, bx, by, rb):
    """The points where the circles around a and b of radii ra and rb
    meet."""
    d = math.hypot(bx - ax, by - ay)
    if d == 0 or d > ra + rb + EPS or d < abs(ra - rb) - EPS:
        return []
    along = (ra * ra - rb * rb + d * d) / (2 * d)
    side = math.sqrt(max(0.0, ra * ra - along * along))
    ux, uy = (bx - ax) / d, (by - ay) / d
    mx, my = ax + ux * along, ay + uy * along
    return [(mx - uy * side, my + ux * side), (mx + uy * side, my - ux * side)]


def shortest(x, y, heading, r, kx, ky):
    if r == 0:
        return math.hypot(kx - x, ky - y)
    best = math.inf
    # sign 1 turns left (counter-clockwise), sign -1 turns right
    for sign in (1, -1):
        cx, cy = x - sign * r * math.sin(heading), y + sign * r * math.cos(heading)
        start = math.atan2(y - cy, x - cx)  # where the cockroach is on the circle
        # an arc, then straight along the tangent to the crumb
        d = math.hypot(kx - cx, ky - cy)
        if d >= r - EPS:
            run = math.sqrt(max(0.0, d * d - r * r))
            leave = math.atan2(ky - cy, kx - cx) - sign * math.acos(min(1.0, r / d))
            best = min(best, r * ahead(sign * (leave - start)) + run)
        # an arc, then an arc the other way around a circle 2r further
        # out that passes through the crumb
        for ox, oy in circle_cross(cx, cy, 2 * r, kx, ky, r):
            switch = math.atan2(oy - cy, ox - cx)
            first = ahead(sign * (switch - start))
            back = switch + math.pi  # the switch point seen from the new center
            end = math.atan2(ky - oy, kx - ox)
            best = min(best, r * (first + ahead(-sign * (end - back))))
    return best


def main():
    x, y, a, r, kx, ky = map(float, sys.stdin.read().split()[:FIELDS])
    print("%.4f" % shortest(x, y, math.radians(a), abs(r), kx, ky))


main()
