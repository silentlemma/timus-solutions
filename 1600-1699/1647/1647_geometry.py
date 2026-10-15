import math

CORNERS = 3
ROUNDS = 200  # bisection steps, far beyond double precision


def shoelace(poly):
    twice = 0.0
    for i in range(len(poly)):
        (ax, ay), (bx, by) = poly[i - 1], poly[i]
        twice += ax * by - bx * ay
    return abs(twice) / 2


def main():
    nums = list(map(int, open(0).read().split()))
    pts = list(zip(nums[0::2], nums[1::2]))
    sides = [math.dist(pts[i], pts[(i + 1) % CORNERS]) for i in range(CORNERS)]
    perimeter = sum(sides)
    # arc positions of the corners along the coast, twice round
    corners = []
    pos = 0.0
    for _ in range(2):
        for i in range(CORNERS):
            corners.append((pos, pts[i]))
            pos += sides[i]

    def point(s):
        """the coast point at arc length s from the first corner"""
        s %= perimeter
        for i in range(CORNERS):
            if s <= sides[i] or i == CORNERS - 1:
                t = min(s / sides[i], 1.0)
                (ax, ay), (bx, by) = pts[i], pts[(i + 1) % CORNERS]
                return (ax + (bx - ax) * t, ay + (by - ay) * t)
            s -= sides[i]

    def area(s, t):
        """area cut off by the coast from s to t (s < t) and the chord"""
        return shoelace([point(s)] + [p for at, p in corners if s < at < t] + [point(t)])

    half = perimeter / 2
    total = shoelace(pts)

    def excess(s):
        return area(s, s + half) - total / 2

    # the excess changes sign over half a turn, as the other part is the
    # complement, so a chord splitting both evenly always exists
    lo, hi = 0.0, half
    low = excess(lo)
    for _ in range(ROUNDS):
        mid = (lo + hi) / 2
        if (excess(mid) > 0) == (low > 0):
            lo = mid
        else:
            hi = mid
    s = (lo + hi) / 2
    print("YES")
    for x, y in (point(s), point(s + half)):
        print("%.12f %.12f" % (x, y))


main()
