import sys
from array import array
from math import gcd


def main():
    # line by line into flat integer rows: half a million links read as one
    # list of words would not fit in the memory limit
    stream = sys.stdin.buffer
    words = []
    while len(words) < 2:
        words += stream.readline().split()
    n, m = int(words[0]), int(words[1])
    cost = [array("i", [0]) * n for _ in range(n)]  # 0: no link, real values are positive
    dist = [array("i", [0]) * n for _ in range(n)]
    left = m
    while left:
        line = stream.readline().split()
        if line:
            a, b, d, c = map(int, line)
            cost[a - 1][b - 1] = cost[b - 1][a - 1] = c
            dist[a - 1][b - 1] = dist[b - 1][a - 1] = d
            left -= 1

    def tree(p, q):
        # Prim on the weights c q - d p, exact integers; returns the tree's
        # total weight, cost and length
        inf = float("inf")
        best = [inf] * n
        bc, bd = [0] * n, [0] * n
        used = [False] * n
        best[0] = 0
        total = tc = td = 0
        for _ in range(n):
            u = min((v for v in range(n) if not used[v]), key=best.__getitem__)
            used[u] = True
            total, tc, td = total + best[u], tc + bc[u], td + bd[u]
            cu, du = cost[u], dist[u]
            for v in range(n):
                c = cu[v]
                if c and not used[v]:
                    w = c * q - du[v] * p
                    if w < best[v]:
                        best[v], bc[v], bd[v] = w, c, du[v]
        return total, tc, td

    # Dinkelbach: the ratio p / q of the last tree drops until no tree beats it
    _, p, q = tree(0, 1)
    while True:
        total, tc, td = tree(p, q)
        if total >= 0:
            break
        g = gcd(tc, td)
        p, q = tc // g, td // g
    print("%.10f" % (p / q))


main()
