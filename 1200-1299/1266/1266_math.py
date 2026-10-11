import sys


def main():
    nums = map(int, sys.stdin.read().split())
    n, m = next(nums), next(nums)
    # g[a][b]: total conductance between two nodes
    g = [[0.0] * n for _ in range(n)]
    for _ in range(m):
        a, b, r = next(nums), next(nums), next(nums)
        g[a - 1][b - 1] += 1 / r
        g[b - 1][a - 1] += 1 / r
    # nodes cut off from node 1 carry no current and would make the
    # system singular
    seen, stack = {0}, [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if g[u][v] and v not in seen:
                seen.add(v)
                stack.append(v)
    inner = [v for v in range(1, n - 1) if v in seen]
    # Kirchhoff at each inner node with potential 1 at node 1, 0 at node N
    k = len(inner)
    a = [[0.0] * (k + 1) for _ in range(k)]
    for i, u in enumerate(inner):
        a[i][i] = sum(g[u])
        for j, v in enumerate(inner):
            a[i][j] -= g[u][v]
        a[i][k] = g[u][0]
    for c in range(k):
        p = max(range(c, k), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]
        for r in range(k):
            if r != c and a[r][c]:
                f = a[r][c] / a[c][c]
                for j in range(c, k + 1):
                    a[r][j] -= f * a[c][j]
    volt = [0.0] * n
    volt[0] = 1.0
    for i, u in enumerate(inner):
        volt[u] = a[i][k] / a[i][i]
    current = sum(g[0][v] * (1 - volt[v]) for v in range(1, n))
    print("%.2f" % (1 / current))


main()
