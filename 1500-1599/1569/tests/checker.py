"""Checker: N - 1 channels of the plan that connect all nodes, with the
same largest distance between nodes as the expected network."""

import sys
from collections import deque


def fail(reason):
    print(reason)
    sys.exit(1)


def diameter(n, tree):
    adj = [[] for _ in range(n)]
    for a, b in tree:
        adj[a].append(b)
        adj[b].append(a)
    worst = 0
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if dist[u] < 0:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        if min(dist) < 0:
            return None
        worst = max(worst, max(dist))
    return worst


def read_tree(path, n):
    words = open(path).read().split()
    if len(words) != 2 * (n - 1) or not all(w.isdigit() for w in words):
        return None
    pairs = [(int(words[2 * i]) - 1, int(words[2 * i + 1]) - 1) for i in range(n - 1)]
    if not all(0 <= a < n and 0 <= b < n for a, b in pairs):
        return None
    return pairs


def main():
    source, expected, output = sys.argv[1:4]
    data = open(source).read().split()
    n, m = int(data[0]), int(data[1])
    plan = {frozenset((int(data[2 + 2 * i]), int(data[3 + 2 * i]))) for i in range(m)}
    want = diameter(n, read_tree(expected, n))
    got = read_tree(output, n)
    if got is None:
        fail("expected %d channels between nodes 1..%d" % (n - 1, n))
    if any(frozenset((a + 1, b + 1)) not in plan for a, b in got):
        fail("a channel is not in the plan")
    have = diameter(n, got)
    if have is None:
        fail("the network is not connected")
    if have != want:
        fail("the largest distance is %d, not %d" % (have, want))


main()
