from math import isqrt


def sign(v):
    return (v > 0) - (v < 0)


def main():
    ax, ay, bx, by, cx, cy = map(int, open(0).read().split())
    a2, b2, c2 = ax * ax + ay * ay, bx * bx + by * by, cx * cx + cy * cy
    # all values are exact integers: the center is (ux / d, uy / d) and the
    # radius times d is the square root of rho2
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = a2 * (by - cy) + b2 * (cy - ay) + c2 * (ay - by)
    uy = a2 * (cx - bx) + b2 * (ax - cx) + c2 * (bx - ax)
    if d < 0:
        d, ux, uy = -d, -ux, -uy
    rho2 = (ax * d - ux) ** 2 + (ay * d - uy) ** 2

    def sign_minus(alpha, gamma):
        """The sign of alpha - gamma * sqrt(rho2)."""
        if gamma == 0:
            return sign(alpha)
        if gamma > 0:
            return -1 if alpha <= 0 else sign(alpha * alpha - gamma * gamma * rho2)
        return 1 if alpha >= 0 else sign(gamma * gamma * rho2 - alpha * alpha)

    def ceil_plus(u):
        """The smallest integer k with k >= (u + sqrt(rho2)) / d."""
        k = (u + isqrt(rho2)) // d - 1
        while not (k * d - u >= 0 and (k * d - u) ** 2 >= rho2):
            k += 1
        return k

    def floor_minus(u):
        """The largest integer k with k <= (u - sqrt(rho2)) / d."""
        k = -((isqrt(rho2) - u) // d) + 1
        while not (u - k * d >= 0 and (u - k * d) ** 2 >= rho2):
            k -= 1
        return k

    # an extreme point of the circle is on the arc when it lies on the same side
    # of the chord AB as C; side(P) * d = alpha - gamma * sqrt(rho2)
    ex, ey = bx - ax, by - ay
    side_c = sign(ex * (cy - ay) - ey * (cx - ax))
    alpha = ex * (uy - ay * d) - ey * (ux - ax * d)
    lo_x, hi_x = min(ax, bx), max(ax, bx)
    lo_y, hi_y = min(ay, by), max(ay, by)
    if sign_minus(alpha, ey) == side_c:
        hi_x = max(hi_x, ceil_plus(ux))
    if sign_minus(alpha, -ey) == side_c:
        lo_x = min(lo_x, floor_minus(ux))
    if sign_minus(alpha, -ex) == side_c:
        hi_y = max(hi_y, ceil_plus(uy))
    if sign_minus(alpha, ex) == side_c:
        lo_y = min(lo_y, floor_minus(uy))
    print((hi_x - lo_x) * (hi_y - lo_y))


main()
