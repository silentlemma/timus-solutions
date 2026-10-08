import sys

INF = 1 << 30
END_OF_INPUT = -1
NO_SOLUTION = "No solution."
TOKENS_PER_ROAD = 3


def solve(n, roads):
    edge = [[INF] * n for _ in range(n)]  # the lightest direct road
    for i in range(n):
        edge[i][i] = 0
    for a, b, length in roads:
        if length < edge[a][b]:
            edge[a][b] = edge[b][a] = length
    dist = [row[:] for row in edge]
    nxt = [list(range(n)) for _ in range(n)]

    # Floyd-Warshall; before vertex k becomes an intermediate, dist[i][j] uses
    # only vertices below k, so i..j plus j-k-i is a simple cycle through k.
    best, cycle = INF, None
    for k in range(n):
        ek = edge[k]
        for i in range(k):
            eik = edge[i][k]
            if eik == INF:
                continue
            di = dist[i]
            for j in range(i + 1, k):
                if ek[j] != INF and di[j] != INF and di[j] + eik + ek[j] < best:
                    best = di[j] + eik + ek[j]
                    cycle = [i]
                    while cycle[-1] != j:
                        cycle.append(nxt[cycle[-1]][j])
                    cycle.append(k)
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            di, ni = dist[i], nxt[i]
            nik = ni[k]
            for j in range(n):
                d = dik + dk[j]
                if d < di[j]:
                    di[j] = d
                    ni[j] = nik
    if cycle is None:
        return NO_SOLUTION
    return " ".join(str(v + 1) for v in cycle)


def main():
    data = sys.stdin.buffer.read().split()
    pos, out = 0, []
    while int(data[pos]) != END_OF_INPUT:
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        roads = []
        for _ in range(m):
            a, b, length = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            roads.append((a - 1, b - 1, length))
            pos += TOKENS_PER_ROAD
        out.append(solve(n, roads))
    sys.stdout.write("\n".join(out) + "\n")


main()
