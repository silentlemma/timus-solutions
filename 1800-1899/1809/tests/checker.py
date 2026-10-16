"""Checker: four distinct cells of the 20 x 20 board in which every potato
sees exactly one other along a row or column with nobody between, moving
as few potatoes as the expected answer does."""

import sys

SIDE = 20
COUNT = 4


class Bad(Exception):
    pass


def sees(p, a, b):
    (xa, ya), (xb, yb) = p[a], p[b]
    if xa != xb and ya != yb:
        return False
    return not any(
        k != a and k != b
        and min(xa, xb) <= x <= max(xa, xb) and min(ya, yb) <= y <= max(ya, yb)
        for k, (x, y) in enumerate(p))


def cells(path):
    v = list(map(int, open(path).read().split()))
    if len(v) != 2 * COUNT:
        raise Bad("expected %d coordinates" % (2 * COUNT))
    return [(v[2 * i], v[2 * i + 1]) for i in range(COUNT)]


def check(source, expected, output):
    start, want = cells(source), cells(expected)
    got = cells(output)
    if len(set(got)) < COUNT or not all(1 <= x <= SIDE and 1 <= y <= SIDE for x, y in got):
        raise Bad("the potatoes must lie on distinct cells of the board")
    for a in range(COUNT):
        seen = sum(sees(got, a, b) for b in range(COUNT) if b != a)
        if seen != 1:
            raise Bad("potato %d sees %d others" % (a + 1, seen))
    moved = sum(s != g for s, g in zip(start, got))
    least = sum(s != w for s, w in zip(start, want))
    if moved != least:
        raise Bad("%d potatoes moved, %d suffice" % (moved, least))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
