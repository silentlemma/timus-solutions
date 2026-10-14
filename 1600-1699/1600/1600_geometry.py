import math
import sys

COORDS = 6  # x, y, z, vx, vy, vz


def main():
    data = sys.stdin.read().split()
    n, d = int(data[0]), float(data[1])
    obj = [[float(v) for v in data[2 + COORDS * i : 2 + COORDS * (i + 1)]] for i in range(n)]
    best, pair = math.inf, None
    for i in range(n):
        x1, y1, z1, u1, v1, w1 = obj[i]
        for j in range(i + 1, n):
            x2, y2, z2, u2, v2, w2 = obj[j]
            # |p + v t| = d for the relative position p and velocity v:
            # (v.v) t^2 + 2 (p.v) t + (p.p - d^2) = 0
            px, py, pz = x2 - x1, y2 - y1, z2 - z1
            vx, vy, vz = u2 - u1, v2 - v1, w2 - w1
            a = vx * vx + vy * vy + vz * vz
            if a == 0:
                continue
            b = px * vx + py * vy + pz * vz
            # summed from -d^2 up, as the other solutions do: on a tangent
            # the rounding decides whether the discriminant is negative
            c = -d * d + px * px + py * py + pz * pz
            disc = b * b - a * c
            if disc < 0:
                continue
            # the earlier root; the pair starts apart, so a negative one
            # means they are moving away
            t = (-b - math.sqrt(disc)) / a
            if 0 <= t < best:
                best, pair = t, (i + 1, j + 1)
    if pair is None:
        print("OK")
    else:
        print("ALARM!")
        print("%.3f %d %d" % (best, pair[0], pair[1]))


main()
