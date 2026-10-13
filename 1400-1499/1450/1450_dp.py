import sys

FIELDS = 3  # a pipeline: from, to and profit


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    out = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(m):
        a, b, c = (int(x) for x in data[2 + FIELDS * i : 2 + FIELDS * (i + 1)])
        out[a].append((b, c))
        indeg[b] += 1
    s, f = int(data[-2]), int(data[-1])
    # the network has no cycles: take the stations in topological order and
    # keep the best profit of a route from S to each of them, None if unreachable
    best = [None] * (n + 1)
    best[s] = 0
    order = [v for v in range(1, n + 1) if indeg[v] == 0]
    for v in order:
        for w, c in out[v]:
            if best[v] is not None and (best[w] is None or best[v] + c > best[w]):
                best[w] = best[v] + c
            indeg[w] -= 1
            if indeg[w] == 0:
                order.append(w)
    print("No solution" if best[f] is None else best[f])


main()
