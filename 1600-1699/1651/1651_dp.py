import sys

INF = float("inf")


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    chain = [int(w) for w in data[1 : 1 + n]]
    end = chain[-1]
    if chain[0] == end:
        print(end)
        return
    # dp[i]: fewest edges from position i to the final vertex, taking only
    # edges of p from i on; reaching the final vertex anywhere ends it
    dp = [INF] * n
    step = [-1] * n  # where the chosen edge leads
    best = {}  # vertex -> (dp after leaving it, that position), latest first
    dp[n - 1] = 0
    for i in range(n - 2, -1, -1):
        u = chain[i]
        if dp[i + 1] < best.get(u, (INF,))[0]:
            best[u] = (dp[i + 1], i + 1)
        if u == end:
            dp[i] = 0
        elif u in best:
            dp[i] = best[u][0] + 1
            step[i] = best[u][1]
    path = [chain[0]]
    i = 0
    while chain[i] != end:
        i = step[i]
        path.append(chain[i])
    print(" ".join(map(str, path)))


main()
