"""Checker: a strictly convex polygon of 3 to 10 000 integer vertices
within the cake, listed counterclockwise, with no straight angles, that
holds exactly k candles inside or on its border."""

import sys

EDGE = 10 ** 9
MOST = 10000


class Bad(Exception):
    pass


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def half(dx, dy):
    return 0 if dy > 0 or (dy == 0 and dx > 0) else 1


def check(source, expected, output):
    v = list(map(int, open(source).read().split()))
    n, k = v[0], v[1]
    candles = list(zip(v[2::2], v[3::2]))
    words = open(output).read().split()
    if not words or not all(t.lstrip("-").isdigit() for t in words):
        raise Bad("not a list of integers")
    m = int(words[0])
    if not 3 <= m <= MOST or len(words) != 2 * m + 1:
        raise Bad("bad vertex count")
    p = [(int(words[1 + 2 * i]), int(words[2 + 2 * i])) for i in range(m)]
    if any(abs(c) > EDGE for q in p for c in q):
        raise Bad("a vertex is off the cake")
    # strictly convex and counterclockwise: every turn is to the left and
    # the edge directions go round exactly once
    turns = 0
    for i in range(m):
        a, b, c = p[i - 1], p[i], p[(i + 1) % m]
        if a == b:
            raise Bad("an edge has zero length")
        if cross(a, b, c) <= 0:
            raise Bad("vertex %d is not a strict left turn" % (i + 1))
        # a left turn moves the direction on; it wraps past the positive
        # x axis when it goes from the lower half to the upper one
        if half(b[0] - a[0], b[1] - a[1]) > half(c[0] - b[0], c[1] - b[1]):
            turns += 1
    if turns != 1:
        raise Bad("the polygon winds %d times" % turns)
    inside = sum(all(cross(p[i], p[(i + 1) % m], q) >= 0 for i in range(m)) for q in candles)
    if inside != k:
        raise Bad("the piece holds %d candles, not %d" % (inside, k))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
