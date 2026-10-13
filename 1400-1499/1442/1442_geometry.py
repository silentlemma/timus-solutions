import math
import sys

EPS = 1e-9
DEPTH = 50
CONE = 1 / 3  # a cone holds a third of its cylinder
SIMPSON = (1 / 6, 4 / 6, 1 / 6)  # weights of the ends and the middle
RICHARDSON = 15  # error estimate of the Simpson rule on halves


def main():
    r, d, h = (int(x) for x in sys.stdin.read().split())
    k = h / r  # the slope of the powder

    def lost(x):
        # the powder lost in the slice at x, parallel to the slit x = d: the cone
        # surface k (r - rho) drops to k |x - d| wherever rho < a = r - |x - d|
        a = r - abs(x - d)
        if a <= abs(x):
            return 0.0
        y = math.sqrt(a * a - x * x)
        tail = x * x * math.log((a + y) / abs(x)) if x else 0.0
        return k * (a * y - tail)

    def rule(lo, hi, flo, fmid, fhi):
        return (hi - lo) * (SIMPSON[0] * flo + SIMPSON[1] * fmid + SIMPSON[2] * fhi)

    def adaptive(lo, hi, flo, fmid, fhi, whole, eps, depth):
        mid = (lo + hi) / 2
        fl, fr = lost((lo + mid) / 2), lost((mid + hi) / 2)
        left, right = rule(lo, mid, flo, fl, fmid), rule(mid, hi, fmid, fr, fhi)
        delta = left + right - whole
        if depth == 0 or abs(delta) <= RICHARDSON * eps:
            return left + right + delta / RICHARDSON
        return adaptive(lo, mid, flo, fl, fmid, left, eps / 2, depth - 1) + adaptive(
            mid, hi, fmid, fr, fhi, right, eps / 2, depth - 1
        )

    def integral(lo, hi):
        if hi <= lo:
            return 0.0
        flo, fmid, fhi = lost(lo), lost((lo + hi) / 2), lost(hi)
        return adaptive(lo, hi, flo, fmid, fhi, rule(lo, hi, flo, fmid, fhi), EPS, DEPTH)

    volume = math.pi * r * r * h * CONE
    if d < r:
        # the slit cuts the base between (d - r) / 2 and (d + r) / 2, kinks at 0 and d
        volume -= integral((d - r) / 2, 0) + integral(0, d) + integral(d, (d + r) / 2)
    print("%.6f" % volume)


main()
