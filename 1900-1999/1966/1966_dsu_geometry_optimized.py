import sys


def intersects(a, b, c, d):
    dx, dy = b[0] - a[0], b[1] - a[1]
    first = dx * (c[1] - a[1]) - dy * (c[0] - a[0])
    second = dx * (d[1] - a[1]) - dy * (d[0] - a[0])
    if first * second > 0:
        return False
    dx, dy = d[0] - c[0], d[1] - c[1]
    first = dx * (a[1] - c[1]) - dy * (a[0] - c[0])
    second = dx * (b[1] - c[1]) - dy * (b[0] - c[0])
    return first * second <= 0


def connected(points, edges):
    parent = [-1] * len(points)
    components = len(points)

    def root(vertex):
        while parent[vertex] >= 0:
            vertex = parent[vertex]
        return vertex

    def union(a, b):
        nonlocal components
        a, b = root(a), root(b)
        if a != b:
            if parent[a] > parent[b]:
                a, b = b, a
            parent[a] += parent[b]
            parent[b] = a
            components -= 1

    tracks = []
    for i, j in set((min(a, b), max(a, b)) for a, b in edges):
        union(i, j)
        a, b = points[i], points[j]
        if a[0] > b[0]:
            a, b = b, a
        tracks.append((a[0], b[0], min(a[1], b[1]), max(a[1], b[1]), i, a, b))
    if components == 1:
        return True

    tracks.sort()
    # Components with no segment endpoint can only be joined through an interior mark.
    for vertex, links in enumerate(parent):
        if links != -1:
            continue
        x, y = points[vertex]
        for x0, x1, y0, y1, i, a, b in tracks:
            if x0 > x:
                break
            if x <= x1 and y0 <= y <= y1:
                if (b[0] - a[0]) * (y - a[1]) == (b[1] - a[1]) * (x - a[0]):
                    union(i, vertex)
                    break
        if parent[vertex] == -1:
            return False
    if components == 1:
        return True

    for index, (x0, x1, y0, y1, i, a, b) in enumerate(tracks):
        for other in range(index + 1, len(tracks)):
            x2, _, y2, y3, j, c, d = tracks[other]
            if x2 > x1:
                break
            if y0 <= y3 and y2 <= y1 and root(i) != root(j) and intersects(a, b, c, d):
                union(i, j)
                if components == 1:
                    return True
    return False


def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    count, length = next(numbers), next(numbers)
    points = [(next(numbers), next(numbers)) for _ in range(count)]
    edges = [(next(numbers) - 1, next(numbers) - 1) for _ in range(length)]
    print("YES" if connected(points, edges) else "NO")


if __name__ == "__main__":
    main()
