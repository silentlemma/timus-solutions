import sys
from math import hypot, sqrt

EPS = 1e-9


def chord(r, eta, x, y, dx, dy):
    """Where the refracted line of sight enters the planet and where it
    would leave it again."""
    # the first crossing of the line of sight with the circle
    a = dx * dx + dy * dy
    half_b = x * dx + y * dy
    c = x * x + y * y - r * r
    t = (-half_b - sqrt(max(0.0, half_b * half_b - a * c))) / a
    ex, ey = x + dx * t, y + dy * t
    length = hypot(dx, dy)
    ux, uy = dx / length, dy / length
    # split the direction into the inward normal and the tangent; Snell's
    # law shrinks the tangent part by eta
    nx, ny = -ex / r, -ey / r
    along = ux * nx + uy * ny
    tx, ty = (ux - along * nx) / eta, (uy - along * ny) / eta
    inward = sqrt(max(0.0, 1 - tx * tx - ty * ty))
    vx, vy = inward * nx + tx, inward * ny + ty
    # the chord from the entry point along v has length -2 (e . v)
    span = -2 * (ex * vx + ey * vy)
    return (ex, ey), (ex + vx * span, ey + vy * span)


def cross(ax, ay, bx, by):
    return ax * by - ay * bx


def main():
    r, eta, ax, ay, adx, ady, bx, by, bdx, bdy = map(float, sys.stdin.read().split())
    (p1, q1), (p2, q2) = chord(r, eta, ax, ay, adx, ady), chord(r, eta, bx, by, bdx, bdy)
    d1 = (q1[0] - p1[0], q1[1] - p1[1])
    d2 = (q2[0] - p2[0], q2[1] - p2[1])
    w = (p2[0] - p1[0], p2[1] - p1[1])
    den = cross(*d1, *d2)
    if abs(den) < EPS:
        # parallel chords meet only if they lie on one line
        seen = abs(cross(*w, *d1)) < EPS * max(1.0, hypot(*d1))
    else:
        s, t = cross(*w, *d2) / den, cross(*w, *d1) / den
        seen = EPS < s < 1 - EPS and EPS < t < 1 - EPS
    print("Yes" if seen else "No")


main()
