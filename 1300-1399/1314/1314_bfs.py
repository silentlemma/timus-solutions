import sys
from collections import deque


def bfs(graph, start):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def main():
    words = iter(sys.stdin.read().split())
    graph = {}
    for _ in range(int(next(words))):
        line = [int(next(words)) for _ in range(int(next(words)))]
        for a, b in zip(line, line[1:]):
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
    seen = [int(next(words)) for _ in range(int(next(words)))]
    # the stations seen must be a walk through the network ...
    if any(s not in graph for s in seen) or any(b not in graph[a] for a, b in zip(seen, seen[1:])):
        return
    first = bfs(graph, seen[0])
    # ... and a shortest one, or no target fits it
    if first[seen[-1]] != len(seen) - 1:
        return
    last = bfs(graph, seen[-1])
    # a target fits when the walk can go on to it along a shortest path
    targets = [t for t in first if t in last and first[t] == first[seen[-1]] + last[t]]
    sys.stdout.write("".join("%d\n" % t for t in sorted(targets)))


main()
