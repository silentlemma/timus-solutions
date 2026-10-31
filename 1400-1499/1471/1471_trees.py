import sys


def main():
    values = (int(token) for line in sys.stdin.buffer for token in line.split())
    n = next(values)
    adjacency = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, weight = next(values), next(values), next(values)
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))
    parent, depth, distance, first = [-1] * n, [0] * n, [0] * n, [0] * n
    pointer, tour, stack = [0] * n, [0], [0]
    while stack:
        v = stack[-1]
        if pointer[v] < len(adjacency[v]):
            u, weight = adjacency[v][pointer[v]]
            pointer[v] += 1
            if u == parent[v]:
                continue
            parent[u] = v
            depth[u] = depth[v] + 1
            distance[u] = distance[v] + weight
            first[u] = len(tour)
            tour.append(u)
            stack.append(u)
        else:
            stack.pop()
            if stack:
                tour.append(stack[-1])
    table = [tour]
    span = 1
    while 2 * span <= len(tour):
        previous = table[-1]
        level = []
        for i in range(len(tour) - 2 * span + 1):
            a, b = previous[i], previous[i + span]
            level.append(a if depth[a] <= depth[b] else b)
        table.append(level)
        span *= 2
    output = []
    for _ in range(next(values)):
        a, b = next(values), next(values)
        lo, hi = sorted((first[a], first[b]))
        k = (hi - lo + 1).bit_length() - 1
        x, y = table[k][lo], table[k][hi - (1 << k) + 1]
        ancestor = x if depth[x] <= depth[y] else y
        output.append(str(distance[a] + distance[b] - 2 * distance[ancestor]))
    print("\n".join(output))


main()
