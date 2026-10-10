import sys
from collections import defaultdict


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n = next(tok)
    rows = [[next(tok) - 1 for _ in range(next(tok))] for _ in range(n)]
    # pair the k-th mention of v in room u with the k-th mention of u in room
    # v; a door to the room itself is mentioned twice in its own row
    ends = []
    slot = {}
    waiting = defaultdict(list)
    for u in range(n):
        for i, v in enumerate(rows[u]):
            key = (min(u, v), max(u, v))
            if waiting[key]:
                e = waiting[key].pop(0)
                ends[e][1] = (u, i)
            else:
                waiting[key].append(len(ends))
                ends.append([(u, i), None])
    # a dummy room joined to every room of odd degree makes all degrees even
    dummy = n
    adj = [[] for _ in range(n + 1)]
    for e, ((u, _), (v, _)) in enumerate(ends):
        adj[u].append((v, e))
        adj[v].append((u, e))
    edges = len(ends)
    for u in range(n):
        if len(adj[u]) % 2:
            adj[u].append((dummy, edges))
            adj[dummy].append((u, edges))
            edges += 1
    # walk Euler circuits and orient each door along the walk
    used = [False] * edges
    tail = {}
    ptr = [0] * (n + 1)
    for start in range(n + 1):
        stack = [start]
        while stack:
            u = stack[-1]
            while ptr[u] < len(adj[u]) and used[adj[u][ptr[u]][1]]:
                ptr[u] += 1
            if ptr[u] == len(adj[u]):
                stack.pop()
                continue
            v, e = adj[u][ptr[u]]
            used[e] = True
            tail[e] = u
            stack.append(v)
    colours = [[""] * len(rows[u]) for u in range(n)]
    for e, ((u, i), (v, j)) in enumerate(ends):
        # green on the side the walk leaves from, orange where it enters
        out_u = tail[e] == u
        colours[u][i] = "G" if out_u else "Y"
        colours[v][j] = "Y" if out_u else "G"
    print("\n".join(" ".join(row) for row in colours))


main()
