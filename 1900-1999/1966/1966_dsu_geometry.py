import sys


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(point, a, b):
    return (cross(a, b, point) == 0
            and min(a[0], b[0]) <= point[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= point[1] <= max(a[1], b[1]))


def straddles(first, second):
    return (first <= 0 <= second) or (second <= 0 <= first)


def intersects(a, b, c, d):
    if max(min(a[0], b[0]), min(c[0], d[0])) > min(max(a[0], b[0]), max(c[0], d[0])):
        return False
    if max(min(a[1], b[1]), min(c[1], d[1])) > min(max(a[1], b[1]), max(c[1], d[1])):
        return False
    return straddles(cross(a, b, c), cross(a, b, d)) and straddles(cross(c, d, a), cross(c, d, b))


def all_reachable(points, edges):
    size = len(points)
    parent = list(range(size))
    weights = [1] * size

    def find(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(first, second):
        first, second = find(first), find(second)
        if first == second:
            return
        if weights[first] < weights[second]:
            first, second = second, first
        parent[second] = first
        weights[first] += weights[second]

    for a, b in edges:
        union(a, b)
    for i, (a, b) in enumerate(edges):
        for c, d in edges[:i]:
            if intersects(points[a], points[b], points[c], points[d]):
                union(a, c)
        for vertex, point in enumerate(points):
            if on_segment(point, points[a], points[b]):
                union(a, vertex)
    root = find(0)
    return all(find(vertex) == root for vertex in range(size))


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    size, count = next(data), next(data)
    points = [(next(data), next(data)) for _ in range(size)]
    edges = [(next(data) - 1, next(data) - 1) for _ in range(count)]
    print('YES' if all_reachable(points, edges) else 'NO')


if __name__ == '__main__':
    main()
