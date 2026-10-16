import math
import sys
from itertools import permutations

FIELDS = 10


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])


def turn(u, w):
    return u[0] * w[1] - u[1] * w[0]


def dot(u, w):
    return u[0] * w[0] + u[1] * w[1]


def within(u, v, w):
    # whether the ray w lies in the closed sector turning left from u to v
    c = turn(u, v)
    if c > 0:
        return turn(u, w) >= 0 and turn(w, v) >= 0
    if c < 0:
        return not (turn(v, w) > 0 and turn(w, u) > 0)
    return turn(u, w) >= 0


def same_side_at_bend(a, b, c, x, y):
    # rays from the bend b towards x and y stay on one side of the ravine
    u, v, p, q = vec(b, a), vec(b, c), vec(b, x), vec(b, y)
    if turn(u, v) == 0 and dot(u, v) > 0:
        # both pieces leave b the same way: b is a free tip
        return True
    return (within(u, v, p) and within(u, v, q)) or (within(v, u, p) and within(v, u, q))


def strictly_inside(p, a, b):
    return cross(a, b, p) == 0 and dot(vec(p, a), vec(p, b)) < 0


def crosses(p, q, a, b):
    o1, o2 = cross(p, q, a), cross(p, q, b)
    o3, o4 = cross(a, b, p), cross(a, b, q)
    return o1 * o2 < 0 and o3 * o4 < 0


def allowed(path, a, b, c):
    for p, q in zip(path, path[1:]):
        if crosses(p, q, a, b) or crosses(p, q, b, c):
            return False
        # going straight through the bend must not change sides there
        if strictly_inside(b, p, q) and not same_side_at_bend(a, b, c, p, q):
            return False
    for x, v, y in zip(path, path[1:], path[2:]):
        if v == b and not same_side_at_bend(a, b, c, x, y):
            return False
        # an end of the ravine lying inside the other piece is no corner
        for end, (e1, e2) in ((a, (b, c)), (c, (a, b))):
            if v == end and strictly_inside(end, e1, e2):
                if cross(e1, e2, x) * cross(e1, e2, y) < 0:
                    return False
    return True


def main():
    data = list(map(int, sys.stdin.read().split()))
    out = []
    for t in range(data[0]):
        v = data[1 + FIELDS * t:1 + FIELDS * (t + 1)]
        s, e, a, b, c = (tuple(v[i:i + 2]) for i in range(0, FIELDS, 2))
        # a shortest way bends only at points of the ravine, at most once at
        # each of A, B and C; the shortest allowed candidate is the answer
        candidates = []
        for k in range(len((a, b, c)) + 1):
            for middle in permutations((a, b, c), k):
                path = (s,) + middle + (e,)
                size = sum(math.dist(p, q) for p, q in zip(path, path[1:]))
                candidates.append((size, path))
        candidates.sort()
        best = next(size for size, path in candidates if allowed(path, a, b, c))
        out.append("%.6f" % best)
    print("\n".join(out))


main()
