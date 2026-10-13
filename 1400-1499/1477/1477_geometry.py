import sys
from math import gcd

FIELDS = 3  # X, Y and Z


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def main():
    data = [int(x) for x in sys.stdin.read().split()]
    n = data[0]
    points = [tuple(data[1 + FIELDS * i : 1 + FIELDS * (i + 1)]) for i in range(n)]

    # every plane through the origin and two non-parallel points, once
    normals = set()
    for i in range(n):
        for j in range(i + 1, n):
            c = cross(points[i], points[j])
            g = gcd(gcd(c[0], c[1]), c[2])
            if g == 0:
                continue
            c = tuple(x // g for x in c)
            if next(x for x in c if x) < 0:
                c = tuple(-x for x in c)
            normals.add(c)

    best = 1  # a single airplane is always visible
    for normal in normals:
        side = [dot(normal, p) for p in points]
        above = sum(1 for s in side if s > 0)
        below = sum(1 for s in side if s < 0)
        circle = [p for p, s in zip(points, side) if s == 0]
        # a slight tilt shows the points of the circle in its best open half:
        # its edge passes through one of them, which a tilt adds as well
        half = 0
        for z in circle:
            edge = cross(normal, z)
            ahead = sum(1 for p in circle if dot(edge, p) > 0)
            behind = sum(1 for p in circle if dot(edge, p) < 0)
            half = max(half, ahead + 1, behind + 1)
        best = max(best, above + half, below + half)
    print(best)


main()
