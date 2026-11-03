from sys import implementation, stdin, stdout

# These short bounded scans trade JIT code-cache memory for interpreter work.
if implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("off")
from math import hypot

walk, metro = map(float, stdin.readline().split())
stations = int(stdin.readline())
points = [tuple(map(float, stdin.readline().split())) for _ in range(stations)]
linked = [0] * (stations + 2)
while True:
    a, b = map(int, stdin.readline().split())
    if a == b == 0:
        break
    linked[a - 1] |= 1 << (b - 1)
    linked[b - 1] |= 1 << (a - 1)
points.extend(tuple(map(float, stdin.readline().split())) for _ in range(2))
start, goal = stations, stations + 1
path = []
if walk == metro or not any(linked) or points[start] == points[goal]:
    result = hypot(points[start][0] - points[goal][0], points[start][1] - points[goal][1]) / walk
else:
    # A station with no train edge can be skipped by the triangle inequality.
    active = [start, goal] + [v for v in range(stations) if linked[v]]
    distance = [float("inf")] * len(points)
    previous = [-1] * len(points)
    done = bytearray(len(points))
    distance[start] = 0.0
    while True:
        u = -1
        for v in active:
            if not done[v] and (u < 0 or distance[v] < distance[u]):
                u = v
        if u == goal:
            break
        done[u] = 1
        row = linked[u]
        for v in active:
            if not done[v]:
                speed = metro if row >> v & 1 else walk
                candidate = (
                    distance[u]
                    + hypot(points[v][0] - points[u][0], points[v][1] - points[u][1]) / speed
                )
                if candidate < distance[v]:
                    distance[v] = candidate
                    previous[v] = u
    result = distance[goal]
    v = previous[goal]
    while v != start:
        path.append(v + 1)
        v = previous[v]
stdout.write("%.17g\n" % result)
stdout.write(str(len(path)) + " " + " ".join(map(str, reversed(path))) + "\n")
