"""Checker: NO exactly when the expected answer says so; otherwise YES
and a road map of 0, 1 and 2 that is symmetric in its roads, has no
road from a crossroad to itself, at most one board per road, and gives
exactly the table as the fewest boards seen between every two
crossroads."""

import sys
from collections import deque


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    a = [[int(words[1 + i * n + j]) for j in range(n)] for i in range(n)]
    want = open(expected).read().split()[0]
    got = open(output).read().split()
    if want == "NO":
        if got != ["NO"]:
            raise Bad("no road map fits the table, expected NO")
        return
    if len(got) != n + 1 or got[0] != "YES" or any(len(r) != n for r in got[1:]):
        raise Bad("expected YES and %d rows of %d characters" % (n, n))
    grid = got[1:]
    for i in range(n):
        if grid[i][i] != "0":
            raise Bad("crossroad %d has a road to itself" % (i + 1))
        for j in range(n):
            c, back = grid[i][j], grid[j][i]
            if c not in "012" or (c == "0") != (back == "0") or c == back == "2":
                raise Bad("the road between %d and %d is not consistent" % (i + 1, j + 1))
    for s in range(n):
        dist = [n * n] * n
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for u in range(n):
                if grid[v][u] != "0":
                    w = 1 if grid[v][u] == "2" else 0
                    if dist[v] + w < dist[u]:
                        dist[u] = dist[v] + w
                        if w:
                            queue.append(u)
                        else:
                            queue.appendleft(u)
        if dist != a[s]:
            raise Bad("the roads do not give row %d of the table" % (s + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
