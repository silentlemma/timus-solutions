import sys
from math import hypot, sqrt

CITIES = 3
EPS = 1e-9  # a tie at the edge gives the same cost either way


def cost(points, weights, mx, my):
    return sum(w * hypot(x - mx, y - my) for (x, y), w in zip(points, weights))


def solve(points, weights):
    # a city is the best place when the pull of the others, the weighted
    # unit vectors towards them, is no stronger than the weight standing on
    # that very spot
    for vx, vy in points:
        here = pull_x = pull_y = 0
        for (x, y), w in zip(points, weights):
            d = hypot(x - vx, y - vy)
            if d == 0:
                here += w
            else:
                pull_x += w * (x - vx) / d
                pull_y += w * (y - vy) / d
        if hypot(pull_x, pull_y) <= here + EPS:
            return cost(points, weights, vx, vy)
    # otherwise the best point is inside: by Ptolemy's inequality
    # w2 |MB| + w3 |MC| >= w1 |MQ| for the point Q beyond BC with
    # |BQ| : |CQ| : |BC| = w3 : w2 : w1, so the answer is w1 |AQ|
    (ax, ay), (bx, by), (cx, cy) = points
    w1, w2, w3 = weights
    base = hypot(cx - bx, cy - by)
    from_b, from_c = base * w3 / w1, base * w2 / w1
    along = (from_b * from_b - from_c * from_c + base * base) / (2 * base)
    height = sqrt(max(0.0, from_b * from_b - along * along))
    ex, ey = (cx - bx) / base, (cy - by) / base
    nx, ny = -ey, ex
    # Q lies on the other side of BC from A
    if (ax - bx) * nx + (ay - by) * ny > 0:
        nx, ny = -nx, -ny
    qx, qy = bx + along * ex + height * nx, by + along * ey + height * ny
    return w1 * hypot(ax - qx, ay - qy)


def main():
    data = list(map(int, sys.stdin.read().split()))
    out = []
    pos = 1
    for _ in range(data[0]):
        coords = data[pos:pos + 2 * CITIES]
        points = list(zip(coords[0::2], coords[1::2]))
        pos += 2 * CITIES
        weights = data[pos:pos + CITIES]
        pos += CITIES
        out.append("%.10f" % solve(points, weights))
    print("\n".join(out))


main()
