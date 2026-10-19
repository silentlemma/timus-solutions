OUTPUT_DIGITS = 10


def solve(points):
    unique = []
    counts = []
    for point in sorted(points):
        if unique and unique[-1] == point:
            counts[-1] += 1
        else:
            unique.append(point)
            counts.append(1)
    n = len(points)
    m = len(unique)
    x = [point[0] for point in unique]
    y = [point[1] for point in unique]
    wx = [x[i] * counts[i] for i in range(m)]
    wy = [y[i] * counts[i] for i in range(m)]
    tx, ty = sum(wx), sum(wy)
    best = [0] * (n + 1)
    best[n] = tx * tx + ty * ty

    # An optimal subset is separated from every distinct excluded vector by
    # projection onto its sum. Rotate a separating line through each pivot.
    # Complements cover the other half-turn. Only one pivot's events are stored.
    for pivot in range(m):
        xp, yp = x[pivot], y[pivot]
        sx = sy = size = 0
        events = []
        slopes = [0.0] * m
        delta_x = [0] * m
        delta_y = [0] * m
        delta_size = [0] * m
        for other in range(m):
            dx, dy = x[other] - xp, y[other] - yp
            if dy > 0 or (dy == 0 and dx < 0):
                sx += wx[other]
                sy += wy[other]
                size += counts[other]
            if dy:
                events.append(other)
                slopes[other] = -dx / dy
                if dy > 0:
                    delta_x[other] = -wx[other]
                    delta_y[other] = -wy[other]
                    delta_size[other] = -counts[other]
                else:
                    delta_x[other] = wx[other]
                    delta_y[other] = wy[other]
                    delta_size[other] = counts[other]

        # Coordinate bounds keep distinct rational slopes well beyond float
        # rounding error. Equal slopes may toggle in any order: all intermediate
        # sums are actual subsets, and every strictly separated subset is visited.
        events.sort(key=slopes.__getitem__)
        events.append(pivot)
        for copies in range(1, counts[pivot] + 1):
            a, b = sx + copies * xp, sy + copies * yp
            k = size + copies
            for other in events:
                norm = a * a + b * b
                if norm > best[k]:
                    best[k] = norm
                opposite_x, opposite_y = tx - a, ty - b
                norm = opposite_x * opposite_x + opposite_y * opposite_y
                if norm > best[n - k]:
                    best[n - k] = norm
                a += delta_x[other]
                b += delta_y[other]
                k += delta_size[other]
    return best[1:]


if __name__ == "__main__":
    import math
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    points = list(zip(data[1::2], data[2::2]))
    print("\n".join(f"{math.sqrt(value):.{OUTPUT_DIGITS}f}" for value in solve(points)))
