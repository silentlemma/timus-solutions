"""Print the table WALKS of the solutions: for every n from 2 to 50 where the
longest walk from inn 1 grows, the line "n: walk".

An exhaustive search, the one described in the write-up: extend the walk
from its last inn, the inns with the fewest free neighbours first, and cut a
branch when the free inns reachable from the last one, less all but one of
those with at most one free neighbour, cannot beat the record. The first
longest walk in this order is printed. Slow: hours for the largest n.
"""

import sys

LOWEST = 2
HIGHEST = 50


def longest_walk(n):
    adj = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i % j == 0 or j % i == 0):
                adj[i] |= 1 << j
    best = [0, []]
    path = [1]

    def dfs(v, free):
        if len(path) > best[0]:
            best[0] = len(path)
            best[1] = list(path)
        # the free inns reachable from v through free inns
        reach = 0
        frontier = adj[v] & free
        while frontier:
            reach |= frontier
            nxt = 0
            f = frontier
            while f:
                low = f & -f
                nxt |= adj[low.bit_length() - 1]
                f ^= low
            frontier = nxt & free & ~reach
        bound = bin(reach).count("1")
        # inns with at most one neighbour among them and v can only end the walk
        around = reach | (1 << v)
        ends = 0
        r = reach
        while r:
            low = r & -r
            if bin(adj[low.bit_length() - 1] & around).count("1") <= 1:
                ends += 1
            r ^= low
        if ends > 1:
            bound -= ends - 1
        if len(path) + bound <= best[0]:
            return
        order = []
        cand = adj[v] & free
        while cand:
            low = cand & -cand
            u = low.bit_length() - 1
            order.append((bin(adj[u] & free).count("1"), u))
            cand ^= low
        order.sort()
        for _, u in order:
            path.append(u)
            dfs(u, free & ~(1 << u))
            path.pop()

    free = 0
    for i in range(2, n + 1):
        free |= 1 << i
    dfs(1, free)
    return best[1]


def main():
    sys.setrecursionlimit(10000)
    last = 0
    for n in range(LOWEST, HIGHEST + 1):
        walk = longest_walk(n)
        if len(walk) > last:
            last = len(walk)
            print("%d: %s" % (n, " ".join(map(str, walk))), flush=True)


main()
