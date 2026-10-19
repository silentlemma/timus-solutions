"""Checker: "Impossible" exactly when the expected output says so;
otherwise n points with integer coordinates of absolute value at most
10^6 whose squared distances are the given ones."""

import sys

LIMIT = 10 ** 6


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n = int(data[0])
    d = [[int(v) for v in data[1 + i * n:1 + (i + 1) * n]] for i in range(n)]
    impossible = open(expected).read().split() == ["Impossible"]
    words = open(output).read().split()
    if words == ["Impossible"]:
        if not impossible:
            raise Bad("the atoms can be placed")
        return
    if impossible:
        raise Bad("the atoms cannot be placed")
    if len(words) != 2 * n or not all(v.lstrip("-").isdigit() for v in words):
        raise Bad("expected %d pairs of integers" % n)
    v = [int(t) for t in words]
    if any(abs(t) > LIMIT for t in v):
        raise Bad("a coordinate is too large")
    xs, ys = v[0::2], v[1::2]
    for i in range(n):
        for j in range(i):
            if (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2 != d[i][j]:
                raise Bad("atoms %d and %d are at the wrong distance" % (j + 1, i + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
