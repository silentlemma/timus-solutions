import sys

TRIANGLE_SIDES = 3


def chain_size(points):
    hull = []
    for point in points:
        x, y = point
        while len(hull) > 1:
            ax, ay = hull[-2]
            bx, by = hull[-1]
            if (bx - ax) * (y - ay) - (by - ay) * (x - ax) >= 0:
                break
            hull.pop()
        hull.append(point)
    return len(hull)


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(values)
    points = sorted(zip(values, values))
    boundary = chain_size(points) + chain_size(reversed(points)) - 2
    # For collinear points the doubled boundary count gives n - 1 roads.
    print(TRIANGLE_SIDES * n - TRIANGLE_SIDES - boundary)


if __name__ == "__main__":
    main()
