import math
import sys

SLACK = 1e-9  # lets a chain that closes exactly keep its last circle


def invert(x, y, r):
    """The image under inversion in the unit circle around the origin."""
    den = x * x + y * y - r * r
    return x / den, y / den, r / abs(den)


def main():
    big, small, d = (int(w) for w in sys.stdin.read().split())
    # the limit point inside the small circle (the common centre if d = 0):
    # inverting there makes both circles concentric
    b = big * big + d * d - small * small
    twice = 2 * d * big
    p = twice * big / (b + math.sqrt(max(0, b * b - twice * twice)))
    outer_x, _, outer_r = invert(-p, 0.0, big)
    inner_x, _, inner_r = invert(d - p, 0.0, small)
    centre = (outer_x + inner_x) / 2
    mid = (outer_r + inner_r) / 2
    half = abs(outer_r - inner_r) / 2
    # there every chain circle has radius half and turns by step around the
    # centre; the chain stops once one more would overlap the first
    step = 2 * math.asin(half / mid)
    count = int(2 * math.pi / step + SLACK)
    span = (count - 1) * step

    def gap(theta):
        x1, y1, r1 = invert(centre + mid * math.cos(theta), mid * math.sin(theta), half)
        theta += span
        x2, y2, r2 = invert(centre + mid * math.cos(theta), mid * math.sin(theta), half)
        return math.hypot(x1 - x2, y1 - y2) - r1 - r2

    # the best chain is symmetric about the line through the centres
    best = min(gap(-span / 2), gap(math.pi - span / 2))
    print("%.10f" % max(0.0, best))


main()
