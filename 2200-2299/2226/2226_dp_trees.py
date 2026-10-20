import sys

MAX_LENGTH = 10**9
INF = MAX_LENGTH + 1


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    graph = [[] for _ in range(n + 1)]
    first = [0] * (n + 1)
    second = [0] * (n + 1)
    shortest = [INF] * (n + 1)
    next_shortest = [INF] * (n + 1)
    for _ in range(n - 1):
        u, v, length = next(data), next(data), next(data)
        graph[u].append(v)
        graph[v].append(u)
        for a, b in ((u, v), (v, u)):
            if length < shortest[a]:
                next_shortest[a] = shortest[a]
                second[a] = first[a]
                shortest[a] = length
                first[a] = b
            elif length < next_shortest[a]:
                next_shortest[a] = length
                second[a] = b

    parent = [0] * (n + 1)
    order = [1]
    for v in order:
        for u in graph[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)

    # down[v] is the endpoint after arriving at v from its parent.
    down = [0] * (n + 1)
    up = [0] * (n + 1)
    for v in reversed(order):
        u = second[v] if first[v] == parent[v] else first[v]
        down[v] = down[u] if u else v
    # up[v] is the endpoint after leaving v for its parent.
    for i in range(1, n):
        v = order[i]
        p = parent[v]
        u = second[p] if first[p] == v else first[p]
        up[v] = p if not u else up[p] if u == parent[p] else down[u]
    answer = (up[v] if first[v] == parent[v] else down[v] for v in range(1, n + 1))
    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
