import sys


def hungarian(cost, n):
    """Smallest total cost of a perfect matching of rows to columns, with
    potentials u, v kept so that reduced costs stay non-negative."""
    inf = float("inf")
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    owner = [0] * (n + 1)
    way = [0] * (n + 1)
    for row in range(1, n + 1):
        owner[0] = row
        col = 0
        low = [inf] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[col] = True
            r = owner[col]
            cr = cost[r - 1]
            ur = u[r]
            delta = inf
            nxt = 0
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cr[j - 1] - ur - v[j]
                    if cur < low[j]:
                        low[j] = cur
                        way[j] = col
                    if low[j] < delta:
                        delta = low[j]
                        nxt = j
            for j in range(n + 1):
                if used[j]:
                    u[owner[j]] += delta
                    v[j] -= delta
                else:
                    low[j] -= delta
            col = nxt
            if owner[col] == 0:
                break
        while col:
            prev = way[col]
            owner[col] = owner[prev]
            col = prev
    return -v[0]


def main():
    tok = list(map(int, sys.stdin.buffer.read().split()))
    n = tok[0]
    rows = [tok[1 + i * n : 1 + (i + 1) * n] for i in range(n)]
    # type j stays in container i; everything else in its column has to move
    cost = [[-x for x in row] for row in rows]
    print(sum(map(sum, rows)) + hungarian(cost, n))


main()
