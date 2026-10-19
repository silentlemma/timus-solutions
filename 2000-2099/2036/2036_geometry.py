import sys

TRIANGLE = 3
CORNERS = 4
CLOSED = 5


def cross(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def parallelogram(p):
    a, b, c, d = p
    return any(
        u[0] + v[0] == w[0] + z[0] and u[1] + v[1] == w[1] + z[1]
        for u, v, w, z in ((a, b, c, d), (a, c, b, d), (a, d, b, c))
    )


def solve(points):
    n = len(points)
    if n <= TRIANGLE:
        return str(n)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        outside = 0
        for p in points:
            if cross(points[i], points[j], p):
                outside += 1
                if outside > 1:
                    break
        if outside <= 1:
            return str(n)
    if n == CORNERS:
        return str(CLOSED) if parallelogram(points) else "oo"
    if n == CLOSED:
        for center in range(n):
            others = [p for i, p in enumerate(points) if i != center]
            if parallelogram(others) and all(
                sum(p[axis] for p in others) == CORNERS * points[center][axis] for axis in (0, 1)
            ):
                return str(CLOSED)
    return "oo"


def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(values)
    points = [(next(values), next(values)) for _ in range(n)]
    print(solve(points))


if __name__ == "__main__":
    main()
