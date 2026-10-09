import sys
from collections import deque


def main():
    tok = iter(sys.stdin.buffer.read().split())
    n = int(next(tok))
    adj = [[] for _ in range(n + 1)]
    for v in range(1, n + 1):
        for u in iter(lambda: int(next(tok)), 0):
            adj[v].append(u)
    # colour a BFS tree of every component by depth parity: each member has a
    # tree neighbour, its parent or a child, in the other team
    side = [-1] * (n + 1)
    for root in range(1, n + 1):
        if side[root] >= 0:
            continue
        side[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for u in adj[v]:
                if side[u] < 0:
                    side[u] = 1 - side[v]
                    queue.append(u)
    team = [v for v in range(1, n + 1) if side[v] == 0]
    print(len(team))
    print(" ".join(map(str, team)))


main()
