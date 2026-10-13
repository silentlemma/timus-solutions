import sys

NONE = -1
INF = float("inf")


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    w = [[INF] * n for _ in range(n)]
    vals = iter(map(int, data[2:]))
    edges = []
    for a, b, c in zip(vals, vals, vals):
        a -= 1
        b -= 1
        w[a][b] = w[b][a] = c
        edges.append((a, b, c))
    # Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
    heaviest = [[0] * n for _ in range(n)]
    dist = w[0][:]
    parent = [0] * n
    done = [False] * n
    done[0] = True
    order = [0]
    in_tree = [[False] * n for _ in range(n)]
    total = 0
    for _ in range(n - 1):
        v = min((d, u) for u, d in enumerate(dist) if not done[u])[1]
        p, c = parent[v], dist[v]
        total += c
        in_tree[p][v] = in_tree[v][p] = True
        row_p, row_v = heaviest[p], heaviest[v]
        for u in order:
            row_v[u] = heaviest[u][v] = max(row_p[u], c)
        done[v] = True
        order.append(v)
        wv = w[v]
        for u in range(n):
            if not done[u] and wv[u] < dist[u]:
                dist[u], parent[u] = wv[u], v
    # the next tree swaps one outside edge for the heaviest edge on its tree path
    swap = min((c - heaviest[a][b] for a, b, c in edges if not in_tree[a][b]), default=None)
    print("Cost: %d" % total)
    print("Cost: %d" % (NONE if swap is None else total + swap))


main()
