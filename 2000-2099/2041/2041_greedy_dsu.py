"""Largest eligible inner bound, with a balanced deletion-only predecessor DSU."""

from bisect import bisect_left
import sys


def solve(dolls):
    items = sorted((a, b, i + 1) for i, (a, b) in enumerate(dolls))
    inner = [item[0] for item in items]
    n = len(items)
    parent = list(range(n + 1))
    best = parent.copy()
    rank = bytearray(n + 1)

    def find(index):
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    limit = max(b for a, b in dolls) + 1
    answer = []
    for _ in range(n):
        root = find(bisect_left(inner, limit))
        position = best[root]
        if not position:
            return None
        _, limit, index = items[position - 1]
        answer.append(index)
        left = find(position - 1)
        if rank[root] < rank[left]:
            root, left = left, root
        parent[left] = root
        best[root] = min(best[root], best[left])
        if rank[root] == rank[left]:
            rank[root] += 1
    return answer


def main():
    n = int(sys.stdin.buffer.readline())
    dolls = [tuple(map(int, sys.stdin.buffer.readline().split())) for _ in range(n)]
    answer = solve(dolls)
    if answer is None:
        print("No")
    else:
        print("Yes")
        print(*answer)


if __name__ == "__main__":
    main()
