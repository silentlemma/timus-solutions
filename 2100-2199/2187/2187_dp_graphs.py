import sys

NEGATIVE_INFINITY = -(10**18)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    gold = data[2 : n + 2]
    cost = [0] + data[n + 2 : 2 * n + 1]
    graph = [[] for _ in range(n)]
    edges = iter(data[2 * n + 1 :])
    for left, right in zip(edges, edges):
        left -= 1
        right -= 1
        graph[left].append(right)
        graph[right].append(left)
    del data, edges
    degree = list(map(len, graph))
    order = sorted(range(n), key=degree.__getitem__)
    parents = [[] for _ in range(n)]
    depth = [-1] * n
    depth[0] = 0
    previous = [-1] * n
    reachable = []
    forward_work = 0
    forward_states = 0

    for vertex in order:
        if depth[vertex] < 0:
            continue
        reachable.append(vertex)
        forward_states += depth[vertex] + 1
        children = []
        popularity = degree[vertex]
        for neighbor in graph[vertex]:
            if degree[neighbor] <= popularity:
                continue
            children.append(neighbor)
            parents[neighbor].append(vertex)
            length = depth[vertex] + 1
            forward_work += length
            if length > depth[neighbor]:
                depth[neighbor] = length
                previous[neighbor] = vertex
        graph[vertex] = children
        forward_work -= depth[vertex]

    height = [0] * n
    following = [-1] * n
    reverse_work = 0
    reverse_states = 0
    for vertex in reversed(reachable):
        longest = 0
        for neighbor in graph[vertex]:
            length = height[neighbor] + 1
            reverse_work += length
            if length > longest:
                longest = length
                following[vertex] = neighbor
        height[vertex] = longest
        reverse_states += longest + 1
        reverse_work -= longest

    # Copy the longest row, and choose the direction with fewer remaining updates.
    reverse = (
        reverse_states <= 2 * forward_states
        and reverse_work + reverse_states < forward_work + forward_states
    )
    if reverse:
        reachable.reverse()
        dependencies = graph
        primary = following
    else:
        dependencies = parents
        primary = previous
    rows = [None] * n
    answer = gold[0]

    for vertex in reachable:
        neighbors = dependencies[vertex]
        if not neighbors:
            rows[vertex] = [gold[vertex]]
            continue
        longest = primary[vertex]
        row = [0] + rows[longest]
        for neighbor in neighbors:
            if neighbor == longest:
                continue
            for length, candidate in enumerate(rows[neighbor], 1):
                if candidate > row[length]:
                    row[length] = candidate
        best = 0 if reverse else NEGATIVE_INFINITY
        for length in range(1, len(row)):
            candidate = row[length] - cost[length]
            if candidate > best:
                best = candidate
        row[0] = best + gold[vertex]
        rows[vertex] = row
        if row[0] > answer:
            answer = row[0]

    print(rows[0][0] if reverse else answer)


if __name__ == "__main__":
    main()
