import sys
from array import array


def main():
    source = sys.stdin.buffer
    n, m = map(int, source.readline().split())
    heads = [-1] * (n + 1)
    target, cost, following = array("H"), array("H"), array("i")
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b, profit = map(int, source.readline().split())
        target.append(b)
        cost.append(profit)
        following.append(heads[a])
        heads[a] = len(target) - 1
        indegree[b] += 1
    start, finish = map(int, source.readline().split())
    best = [-1] * (n + 1)
    best[start] = 0
    order = [v for v in range(1, n + 1) if indegree[v] == 0]
    for v in order:
        value = best[v]
        edge = heads[v]
        # Follow real outgoing edges; no quadratic scan of absent matrix cells.
        while edge >= 0:
            w = target[edge]
            if value >= 0:
                candidate = value + cost[edge]
                if candidate > best[w]:
                    best[w] = candidate
            indegree[w] -= 1
            if indegree[w] == 0:
                order.append(w)
            edge = following[edge]
    print("No solution" if best[finish] < 0 else best[finish])


main()
