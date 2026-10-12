import math
import sys

TURN = 2 * math.pi
FULL_TURN_DEGREES = 360
ROUND_OFF = 1e-15
FIELDS = 6


def ahead(angle):
    """An arc angle in [0, 2 pi)."""
    return angle % TURN


def circle_cross(r, cy, kx, ky, power):
    """The second-circle centers, using power = d squared minus r squared
    to test whether the circles meet."""
    if power < 0 or power > 8 * r * r:
        return []
    d = math.hypot(kx, ky - cy)
    along = (4 * r * r + power) / (2 * d)
    side = math.sqrt(max(0.0, power * (8 * r * r - power))) / (2 * d)
    ux, uy = kx / d, (ky - cy) / d
    mx, my = ux * along, cy + uy * along
    return [(mx - uy * side, my + ux * side), (mx + uy * side, my - ux * side)]


def shortest(x, y, heading, r, kx, ky):
    dx, dy = kx - x, ky - y
    if r * r == 0 or (dx == 0 and dy == 0):
        return math.hypot(dx, dy)
    heading %= FULL_TURN_DEGREES
    quadrant = math.floor(heading / 90 + 0.5)
    heading = (heading - quadrant * 90) * math.pi / 180
    kx, ky = (dx * math.cos(heading) + dy * math.sin(heading),
              -dx * math.sin(heading) + dy * math.cos(heading))
    for _ in range(quadrant % 4):
        kx, ky = ky, -kx
    best = math.inf
    # sign 1 turns left (counter-clockwise), sign -1 turns right
    for sign in (1, -1):
        cy = sign * r
        power = dx * dx + dy * dy - 2 * cy * ky
        if -ROUND_OFF * (dx * dx + dy * dy) <= power < 0:
            power = 0.0
        # an arc, then straight along the tangent to the crumb
        if power >= 0:
            run = math.sqrt(power)
            leave = math.atan2(kx, r - sign * ky) - math.atan2(run, r)
            best = min(best, r * ahead(leave) + run)
        # an arc, then an arc the other way around a circle 2r further
        # out that passes through the crumb
        for ox, oy in circle_cross(r, cy, kx, ky, power):
            first = ahead(math.atan2(ox, r - sign * oy))
            vx, vy = -ox, cy - oy  # the switch radius from the new center, doubled
            ex, ey = kx - ox, ky - oy
            last = math.atan2(-sign * (vx * ey - vy * ex), vx * ex + vy * ey)
            best = min(best, r * (first + ahead(last)))
    return best


def main():
    x, y, a, r, kx, ky = map(float, sys.stdin.read().split()[:FIELDS])
    print("%.4f" % shortest(x, y, a, abs(r), kx, ky))


main()
