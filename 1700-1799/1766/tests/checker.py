"""Checker: 64 probabilities, each within 1e-12 of the settled
distribution, which is computed exactly from the input: a cell is
weighted by its count times the sum of the counts around it."""

import sys
from fractions import Fraction

SIDE = 8
LIMIT = 1e-12


class Bad(Exception):
    pass


def check(source, expected, output):
    v = [int(w) for w in open(source).read().split()]
    score = []
    for r in range(SIDE):
        for c in range(SIDE):
            around = sum(v[y * SIDE + x] for y in range(r - 1, r + 2) for x in range(c - 1, c + 2)
                         if 0 <= y < SIDE and 0 <= x < SIDE and (y, x) != (r, c))
            score.append(v[r * SIDE + c] * around)
    total = sum(score)
    got = open(output).read().split()
    if len(got) != SIDE * SIDE:
        raise Bad("expected %d numbers, got %d" % (SIDE * SIDE, len(got)))
    for i, (w, s) in enumerate(zip(got, score)):
        try:
            value = Fraction(w)
        except ValueError:
            raise Bad("cell %d is not a number" % (i + 1))
        if abs(value - Fraction(s, total)) > LIMIT:
            raise Bad("cell %d is %s, off by more than 1e-12" % (i + 1, w))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
