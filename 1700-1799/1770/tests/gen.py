"""One test from a seed and a mode: mode 1 the table of a random road
map of up to 8 crossroads, mode 2 a random table of up to 6 crossroads,
mode 3 the table of a random road map of 300 crossroads, mode 4 the
same with one entry changed by one."""

import random
import sys
from collections import deque

FEW = 8
TINY = 6
MOST = 300
EXTRA = 2
BOARD = 0.5


def table(rng, n):
    # a random tree keeps the map connected, and a few more roads join it
    roads = {(rng.randrange(v), v) for v in range(1, n)}
    for _ in range(EXTRA * n):
        i, j = rng.sample(range(n), 2)
        roads.add((min(i, j), max(i, j)))
    out = [[] for _ in range(n)]
    for i, j in roads:
        if rng.random() < BOARD:
            i, j = (i, j) if rng.random() < BOARD else (j, i)
            out[i].append((j, 1))
            out[j].append((i, 0))
        else:
            out[i].append((j, 0))
            out[j].append((i, 0))
    rows = []
    for s in range(n):
        dist = [n] * n
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for u, w in out[v]:
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
                    if w:
                        queue.append(u)
                    else:
                        queue.appendleft(u)
        rows.append(dist)
    return rows


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        n = rng.randint(2, TINY)
        rows = [[0 if i == j else rng.randint(0, min(2, n - 1)) for j in range(n)]
                for i in range(n)]
    else:
        n = rng.randint(2, FEW) if mode == 1 else MOST
        rows = table(rng, n)
    if mode == 4:
        i, j = rng.sample(range(n), 2)
        rows[i][j] = rows[i][j] + 1 if rows[i][j] < n - 1 else rows[i][j] - 1
    print(n)
    for row in rows:
        print(*row)


main()
