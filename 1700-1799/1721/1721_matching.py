import sys

# two people can team up only if their ranks differ by exactly 2, so half
# the rank changes parity along every pair: the graph is bipartite
GAP = 2
SIDES = 2
FIELDS = 3


def matching(adj, right_count):
    mate_left = [-1] * len(adj)
    mate_right = [-1] * right_count
    total = 0
    while True:
        dist = [-1] * len(adj)
        queue = [u for u in range(len(adj)) if mate_left[u] < 0]
        for u in queue:
            dist[u] = 0
        found = False
        for u in queue:
            for v in adj[u]:
                w = mate_right[v]
                if w < 0:
                    found = True
                elif dist[w] < 0:
                    dist[w] = dist[u] + 1
                    queue.append(w)
        if not found:
            return total, mate_left
        nxt = [0] * len(adj)
        for root in range(len(adj)):
            if mate_left[root] >= 0:
                continue
            path = [root]
            while path:
                u = path[-1]
                if nxt[u] == len(adj[u]):
                    # a dead end: cut it off and move its parent on
                    dist[u] = -1
                    path.pop()
                    if path:
                        nxt[path[-1]] += 1
                    continue
                v = adj[u][nxt[u]]
                w = mate_right[v]
                if w < 0:
                    for x in path:
                        y = adj[x][nxt[x]]
                        mate_left[x] = y
                        mate_right[y] = x
                    total += 1
                    break
                if dist[w] == dist[u] + 1:
                    path.append(w)
                else:
                    nxt[u] += 1


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    names, writes, tests, ranks = [], [], [], []
    for i in range(n):
        k = 1 + FIELDS * i
        name, kind, rank = words[k:k + FIELDS]
        names.append(name)
        writes.append(kind != "testdata")
        tests.append(kind != "statements")
        ranks.append(int(rank))
    side = [[] for _ in range(SIDES)]
    for i in range(n):
        side[ranks[i] // GAP % SIDES].append(i)
    left, right = side
    by_rank = {}
    for j, y in enumerate(right):
        by_rank.setdefault(ranks[y], []).append(j)
    adj = []
    for x in left:
        edges = []
        for r in (ranks[x] - GAP, ranks[x] + GAP):
            for j in by_rank.get(r, ()):
                y = right[j]
                if (writes[x] and tests[y]) or (writes[y] and tests[x]):
                    edges.append(j)
        adj.append(edges)
    total, mate_left = matching(adj, len(right))
    out = [str(total)]
    for u, v in enumerate(mate_left):
        if v < 0:
            continue
        a, b = left[u], right[v]
        if writes[a] and tests[b]:
            out.append(names[a] + " " + names[b])
        else:
            out.append(names[b] + " " + names[a])
    print("\n".join(out))


main()
