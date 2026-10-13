import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    pos = 2
    routes = []
    on_stop = [[] for _ in range(m + 1)]
    for r in range(n):
        k = int(data[pos])
        stops = [int(x) for x in data[pos + 1 : pos + 1 + k]]
        pos += 1 + k
        routes.append(stops)
        for st in stops:
            on_stop[st].append(r)
    a, b = int(data[pos]), int(data[pos + 1])
    # one ride along a route reaches any of its stops, both ways; layers of rides
    rides = [-1] * (m + 1)
    came_by = [-1] * (m + 1)  # the route that first reached a stop
    boarded = [-1] * n  # the stop where a route was first taken
    rides[a] = 0
    queue = deque([a])
    while queue and rides[b] < 0:
        st = queue.popleft()
        for r in on_stop[st]:
            if boarded[r] >= 0:
                continue
            boarded[r] = st
            for nxt in routes[r]:
                if rides[nxt] < 0:
                    rides[nxt] = rides[st] + 1
                    came_by[nxt] = r
                    queue.append(nxt)
    if rides[b] < 0:
        print(-1)
        return
    path = [b]
    while path[-1] != a:
        path.append(boarded[came_by[path[-1]]])
    print(rides[b])
    print(" ".join(map(str, reversed(path))))


main()
