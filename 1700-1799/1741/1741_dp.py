import sys

INF = float("inf")
FIELDS = 4


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    updates = [[] for _ in range(n + 1)]
    for k in range(m):
        x, y, d, kind = data[2 + FIELDS * k:2 + FIELDS * (k + 1)]
        updates[int(x)].append((int(y), int(d), kind.decode()))
    # updates only go up, so the versions can be taken in order; the
    # client is either still licensed (0) or already pirated (1)
    best = [[INF, INF] for _ in range(n + 1)]
    best[1][0] = 0
    for v in range(1, n + 1):
        for y, d, kind in updates[v]:
            for state in (0, 1):
                cost = best[v][state] + d
                if kind == "Pirated":
                    best[y][1] = min(best[y][1], cost)
                elif kind == "Cracked":
                    best[y][state] = min(best[y][state], cost)
                elif state == 0:
                    best[y][0] = min(best[y][0], cost)
    answer = min(best[n])
    print("Offline" if answer == INF else "Online\n%d" % answer)


main()
