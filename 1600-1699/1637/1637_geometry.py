from itertools import permutations

CORNERS = 3
GLIDE = 3  # a glide reflection takes three reflections


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def bisector(p, q):
    """the line a x + b y = c of points as far from p as from q"""
    return (2 * (q[0] - p[0]), 2 * (q[1] - p[1]), dist2(q, (0, 0)) - dist2(p, (0, 0)))


def same_line(u, v):
    return u[0] * v[1] == u[1] * v[0] and u[0] * v[2] == u[2] * v[0] and u[1] * v[2] == u[2] * v[1]


def moves(cur, to):
    """reflections taking cur[i] to to[i], or None when no isometry does"""
    if any(dist2(cur[i], cur[j]) != dist2(to[i], to[j]) for i, j in ((0, 1), (0, 2), (1, 2))):
        return None
    if cur == to:
        return 0
    if (cross(*cur) > 0) == (cross(*to) > 0):
        return 2  # a rotation or a translation: two reflections
    # orientation reversed: one reflection if a single mirror fits all three
    lines = [bisector(p, q) for p, q in zip(cur, to) if p != q]
    fixed = [p for p, q in zip(cur, to) if p == q]
    mirror = lines[0]
    if all(same_line(mirror, line) for line in lines) and all(
        mirror[0] * p[0] + mirror[1] * p[1] == mirror[2] for p in fixed
    ):
        return 1
    return GLIDE


def main():
    nums = list(map(int, open(0).read().split()))
    points = list(zip(nums[0::2], nums[1::2]))
    target, cur = points[:CORNERS], points[CORNERS:]
    options = [moves(cur, list(to)) for to in permutations(target)]
    options = [m for m in options if m is not None]
    print(min(options) if options else "IMPOSSIBLE")


main()
