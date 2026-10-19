import sys
from math import hypot, inf


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    xs = [int(v) for v in data[1:2 * n + 1:2]]
    ys = [int(v) for v in data[2:2 * n + 2:2]]
    adjacent = [[] for _ in range(n)]
    for k in range(n - 1):
        a, b = int(data[2 * n + 1 + 2 * k]) - 1, int(data[2 * n + 2 + 2 * k]) - 1
        adjacent[a].append(b)
        adjacent[b].append(a)
    order, parent = [0], [-1] * n
    for u in order:
        for v in adjacent[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    def far(a, b):
        return hypot(xs[a] - xs[b], ys[a] - ys[b])

    # the walk through a subtree starts at its root and ends at one of its
    # leaves: ends[u] lists them, cost[u] the shortest walk ending at each
    ends, cost = [None] * n, [None] * n
    for u in reversed(order):
        children = [v for v in adjacent[u] if v != parent[u]]
        if not children:
            ends[u], cost[u] = [u], [0.0]
            continue
        k = len(children)
        # link[a][b]: leave child a at its best end and fly to child b
        link = [[min(c + far(e, b) for e, c in zip(ends[a], cost[a])) for b in children]
                for a in children]
        # enter[m][b]: the children in mask m are done and b, in m, came last
        enter = [[inf] * k for _ in range(1 << k)]
        for b in range(k):
            enter[1 << b][b] = far(u, children[b])
        for m in range(1, 1 << k):
            for a in range(k):
                here = enter[m][a]
                if here == inf:
                    continue
                for b in range(k):
                    if not m >> b & 1:
                        step = here + link[a][b]
                        if step < enter[m | 1 << b][b]:
                            enter[m | 1 << b][b] = step
        full = enter[(1 << k) - 1]
        ends[u] = [e for b in children for e in ends[b]]
        cost[u] = [full[i] + c for i, b in enumerate(children) for c in cost[b]]
        for b in children:
            ends[b] = cost[b] = None
    print("%.10f" % min(c + far(e, 0) for e, c in zip(ends[0], cost[0])))


main()
