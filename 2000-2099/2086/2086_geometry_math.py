import math
import sys

QUAD = 4  # the discriminant of a t^2 + b t + c is b^2 - 4 a c


def sign_sqrt_vs(sign, disc, k):
    # compares sign * sqrt(disc) with the integer k exactly: -1, 0 or 1
    if sign > 0:
        if k < 0:
            return 1
        return (disc > k * k) - (disc < k * k)
    if k > 0:
        return -1
    return (k * k > disc) - (k * k < disc)


def main():
    x, y, z, vx, vy, ex, ey = map(int, sys.stdin.read().split())
    # Stewart: the point at fraction t of the way from Denis to the hall is at
    # squared distance (1 - t) X^2 + t Y^2 - t (1 - t) Z^2 from Vanya; Eugene is
    # at d^2, so t solves z2 t^2 + b t + c = 0 with integer coefficients
    d2 = (ex - vx) ** 2 + (ey - vy) ** 2
    z2 = z * z
    b = y * y - x * x - z2
    c = x * x - d2
    disc = b * b - QUAD * z2 * c
    found = []
    if disc >= 0:
        signs = [1] if disc == 0 else [1, -1]
        for s in signs:
            # t = (-b + s sqrt(disc)) / (2 z2) must lie in [0, 1]
            if sign_sqrt_vs(s, disc, b) < 0 or sign_sqrt_vs(s, disc, 2 * z2 + b) > 0:
                continue
            t = (-b + s * math.sqrt(disc)) / (2 * z2)
            found.append((t, c == 0 and sign_sqrt_vs(s, disc, b) == 0))
    points = []
    # a model triangle: Vanya at 0, Denis on the x axis, the hall above it
    cos_v = (x * x + y * y - z2) / (2 * x * y)
    hall = (y * cos_v, y * math.sqrt(max(0.0, 1 - cos_v * cos_v)))
    ux, uy = ex - vx, ey - vy
    for t, at_denis in found:
        px, py = x + t * (hall[0] - x), t * hall[1]
        for mirror in ([1] if at_denis else [1, -1]):
            # rotate (and maybe reflect) the model so that its point lands on Eugene
            qx, qy = px, mirror * py
            norm = qx * qx + qy * qy
            cos_r, sin_r = (qx * ux + qy * uy) / norm, (qx * uy - qy * ux) / norm
            points.append((vx + cos_r * x, vy + sin_r * x))
    print(len(points))
    for px, py in points:
        print("%.12f %.12f" % (px, py))


main()
