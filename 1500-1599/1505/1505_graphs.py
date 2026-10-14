import heapq
import sys


def main():
    data = sys.stdin.read()
    head, _, rest = data.lstrip().partition("\n")
    n = int(head)
    # every station's description ends with a dot, whatever the line breaks
    lines = rest.split(".")[:n]
    origin, target, cap, flow, cost = [], [], [], [], []
    out = [[] for _ in range(n + 1)]  # pipe ids leaving each station
    into = [[] for _ in range(n + 1)]  # pipe ids entering each station
    balance = [0] * (n + 1)  # outflow minus inflow
    for i, line in enumerate(lines, 1):
        for quad in line.split(","):
            if not quad.strip():
                continue
            a, b, c, d = map(int, quad.split())
            out[i].append(len(target))
            into[a].append(len(target))
            origin.append(i)
            target.append(a)
            cap.append(b)
            flow.append(c)
            cost.append(d)
            balance[i] += c
            balance[a] -= c

    # one more unit from any station with a well to station n through the
    # residual network: a pipe with spare room is free, a full one costs d,
    # and pushing back existing flow is free
    inf = float("inf")
    dist = [inf] * (n + 1)
    came = [None] * (n + 1)  # (pipe, +1 forward or -1 backward)
    heap = []
    for i in range(1, n):
        if balance[i] > 0:
            dist[i] = 0
            heap.append((0, i))
    heapq.heapify(heap)
    while heap:
        du, u = heapq.heappop(heap)
        if du > dist[u]:
            continue
        for e in out[u]:
            nd = du + (cost[e] if flow[e] == cap[e] else 0)
            v = target[e]
            if nd < dist[v]:
                dist[v], came[v] = nd, (e, 1)
                heapq.heappush(heap, (nd, v))
        for e in into[u]:
            if flow[e] > 0:
                v = origin[e]
                if du < dist[v]:
                    dist[v], came[v] = du, (e, -1)
                    heapq.heappush(heap, (du, v))
    if dist[n] == inf:
        print("Impossible")
        return

    v = n
    while came[v]:
        e, step = came[v]
        flow[e] += step
        v = origin[e] if step == 1 else target[e]
    res = [str(dist[n])]
    for i in range(1, n + 1):
        res.append(", ".join("%d %d" % (target[e], flow[e]) for e in out[i]) + ".")
    print("\n".join(res))


main()
