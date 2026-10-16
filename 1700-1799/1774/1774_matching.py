import sys
from collections import deque

SHAVES = 2


class Flow:
    def __init__(self, size):
        self.edges = []
        self.out = [[] for _ in range(size)]

    def add(self, a, b, cap):
        self.out[a].append(len(self.edges))
        self.edges.append([b, cap])
        self.out[b].append(len(self.edges))
        self.edges.append([a, 0])
        return len(self.edges) - 2

    def push(self, v, sink, limit, level, at):
        if v == sink:
            return limit
        while at[v] < len(self.out[v]):
            e = self.out[v][at[v]]
            to, cap = self.edges[e]
            if cap and level[to] == level[v] + 1:
                got = self.push(to, sink, min(limit, cap), level, at)
                if got:
                    self.edges[e][1] -= got
                    self.edges[e ^ 1][1] += got
                    return got
            at[v] += 1
        return 0

    def max_flow(self, source, sink):
        total = 0
        while True:
            level = [-1] * len(self.out)
            level[source] = 0
            queue = deque([source])
            while queue:
                v = queue.popleft()
                for e in self.out[v]:
                    to, cap = self.edges[e]
                    if cap and level[to] < 0:
                        level[to] = level[v] + 1
                        queue.append(to)
            if level[sink] < 0:
                return total
            at = [0] * len(self.out)
            while True:
                got = self.push(source, sink, SHAVES, level, at)
                if not got:
                    break
                total += got


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    pairs = [int(v) for v in data[2:2 + 2 * n]]
    come, stay = pairs[0::2], pairs[1::2]
    # minutes between consecutive arrivals and departures see the same mages,
    # so they form blocks: a block of L minutes shaves k L times, at most
    # min(L, 2) of them on one mage
    cuts = sorted(set(come) | {t + s for t, s in zip(come, stay)})
    blocks = list(zip(cuts, cuts[1:]))
    source, sink = n + len(blocks), n + len(blocks) + 1
    flow = Flow(sink + 1)
    links = []
    for i in range(n):
        flow.add(source, i, SHAVES)
        for j, (lo, hi) in enumerate(blocks):
            if come[i] <= lo and hi <= come[i] + stay[i]:
                links.append((i, j, flow.add(i, n + j, min(hi - lo, SHAVES))))
    for j, (lo, hi) in enumerate(blocks):
        flow.add(n + j, sink, k * (hi - lo))
    if flow.max_flow(source, sink) < SHAVES * n:
        print("No")
        return
    # inside a block the shaves are dealt out round the minutes, so the two
    # shaves of one mage fall on different minutes and no minute gets more
    # than k of them
    dealt = [0] * len(blocks)
    times = [[] for _ in range(n)]
    for i, j, e in links:
        lo, hi = blocks[j]
        for _ in range(flow.edges[e ^ 1][1]):
            times[i].append(lo + dealt[j] % (hi - lo))
            dealt[j] += 1
    print("Yes")
    print("\n".join("%d %d" % tuple(sorted(t)) for t in times))


main()
