import sys
from math import hypot, sqrt

BOSSES = 4
# the three ways to split the four bosses into two shots
SPLITS = ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2))


def walk(a1, b1, a2, b2):
    # walk from the origin to a point P on the line a1 b1, shoot, then walk
    # straight to the line a2 b2; along the first line P = a1 + t u and the
    # length is sqrt((t - t0)^2 + h^2) + |k t + m|, convex in t
    lx, ly = b1[0] - a1[0], b1[1] - a1[1]
    length = hypot(lx, ly)
    ux, uy = lx / length, ly / length
    t0 = -(a1[0] * ux + a1[1] * uy)
    h = abs(a1[0] * uy - a1[1] * ux)
    mx, my = b2[0] - a2[0], b2[1] - a2[1]
    norm = hypot(mx, my)
    nx, ny = -my / norm, mx / norm
    k = nx * ux + ny * uy
    m = nx * (a1[0] - a2[0]) + ny * (a1[1] - a2[1])
    # the minimum is at the foot of the origin, where the lines cross, or
    # where the slope of the first term cancels the slope k of the second
    candidates = [t0]
    if k != 0:
        candidates.append(-m / k)
    if abs(k) < 1:
        shift = k * h / sqrt(1 - k * k)
        candidates += [t0 + shift, t0 - shift]
    return min(hypot(t - t0, h) + abs(k * t + m) for t in candidates)


def main():
    v = [int(w) for w in sys.stdin.read().split()]
    p = [(v[2 * i], v[2 * i + 1]) for i in range(BOSSES)]
    best = min(min(walk(p[a], p[b], p[c], p[d]), walk(p[c], p[d], p[a], p[b]))
               for a, b, c, d in SPLITS)
    print("%.10f" % best)


main()
