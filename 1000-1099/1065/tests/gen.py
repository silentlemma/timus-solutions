"""A random convex border: a seed, N, M and the shape. ring: N integer
points near a circle of radius 9000, kept in convex position; box: the
border of a rectangle with N // 4 towers on each side (collinear towers;
N is rounded down to a multiple of 4).
The towers go clockwise; the monuments are random points strictly inside."""

import math
import random
import sys

RADIUS = 9000


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    pts = sorted(set(points))
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def main():
    seed, n, m = (int(x) for x in sys.argv[1:4])
    shape = sys.argv[4]
    rng = random.Random(seed)
    if shape == "box":
        w, h = rng.randint(100, RADIUS), rng.randint(100, RADIUS)
        corners = [(-w, -h), (w, -h), (w, h), (-w, h)]
        towers = []
        per_side = max(1, n // 4)
        for c in range(4):
            a, b = corners[c], corners[(c + 1) % 4]
            for k in range(per_side):
                towers.append(
                    (a[0] + (b[0] - a[0]) * k // per_side, a[1] + (b[1] - a[1]) * k // per_side)
                )
        n = len(towers)
    else:
        while True:
            angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))
            pts = [(round(RADIUS * math.cos(a)), round(RADIUS * math.sin(a))) for a in angles]
            towers = hull(pts)
            if len(towers) == n:
                break
    towers.reverse()  # counterclockwise -> clockwise
    xs = [p[0] for p in towers]
    ys = [p[1] for p in towers]
    monuments = []
    while len(monuments) < m:
        p = (rng.randint(min(xs), max(xs)), rng.randint(min(ys), max(ys)))
        if all(cross(towers[k], towers[(k + 1) % n], p) < 0 for k in range(n)):
            monuments.append(p)
    lines = ["%d %d" % (n, m)] + ["%d %d" % p for p in towers + monuments]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
