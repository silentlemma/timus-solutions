import math
import sys

DIM = 8
POINTS = 3


def main():
    nums = map(int, sys.stdin.read().split())
    a, b, c = ([next(nums) for _ in range(DIM)] for _ in range(POINTS))
    r = next(nums)
    ab = [y - x for x, y in zip(a, b)]
    ac = [y - x for x, y in zip(a, c)]
    bc = [y - x for x, y in zip(b, c)]
    length2 = sum(x * x for x in ab)
    ca2, cb2 = sum(x * x for x in ac), sum(x * x for x in bc)
    dot = sum(x * y for x, y in zip(ab, ac))
    # the segment enters the ball when the closest point of it to C lies
    # strictly inside; outside 0 <= t <= 1 the closest point is an end, and
    # both ends are outside: |AC|^2 |AB|^2 - (AB . AC)^2 < R^2 |AB|^2
    if length2 == 0 or not 0 < dot < length2 or ca2 * length2 - dot * dot >= r * r * length2:
        print("%.2f" % math.sqrt(length2))
        return
    # otherwise, in the plane of A, B and C: a tangent from A, an arc of the
    # great circle and a tangent to B
    da, db = math.sqrt(ca2), math.sqrt(cb2)
    angle = math.acos(max(-1.0, min(1.0, (ca2 + cb2 - length2) / (2 * da * db))))
    arc = angle - math.acos(r / da) - math.acos(r / db)
    print("%.2f" % (math.sqrt(ca2 - r * r) + math.sqrt(cb2 - r * r) + r * arc))


main()
