"""A city and a plan: a seed, N, M, a coordinate range and a mode. The
shelters hold the workers with spare room of SPARE places in all (or
none). Mode 1 sends workers to random shelters with room; mode 2 gives an
optimal plan from min-cost flow; mode 3 takes that optimal plan and swaps
one pair of workers between two buildings, which may or may not make it
worse."""

import heapq
import random
import sys

SPARE = 5
WORKERS = 1000


def optimal(n, m, need, room, time):
    """Successive shortest paths with potentials, one augmenting path at a time."""
    size = n + m + 2
    source, sink = n + m, n + m + 1
    graph = [[] for _ in range(size)]

    def edge(u, v, cap, cost):
        graph[u].append([v, cap, cost, len(graph[v])])
        graph[v].append([u, 0, -cost, len(graph[u]) - 1])

    for i in range(n):
        edge(source, i, need[i], 0)
        for j in range(m):
            edge(i, n + j, need[i], time[i][j])
    for j in range(m):
        edge(n + j, sink, room[j], 0)
    potential = [0] * size
    flow = 0
    while flow < sum(need):
        dist = [None] * size
        dist[source] = 0
        back = [None] * size
        heap = [(0, source)]
        while heap:
            du, u = heapq.heappop(heap)
            if du > dist[u]:
                continue
            for k, (v, cap, cost, _) in enumerate(graph[u]):
                nd = du + cost + potential[u] - potential[v]
                if cap > 0 and (dist[v] is None or nd < dist[v]):
                    dist[v], back[v] = nd, (u, k)
                    heapq.heappush(heap, (nd, v))
        potential = [p + (d or 0) for p, d in zip(potential, dist)]
        push, v = sum(need) - flow, sink
        while v != source:
            u, k = back[v]
            push, v = min(push, graph[u][k][1]), u
        v = sink
        while v != source:
            u, k = back[v]
            graph[u][k][1] -= push
            graph[v][graph[u][k][3]][1] += push
            v = u
        flow += push
    plan = [[0] * m for _ in range(n)]
    for i in range(n):
        for v, cap, cost, rev in graph[i]:
            if n <= v < n + m:
                plan[i][v - n] = graph[v][rev][1]
    return plan


def main():
    seed, n, m, span, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    most = max(1, min(WORKERS, (WORKERS * m - SPARE) // n))
    buildings = [
        (rng.randint(-span, span), rng.randint(-span, span), rng.randint(1, most)) for _ in range(n)
    ]
    total = sum(b[2] for b in buildings)
    spare = 0 if seed % 2 else SPARE
    room = [1] * m
    for _ in range(total + spare - m):
        room[rng.choice([j for j in range(m) if room[j] < WORKERS])] += 1
    shelters = [(rng.randint(-span, span), rng.randint(-span, span), c) for c in room]
    time = [[abs(x - p) + abs(y - q) + 1 for p, q, _ in shelters] for x, y, _ in buildings]
    if mode == 1:
        free = room[:]
        plan = [[0] * m for _ in range(n)]
        for i, (_, _, b) in enumerate(buildings):
            for _ in range(b):
                j = rng.choice([j for j in range(m) if free[j] > 0])
                free[j] -= 1
                plan[i][j] += 1
    else:
        plan = optimal(n, m, [b[2] for b in buildings], room, time)
        if mode == 3 and n > 1:
            i1, i2 = rng.sample(range(n), 2)
            j1 = rng.choice([j for j in range(m) if plan[i1][j] > 0])
            j2 = rng.choice([j for j in range(m) if plan[i2][j] > 0])
            plan[i1][j1] -= 1
            plan[i1][j2] += 1
            plan[i2][j2] -= 1
            plan[i2][j1] += 1
    lines = ["%d %d" % (n, m)]
    lines += ["%d %d %d" % b for b in buildings] + ["%d %d %d" % s for s in shelters]
    lines += [" ".join(map(str, row)) for row in plan]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
