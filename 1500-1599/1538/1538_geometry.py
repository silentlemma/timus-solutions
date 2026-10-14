import sys
from itertools import combinations

ENOUGH = 9  # any 9 points, no three on a line, hold a convex pentagon
SIDES = 5


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    """Indices of the convex hull of (x, y, index) points, counterclockwise."""
    points = sorted(points)
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return [p[2] for p in lower[:-1] + upper[:-1]]


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # by the Erdos-Szekeres theorem the first nine points are enough
    points = [(int(data[1 + 2 * i]), int(data[2 + 2 * i]), i + 1) for i in range(min(n, ENOUGH))]
    for five in combinations(points, SIDES):
        order = hull(five)
        if len(order) == SIDES:
            print("Yes")
            print(*order)
            return
    print("No")


main()
