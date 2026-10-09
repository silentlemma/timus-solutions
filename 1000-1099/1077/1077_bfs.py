import sys
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]
    rest = data[2:]
    ends = list(zip(rest[0::2], rest[1::2]))[:m]
    adj = [[] for _ in range(n + 1)]
    for i, (a, b) in enumerate(ends):
        adj[a].append((b, i))
        adj[b].append((a, i))
    parent = [0] * (n + 1)
    depth = [-1] * (n + 1)
    tree = [False] * m
    # a breadth-first forest keeps the tree paths, and so the tours, short
    for root in range(1, n + 1):
        if depth[root] >= 0:
            continue
        depth[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, i in adj[u]:
                if depth[v] < 0:
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    tree[i] = True
                    queue.append(v)
    out = []
    # every road outside the forest closes its own tour with the tree path
    for i, (a, b) in enumerate(ends):
        if tree[i]:
            continue
        left, right = [], []
        while depth[a] > depth[b]:
            left.append(a)
            a = parent[a]
        while depth[b] > depth[a]:
            right.append(b)
            b = parent[b]
        while a != b:
            left.append(a)
            right.append(b)
            a, b = parent[a], parent[b]
        cycle = left + [a] + right[::-1]
        out.append("%d %s" % (len(cycle), " ".join(map(str, cycle))))
    sys.stdout.write("\n".join([str(len(out))] + out) + "\n")


main()
