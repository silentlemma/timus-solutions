import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n, m, q = next(data), next(data), next(data)
    size = n
    edges = []
    for _ in range(m):
        u, v, s, w = next(data), next(data), next(data), next(data)
        edges.append((u, v, s, w))
        size = max(size, u, v)
    adj = [[] for _ in range(size + 1)]
    indegree = [0] * (size + 1)
    for u, v, s, w in edges:
        adj[u].append((v, s, w))
        indegree[v] += 1

    # The best route maximizes its smallest ratio s / w, stored as a
    # numerator and denominator; 1 / 0 stands for the empty route at 1.
    num = [0] * (size + 1)
    den = [0] * (size + 1)
    reached = [False] * (size + 1)
    reached[1] = True
    num[1] = 1
    order = [v for v in range(1, size + 1) if indegree[v] == 0]
    for u in order:
        for v, s, w in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                order.append(v)
            if not reached[u]:
                continue
            a, b = num[u], den[u]
            if s * b < a * w:
                a, b = s, w
            if not reached[v] or num[v] * b < a * den[v]:
                reached[v] = True
                num[v], den[v] = a, b

    out = []
    for _ in range(q):
        price_s, price_w = next(data), next(data)
        good = reached[n] and price_s * num[n] > price_w * den[n]
        out.append("YES" if good else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
