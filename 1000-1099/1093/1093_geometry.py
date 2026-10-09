import math
import sys

HALF_G = 5.0
# coefficients this small count as zero
TINY = 1e-12
# tolerance for times and for being strictly inside the rim
EPS = 1e-9


def main():
    cx, cy, cz, nx, ny, nz, r, sx, sy, sz, vx, vy, vz = map(float, sys.stdin.read().split())
    dx, dy, dz = sx - cx, sy - cy, sz - cz

    def inside(t):
        # the dart at time t, if that time has come, is strictly inside the rim
        if t < -EPS:
            return False
        t = max(t, 0.0)
        px, py, pz = dx + vx * t, dy + vy * t, dz + vz * t - HALF_G * t * t
        return px * px + py * py + pz * pz < r * r - EPS

    # the distance to the plane, times |N|, is a t^2 + 2 h t + c; a flight
    # that never crosses the plane, even one lying in it, misses
    a = -HALF_G * nz
    h = (nx * vx + ny * vy + nz * vz) / 2
    c = nx * dx + ny * dy + nz * dz
    hit = False
    if abs(a) < TINY:
        hit = abs(h) >= TINY and inside(-c / (2 * h))
    else:
        d = h * h - a * c
        if d >= -TINY:
            root = math.sqrt(max(d, 0.0))
            hit = inside((-h - root) / a) or inside((-h + root) / a)
    print("HIT" if hit else "MISSED")


main()
