import sys
from array import array


def main():
    source = sys.stdin.buffer
    n, m = map(int, source.readline().split())
    # profits are 1..10000; unsigned short cells use zero for absent edges.
    cost = [array("H", [0]) * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, source.readline().split())
        cost[a][b] = c
        indegree[b] += 1
    start, finish = map(int, source.readline().split())
    best = [-1] * (n + 1)
    best[start] = 0
    order = [v for v in range(1, n + 1) if indegree[v] == 0]
    for v in order:
        value = best[v]
        for w, c in enumerate(cost[v]):
            if c:
                if value >= 0 and value + c > best[w]:
                    best[w] = value + c
                indegree[w] -= 1
                if indegree[w] == 0:
                    order.append(w)
    print("No solution" if best[finish] < 0 else best[finish])


main()
