import os
import sys

INF = float("inf")
FIELDS = 4


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    updates = [[] for _ in range(n + 1)]
    for k in range(m):
        x, y, d, kind = data[2 + FIELDS * k : 2 + FIELDS * (k + 1)]
        updates[int(x)].append((int(y), int(d), kind))
    # updates only go up, so the versions can be taken in order; the
    # client is either still licensed (0) or already pirated (1)
    licensed = [INF] * (n + 1)
    pirated = [INF] * (n + 1)
    licensed[1] = 0
    del data
    for v in range(1, n + 1):
        legal, illegal = licensed[v], pirated[v]
        for y, d, kind in updates[v]:
            if kind == b"Pirated":
                candidate = min(legal, illegal) + d
                if candidate < pirated[y]:
                    pirated[y] = candidate
            elif kind == b"Cracked":
                candidate = legal + d
                if candidate < licensed[y]:
                    licensed[y] = candidate
                candidate = illegal + d
                if candidate < pirated[y]:
                    pirated[y] = candidate
            else:
                candidate = legal + d
                if candidate < licensed[y]:
                    licensed[y] = candidate
    answer = min(licensed[n], pirated[n])
    print("Offline" if answer == INF else "Online\n%d" % answer)


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
