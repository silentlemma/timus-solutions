import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    nums = iter(map(int, data[1:]))
    for _ in range(n - 1):
        a, b, c = next(nums), next(nums), next(nums)
        adj[a].append((b, c))
        adj[b].append((a, c))
    # an edge with s branches on one side carries the s (n - s) pairs that
    # it separates; sizes come from a parents-first order read backwards
    parent, cost = [0] * (n + 1), [0] * (n + 1)
    parent[1] = -1
    order = [1]
    for v in order:
        for u, c in adj[v]:
            if u != parent[v]:
                parent[u], cost[u] = v, c
                order.append(u)
    size = [1] * (n + 1)
    total = 0
    for v in reversed(order[1:]):
        size[parent[v]] += size[v]
        total += cost[v] * size[v] * (n - size[v])
    # every pair is counted in both directions
    print("%.4f" % (2 * total / (n * (n - 1))))


main()
