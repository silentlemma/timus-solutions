import math
import sys


def lens(d, a, b):
    # area common to discs of radii a and b with centres d apart
    if d >= a + b:
        return 0.0
    if d <= abs(a - b):
        return math.pi * min(a, b) ** 2
    # half-angles seen from each centre, by the law of cosines
    alpha = math.acos((d * d + a * a - b * b) / (2 * d * a))
    beta = math.acos((d * d + b * b - a * a) / (2 * d * b))
    # the kite between both centres and the two crossing points
    kite = math.sqrt((-d + a + b) * (d + a - b) * (d - a + b) * (d + a + b)) / 2
    return a * a * alpha + b * b * beta - kite


def main():
    d, r1, big1, r2, big2 = map(int, sys.stdin.read().split())
    ring1 = math.pi * (big1 * big1 - r1 * r1)
    ring2 = math.pi * (big2 * big2 - r2 * r2)
    # a ring is a disc minus a smaller one, so their overlap follows by
    # inclusion and exclusion over the four pairs of discs
    common = lens(d, big1, big2) - lens(d, r1, big2) - lens(d, big1, r2) + lens(d, r1, r2)
    print(f"{ring1 + ring2 - common:.6f}")


main()
