import sys

SCALE = 4  # N is the distance of Q from the vertex times 4 |A|^3
NUMBERS = 9  # numbers per test


def cross(ux, uy, vx, vy):
    return ux * vy - uy * vx


def answer(a, b, c, d, e, f, px, py, r):
    # the curve is C + B t + A t^2 with A = (a, d), B = (b, e), C = (c, f)
    wx, wy = px - c, py - f  # P relative to C
    r2 = r * r
    if a == 0 and d == 0:
        if b == 0 and e == 0:
            # a single point: every line through it is an axis, and Q runs over the
            # circle with diameter CP, from C itself to P
            return "YES" if wx * wx + wy * wy <= r2 else "MAYBE"
        # a line: the line itself is an axis (Q lies on it), and so is every
        # perpendicular, with Q at the distance of P from the line
        dist = cross(wx, wy, b, e)
        return "YES" if dist * dist <= r2 * (b * b + e * e) else "MAYBE"
    # one axis along A; along it, P lies at N / (4 |A|^3) from the vertex
    a2 = a * a + d * d
    ab = a * b + d * e
    n = SCALE * a2 * (wx * a + wy * d) + ab * ab
    k2 = cross(a, d, b, e) ** 2  # zero for a ray, otherwise the parabola width
    if n <= 2 * k2:
        # the nearest point of the curve is its vertex (the end of a ray)
        return "YES" if n * n <= SCALE * SCALE * r2 * a2 * a2 * a2 else "NO"
    # Q far enough inside: squared distance k2 (N - k2) / (4 |A|^6), zero on a ray
    return "YES" if k2 * (n - k2) <= SCALE * r2 * a2 * a2 * a2 else "NO"


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    out = []
    for i in range(data[0]):
        out.append(answer(*data[1 + NUMBERS * i:1 + NUMBERS * (i + 1)]))
    print("\n".join(out))


main()
