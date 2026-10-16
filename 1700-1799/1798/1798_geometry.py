import sys
from math import isqrt

QUARTERS = 4


def column_sum(n, m):
    """Sum of isqrt(n - x*x) over x = 0 .. m, where 2*m*m <= n.

    The columns are summed by walking from m to the left along the upper
    hull of the lattice points in the disk, one edge at a time; a vector
    (a, b) moves a columns left and b rows up.
    """
    x, y = m, isqrt(n - m * m)
    total = y
    stack = [(1, 0), (1, 1)]
    while x > 0:
        a1, b1 = stack.pop()
        while True:
            nx, ny = x - a1, y + b1
            if nx < 0 or nx * nx + ny * ny > n:
                break
            # the columns nx .. x - 1 lie under this hull edge
            total += a1 * y + (a1 - 1) * (b1 - 1) // 2 + b1
            x, y = nx, ny
        if x - a1 < 0:
            break
        a2, b2 = a1, b1
        while True:
            a1, b1 = stack[-1]
            nx, ny = x - a1, y + b1
            if nx * nx + ny * ny <= n:
                break
            a2, b2 = a1, b1
            stack.pop()
        while True:
            a12, b12 = a1 + a2, b1 + b2
            nx, ny = x - a12, y + b12
            if nx < 0:
                break
            if nx * nx + ny * ny <= n:
                stack.append((a12, b12))
                a1, b1 = a12, b12
            else:
                # from the outside point nx, steps of (a1, b1) rise at least
                # as fast as the circle, so no inside point lies between
                if b1 * b1 * (n - nx * nx) >= a1 * a1 * nx * nx:
                    break
                a2, b2 = a12, b12
    for column in range(x):
        total += isqrt(n - column * column)
    return total


def main():
    radius = int(sys.stdin.read())
    # slab (x, y) of the first quarter burns when its nearest corner is
    # strictly inside the circle: x*x + y*y <= radius^2 - 1
    n = radius * radius - 1
    m = isqrt(n // 2)
    total = column_sum(n, m)
    # points with x < y twice, then the diagonal once
    quarter = 2 * (total - m * (m + 1) // 2) + m + 1
    print(QUARTERS * quarter)


main()
