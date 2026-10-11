"""A metro network and a bearing: a seed and a mode. Mode 1 gives a few
short lines over a few stations, mode 2 50 lines of 50 stations with
indices up to 32767, mode 3 a long chain where the bearing runs along a
shortest path. The bearing follows a shortest path from its first
station, except in mode 1, where it is a random walk now and then."""

import random
import sys
from collections import deque

LINES, LENGTH, TOP = 50, 50, 32767


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
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        names = rng.sample(range(1, 40), rng.randint(3, 12))
        lines = [
            [rng.choice(names) for _ in range(rng.randint(2, 6))] for _ in range(rng.randint(1, 5))
        ]
    elif mode == 2:
        names = rng.sample(range(1, TOP + 1), 800)
        lines = [[rng.choice(names) for _ in range(LENGTH)] for _ in range(LINES)]
    else:
        names = rng.sample(range(1, TOP + 1), LINES * (LENGTH - 1) + 1)
        lines = [names[i * (LENGTH - 1) : (i + 1) * (LENGTH - 1) + 1] for i in range(LINES)]
    # stations next to each other on a line must differ
    lines = [[s for i, s in enumerate(line) if i == 0 or s != line[i - 1]] for line in lines]
    lines = [line for line in lines if len(line) >= 2] or [[names[0], names[1]]]
    graph = {}
    for line in lines:
        for a, b in zip(line, line[1:]):
            graph.setdefault(a, set()).add(b)
            graph.setdefault(b, set()).add(a)
    start = rng.choice(sorted(graph))
    if mode == 3:
        start = lines[0][0]
    dist = bfs(graph, start)
    bearing = [start]
    for _ in range(rng.randint(0, 2 * LENGTH if mode != 1 else 4)):
        here = bearing[-1]
        if mode == 1 and rng.random() < 0.2:
            steps = sorted(graph[here])
        else:
            steps = sorted(v for v in graph[here] if dist[v] == dist[here] + 1)
        if not steps:
            break
        bearing.append(rng.choice(steps))
    print(len(lines))
    for line in lines:
        print(len(line), *line)
    print(len(bearing), *bearing)


main()
