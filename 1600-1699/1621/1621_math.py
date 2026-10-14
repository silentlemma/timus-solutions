import math
import sys

NODE = math.sqrt(0.6)  # the outer nodes of three-point Gauss-Legendre on [-1, 1]
OUTER = 5.0  # its weights are 5/9, 8/9 and 5/9
MIDDLE = 8.0
TOTAL = 9.0
TOLERANCE = 1e-13
DEPTH = 50
LIMIT = 20.0  # sinh(20) is about 2.4e8, beyond which the tails are negligible


def main():
    a0, a1, a2, a3, a4 = (float(x) for x in sys.stdin.read().split())

    def f(t):
        # x = sinh t, dx = cosh t dt: the infinite line becomes a finite range
        x = math.sinh(t)
        return math.cosh(t) / ((((a4 * x + a3) * x + a2) * x + a1) * x + a0)

    def gauss(lo, hi):
        mid, half = (lo + hi) / 2, (hi - lo) / 2
        nodes = OUTER * f(mid - half * NODE) + MIDDLE * f(mid) + OUTER * f(mid + half * NODE)
        return half * nodes / TOTAL

    def integrate(lo, hi, whole, depth):
        """adaptive: split while the halves disagree with the whole"""
        mid = (lo + hi) / 2
        left, right = gauss(lo, mid), gauss(mid, hi)
        both = left + right
        if depth == 0 or abs(both - whole) <= TOLERANCE * (1 + abs(both)):
            return both
        return integrate(lo, mid, left, depth - 1) + integrate(mid, hi, right, depth - 1)

    print("%.10f" % integrate(-LIMIT, LIMIT, gauss(-LIMIT, LIMIT), DEPTH))


main()
