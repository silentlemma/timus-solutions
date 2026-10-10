import math
import sys

# halvings of the radius interval; far more than double precision needs
STEPS = 200


def main():
    tok = list(map(int, sys.stdin.read().split()))
    n, sides = tok[0], sorted(tok[1 : 1 + tok[0]])
    longest, rest = sides[-1], sides[:-1]
    if longest >= sum(rest):
        print("0.00")
        return

    # the largest area belongs to the polygon inscribed in a circle; a side
    # of length l sees the centre at the angle 2 asin(l / 2R)
    def angle(length, r):
        return 2 * math.asin(min(1.0, length / (2 * r)))

    low = longest / 2
    inside = sum(angle(s, low) for s in sides) >= 2 * math.pi

    # with the centre inside, the angles fill the full turn; otherwise the
    # longest side's angle equals the sum of the others
    def surplus(r):
        if inside:
            return sum(angle(s, r) for s in sides) - 2 * math.pi
        return angle(longest, r) - sum(angle(s, r) for s in rest)

    high = low
    while surplus(high) > 0:
        high *= 2
    for _ in range(STEPS):
        mid = (low + high) / 2
        if surplus(mid) > 0:
            low = mid
        else:
            high = mid
    r = (low + high) / 2
    area = sum(math.sin(angle(s, r)) for s in rest)
    area += math.sin(angle(longest, r)) if inside else -math.sin(angle(longest, r))
    print("%.2f" % (r * r * area / 2))


main()
