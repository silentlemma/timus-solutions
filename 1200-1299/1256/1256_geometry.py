import math
import sys

GOLD = (math.sqrt(5) - 1) / 2
STEPS = 70  # golden-section steps: the bracket shrinks by 0.618 each
SAMPLES = 24  # first look along circle B, before refining


def golden(f, lo, hi):
    """The least value of a function with one minimum on [lo, hi]."""
    a, b = hi - GOLD * (hi - lo), lo + GOLD * (hi - lo)
    fa, fb = f(a), f(b)
    for _ in range(STEPS):
        if fa < fb:
            hi, b, fb = b, a, fa
            a = hi - GOLD * (hi - lo)
            fa = f(a)
        else:
            lo, a, fa = a, b, fb
            b = lo + GOLD * (hi - lo)
            fb = f(b)
    return min(fa, fb)


def main():
    r1, r2, r3, r = map(float, sys.stdin.read().split())
    # a dog is fed from the house itself: then the tour goes to the other
    # dog's circle and back, and nothing shorter exists
    if min(r1, r2) <= r:
        print("%.3f" % (2 * max(max(r1, r2) - r, 0)))
        return
    # posts at (0, 0) and (r3, 0), the house above them
    hx = (r1 * r1 - r2 * r2 + r3 * r3) / (2 * r3) if r3 > 0 else r1
    hy = math.sqrt(max(r1 * r1 - hx * hx, 0))
    bx = r3

    def to_b(px, py):
        """The shortest way from P to the circle of dog B and on home."""
        dx, dy = hx - px, hy - py
        length = math.hypot(dx, dy)
        t = ((bx - px) * dx - py * dy) / (length * length) if length > 0 else 0
        t = min(max(t, 0), 1)
        if math.hypot(px + t * dx - bx, py + t * dy) <= r:
            return length

        def via(phi):
            qx, qy = bx + r * math.cos(phi), r * math.sin(phi)
            return math.hypot(qx - px, qy - py) + math.hypot(hx - qx, hy - qy)

        step = 2 * math.pi / SAMPLES
        best = min(range(SAMPLES), key=lambda k: via(k * step))
        return golden(via, (best - 1) * step, (best + 1) * step)

    # the tour length is convex in P inside dog A's circle, so a golden
    # search over x of golden searches over y finds its least value
    def column(px):
        half = math.sqrt(max(r * r - px * px, 0))
        return golden(lambda py: math.hypot(hx - px, hy - py) + to_b(px, py), -half, half)

    print("%.3f" % golden(column, -r, r))


main()
