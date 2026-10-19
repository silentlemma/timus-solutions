import sys


VERTEX_COUNT = 4


def boundary_count(points):
    boundary_points = set()
    for shift in range(VERTEX_COUNT):
        if shift % 2 == 0:
            first = shift // 2
            opposite = (first + 2) % VERTEX_COUNT
            a = tuple(2 * value for value in points[first])
            b = tuple(2 * value for value in points[opposite])
        else:
            a = tuple(points[0][axis] + points[shift][axis] for axis in range(2))
            remaining = [i for i in range(VERTEX_COUNT) if i not in (0, shift)]
            b = tuple(points[remaining[0]][axis] + points[remaining[1]][axis]
                      for axis in range(2))
        dx, dy = b[0] - a[0], b[1] - a[1]
        if dx == dy == 0:
            continue
        valid = True
        for i, (x, y) in enumerate(points):
            u, v = points[(shift - i) % VERTEX_COUNT]
            if (x + u - a[0]) * dy != (y + v - a[1]) * dx:
                valid = False
                break
            if (x - u) * dx + (y - v) * dy != 0:
                valid = False
                break
        if valid:
            boundary_points.add(a)
            boundary_points.add(b)
    return len(boundary_points)


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    points = [(next(data), next(data)) for _ in range(VERTEX_COUNT)]
    print(boundary_count(points))


if __name__ == '__main__':
    main()
