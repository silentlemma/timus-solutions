import sys
from functools import cmp_to_key


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def main():
    tok = list(map(int, sys.stdin.buffer.read().split()))
    n = tok[0]
    pts = list(zip(tok[1::2], tok[2::2]))[:n]
    # A is the lowest point and B the next one on the hull, so every other
    # point lies on the left of AB and sees it under an angle below 180
    a = min(pts, key=lambda p: (p[1], p[0]))
    rest = [p for p in pts if p != a]
    b = rest[0]
    for p in rest:
        if cross(a, b, p) < 0:
            b = p
    others = [p for p in rest if p != b]

    def key(p):
        # the angle APB grows as its cotangent dot / cross falls
        dot = (a[0] - p[0]) * (b[0] - p[0]) + (a[1] - p[1]) * (b[1] - p[1])
        return dot, cross(p, a, b)

    def by_angle(p, q):
        (dp, cp), (dq, cq) = key(p), key(q)
        return (dq * cp > dp * cq) - (dq * cp < dp * cq)

    others.sort(key=cmp_to_key(by_angle))
    # points seeing AB under a larger angle than C lie inside the circle ABC
    c = others[len(others) // 2]
    print("\n".join("%d %d" % p for p in (a, b, c)))


main()
