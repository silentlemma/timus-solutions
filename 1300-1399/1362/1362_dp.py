import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    pos = 1
    for boss in range(1, n + 1):
        while data[pos] != b"0":
            v = int(data[pos])
            adj[boss].append(v)
            adj[v].append(boss)
            pos += 1
        pos += 1
    root = int(data[pos])
    # calls go both up and down, so the news spreads over the tree rooted
    # at Tanya; order parents before children
    parent = [0] * (n + 1)
    parent[root] = -1
    order = [root]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    # time[v]: minutes v needs to tell its whole subtree; the slowest
    # subtrees are called first, the i-th call starting at minute i
    time = [0] * (n + 1)
    kids = [[] for _ in range(n + 1)]
    for v in reversed(order):
        times = sorted(kids[v], reverse=True)
        time[v] = max((t + i for i, t in enumerate(times, 1)), default=0)
        if parent[v] > 0:
            kids[parent[v]].append(time[v])
    print(time[root])


main()
