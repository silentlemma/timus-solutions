import sys
from functools import cmp_to_key

# squared distances carry these denominators: a point scaled by 2, a square
# by its projections
POINT_DEN = 4
SQUARE_DEN = 8


def distance(x1, y1, x2, y2, px, py):
    """Squared distance from P to the square with diagonal (x1, y1)-(x2, y2)
    as an exact fraction (numerator, denominator)."""
    # doubled coordinates of P relative to the centre, and the diagonal
    qx, qy = 2 * px - x1 - x2, 2 * py - y1 - y2
    dx, dy = x2 - x1, y2 - y1
    h = dx * dx + dy * dy
    if h == 0:
        return qx * qx + qy * qy, POINT_DEN
    # projections on the two side directions, the diagonal turned by +-45
    # degrees; inside the square both stay within h
    s1 = abs(qx * (dx - dy) + qy * (dy + dx))
    s2 = abs(qx * (dx + dy) + qy * (dy - dx))
    a, b = max(0, s1 - h), max(0, s2 - h)
    return a * a + b * b, SQUARE_DEN * h


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n = next(tok)
    squares = [(next(tok), next(tok), next(tok), next(tok)) for _ in range(n)]
    px, py = next(tok), next(tok)
    dist = [distance(*sq, px, py) for sq in squares]

    def closer(i, j):
        (ni, di), (nj, dj) = dist[i], dist[j]
        return (ni * dj > nj * di) - (ni * dj < nj * di) or i - j

    print(" ".join(str(i + 1) for i in sorted(range(n), key=cmp_to_key(closer))))


main()
