import sys
from operator import add

INF = 1 << 60


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(data), next(data)
    buildings = [(next(data), next(data), next(data)) for _ in range(n)]
    shelters = [(next(data), next(data), next(data)) for _ in range(m)]
    plan = [[next(data) for _ in range(m)] for _ in range(n)]
    dist = [[abs(x - p) + abs(y - q) + 1 for p, q, _ in shelters] for x, y, _ in buildings]
    # nodes 0..m-1 are shelters and m is the spare room; j -> k moves one
    # worker of some building from shelter j to k, j -> m uses a free place
    # at j, and m -> k lets shelter k end up one worker short
    v = m + 1
    w = [[INF] * v for _ in range(v)]
    for i in range(n):
        for j in range(m):
            if plan[i][j]:
                base = dist[i][j]
                w[j][:m] = map(min, w[j][:m], [t - base for t in dist[i]])
    for j in range(m):
        w[j][j] = INF
        if sum(plan[i][j] for i in range(n)) < shelters[j][2]:
            w[j][m] = 0
        w[m][j] = 0
    into = [list(col) for col in zip(*w)]
    # Bellman-Ford from all nodes at once; a change in round v means a
    # negative cycle, which the predecessors lead into
    d, pred = [0] * v, [0] * v
    last = -1
    for _ in range(v):
        last = -1
        for k in range(v):
            vals = list(map(add, d, into[k]))
            best = min(vals)
            if best < d[k]:
                d[k], pred[k], last = best, vals.index(best), k
        if last < 0:
            break
    if last < 0:
        print("OPTIMAL")
        return
    for _ in range(v):
        last = pred[last]
    # shift one worker along each shelter-to-shelter edge of the cycle
    moves, k = [], last
    while True:
        j = pred[k]
        if j < m and k < m:
            _, i = min((dist[i][k] - dist[i][j], i) for i in range(n) if plan[i][j])
            moves.append((i, j, k))
        k = j
        if k == last:
            break
    for i, j, k in moves:
        plan[i][j] -= 1
        plan[i][k] += 1
    print("SUBOPTIMAL")
    print("\n".join(" ".join(map(str, row)) for row in plan))


main()
