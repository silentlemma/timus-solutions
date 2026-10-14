import math
import sys

EPS = 1e-9
HALF = 0.5  # a cell goes to an owner who held more than half of it
LETTERS = 26
STRAIGHT = 180  # degrees in a half turn
TRIANGLE = 3  # the fewest corners of a polygon with area


def clip(poly, axis, bound, keep_above):
    """The part of a convex polygon with coordinate axis >= bound (or <=)."""
    out = []
    count = len(poly)
    for i in range(count):
        a, b = poly[i], poly[(i + 1) % count]
        if keep_above:
            in_a, in_b = a[axis] >= bound - EPS, b[axis] >= bound - EPS
        else:
            in_a, in_b = a[axis] <= bound + EPS, b[axis] <= bound + EPS
        if in_a != in_b:
            t = (bound - a[axis]) / (b[axis] - a[axis])
            cross = (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
            out.append(cross)
        if in_b:
            out.append(b)
    return out


def area(poly):
    total = 0.0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2


def main():
    data = sys.stdin.read().split()
    n, alpha = int(data[0]), float(data[1])
    grid = data[2 : 2 + 2 * n]
    size = 2 * (2 * n)  # the new map covers twice the old side
    # owned area of each new cell, per owner letter
    held = [[0.0] * LETTERS for _ in range(size * size)]
    rad = alpha * math.pi / STRAIGHT
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    for row in range(2 * n):
        y = n - 1 - row
        for col in range(2 * n):
            owner = grid[row][col]
            if owner == ".":
                continue
            x = col - n
            # the axes turn clockwise, so the cell turns counterclockwise
            corners = [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
            square = [(px * cos_a - py * sin_a, px * sin_a + py * cos_a) for px, py in corners]
            xs = [p[0] for p in square]
            ys = [p[1] for p in square]
            x_lo = max(-2 * n, math.floor(min(xs) + EPS))
            x_hi = min(2 * n, math.ceil(max(xs) - EPS))
            y_lo = max(-2 * n, math.floor(min(ys) + EPS))
            y_hi = min(2 * n, math.ceil(max(ys) - EPS))
            letter = ord(owner) - ord("a")
            for cy in range(y_lo, y_hi):
                for cx in range(x_lo, x_hi):
                    part = clip(square, 0, cx, True)
                    part = clip(part, 0, cx + 1, False)
                    part = clip(part, 1, cy, True)
                    part = clip(part, 1, cy + 1, False)
                    if len(part) >= TRIANGLE:
                        held[(2 * n - 1 - cy) * size + cx + 2 * n][letter] += area(part)
    out = []
    for r in range(size):
        line = []
        for c in range(size):
            cell = held[r * size + c]
            best = next((i for i in range(LETTERS) if cell[i] > HALF + EPS), -1)
            line.append("." if best < 0 else chr(ord("a") + best))
        out.append("".join(line))
    print("\n".join(out))


main()
