import sys

VERTICES = 1000


def main():
    ends = list(map(int, sys.stdin.read().split()))
    parent = list(range(VERTICES + 1))
    edges = [0] * (VERTICES + 1)  # edges of each component, kept at its root

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for a, b in zip(ends[::2], ends[1::2]):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            edges[rb] += edges[ra]
        edges[rb] += 1
    even = all(edges[v] % 2 == 0 for v in range(1, VERTICES + 1) if parent[v] == v)
    print(1 if even else 0)


main()
