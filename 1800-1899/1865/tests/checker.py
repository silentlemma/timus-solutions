"""Checker: "Impossible" exactly when the expected output says so;
otherwise a polyline of at most 1000 integer vertices from the north
coast to the south coast, alternating vertical and horizontal segments of
nonzero length, away from the west and east coasts, without touching
itself, not entering the lighthouse, with the lighthouse on its east side
and half of the island there."""

import sys

MOST_VERTICES = 1000


class Bad(Exception):
    pass


def crosses_inside(a, b, x, y, d):
    # does segment ab have a point strictly inside the lighthouse
    low_x, high_x = min(a[0], b[0]), max(a[0], b[0])
    low_y, high_y = min(a[1], b[1]), max(a[1], b[1])
    return low_x < x + d and high_x > x and low_y < y + d and high_y > y


def meet(a, b, c, e):
    # do the closed axis-parallel segments ab and ce share a point
    return (max(min(a[0], b[0]), min(c[0], e[0])) <= min(max(a[0], b[0]), max(c[0], e[0])) and
            max(min(a[1], b[1]), min(c[1], e[1])) <= min(max(a[1], b[1]), max(c[1], e[1])))


def check(source, expected, output):
    w, h, x, y, d = map(int, open(source).read().split())
    impossible = open(expected).read().split() == ["Impossible"]
    words = open(output).read().split()
    if words == ["Impossible"]:
        if not impossible:
            raise Bad("a border exists")
        return
    if impossible:
        raise Bad("no border exists")
    if not words or not all(v.lstrip("-").isdigit() for v in words):
        raise Bad("not a list of integers")
    k = int(words[0])
    if not 2 <= k <= MOST_VERTICES or len(words) != 2 * k + 1:
        raise Bad("bad vertex count")
    p = [(int(words[1 + 2 * i]), int(words[2 + 2 * i])) for i in range(k)]
    if p[0][1] != h or p[-1][1] != 0:
        raise Bad("does not run from north to south")
    for i, (px, py) in enumerate(p):
        if not 0 < px < w or not 0 <= py <= h or (0 < i < k - 1 and not 0 < py < h):
            raise Bad("vertex %d touches a coast" % (i + 1))
    segments = list(zip(p, p[1:]))
    for i, (a, b) in enumerate(segments):
        vertical = i % 2 == 0
        if a == b or (a[0] != b[0] if vertical else a[1] != b[1]):
            raise Bad("segment %d has the wrong direction or no length" % (i + 1))
        if crosses_inside(a, b, x, y, d):
            raise Bad("segment %d enters the lighthouse" % (i + 1))
    if len(segments) % 2 == 0:
        raise Bad("the last segment is not vertical")
    for i in range(len(segments)):
        for j in range(i + 2, len(segments)):
            if meet(*segments[i], *segments[j]):
                raise Bad("segments %d and %d touch" % (i + 1, j + 1))
    ring = p + [(w, 0), (w, h)]
    twice = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(ring, ring[1:] + ring[:1]))
    if abs(twice) != w * h:
        raise Bad("the areas differ")
    # the centre of the lighthouse's south-west cell, doubled
    cx, cy = 2 * x + 1, 2 * y + 1
    inside = False
    for a, b in zip(ring, ring[1:] + ring[:1]):
        if a[0] == b[0] and 2 * a[0] > cx and min(a[1], b[1]) * 2 < cy < max(a[1], b[1]) * 2:
            inside = not inside
    if not inside:
        raise Bad("the lighthouse is in Sweden")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
