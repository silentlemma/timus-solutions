import sys
from math import sqrt

SCALE = 100  # coordinates come with two decimals: work in hundredths
SIZES = 3  # A, B and C


def hundredths(text):
    whole, _, part = text.partition(".")
    sign = -1 if whole.startswith("-") else 1
    return int(whole) * SCALE + sign * int((part + "00")[:2])


def fold(a, b, c, x, y):
    """The point of the box for the point (x, y) of the net.

    The face A x B in the middle of the column lies at z = 0 with its
    corner (c, b + c) at the origin; every other face folds up from it."""
    if x < c:
        return (0, y - b - c, c - x)
    if x > c + a:
        return (a, y - b - c, x - c - a)
    if y < b:
        return (x - c, b - y, c)
    if y < b + c:
        return (x - c, 0, b + c - y)
    if y <= 2 * b + c:
        return (x - c, y - b - c, 0)
    return (x - c, b, y - 2 * b - c)


def main():
    data = sys.stdin.read().split()
    a, b, c = (int(v) * SCALE for v in data[:SIZES])
    x1, y1, x2, y2 = (hundredths(v) for v in data[SIZES:])
    p, q = fold(a, b, c, x1, y1), fold(a, b, c, x2, y2)
    squared = sum((u - v) ** 2 for u, v in zip(p, q))
    print("%.10f" % (sqrt(squared) / SCALE))


main()
