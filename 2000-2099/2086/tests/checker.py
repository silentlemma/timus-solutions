"""Checker: the same number of points as expected and the same points in any
order, each coordinate within an absolute or relative error of 10^-6."""

import sys

EPS = 1e-6


class Bad(Exception):
    pass


def points(path):
    words = open(path).read().split()
    if not words or not words[0].isdigit():
        raise Bad("no count")
    n = int(words[0])
    if len(words) != 1 + 2 * n:
        raise Bad("expected %d points" % n)
    try:
        values = [float(w) for w in words[1:]]
    except ValueError:
        raise Bad("not a number")
    return [(values[2 * i], values[2 * i + 1]) for i in range(n)]


def close(a, b):
    return abs(a - b) <= EPS * max(1.0, abs(b))


def check(source, expected, output):
    want, got = points(expected), points(output)
    if len(want) != len(got):
        raise Bad("expected %d points, got %d" % (len(want), len(got)))
    free = list(got)
    for p in want:
        match = [q for q in free if close(q[0], p[0]) and close(q[1], p[1])]
        if not match:
            raise Bad("missing the point %.9f %.9f" % p)
        free.remove(match[0])


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
