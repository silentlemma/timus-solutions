import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    pairs = data[2 : 2 + 2 * m]
    a = [int(x) for x in pairs[::2]]
    b = [int(x) for x in pairs[1::2]]
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[a[i]].append(i)
        adj[b[i]].append(i)
    # breadth-first order from city 1 with the road to each parent
    parent = [0] * (n + 1)
    up = [-1] * (n + 1)
    order = [1]
    parent[1] = -1
    for v in order:
        for e in adj[v]:
            u = a[e] + b[e] - v
            if u != parent[v]:
                parent[u], up[u] = v, e
                order.append(u)
    # leaves first: close the road to the parent while both ends are free
    used = [False] * (n + 1)
    chosen = [False] * m
    for v in reversed(order):
        if up[v] >= 0 and not used[v] and not used[parent[v]]:
            used[v] = used[parent[v]] = True
            chosen[up[v]] = True
    out = ["%d %d" % (a[i], b[i]) for i in range(m) if chosen[i]]
    sys.stdout.write("%d\n" % len(out) + "".join(line + "\n" for line in out))


main()
