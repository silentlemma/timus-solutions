import random
import sys

BITS = 64
MASK = (1 << BITS) - 1
SEED = 31337


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0

    def take():
        nonlocal pos
        pos += 1
        return int(data[pos - 1])

    n, m = take(), take()
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = take() - 1, take() - 1
        adj[u].append(v)
        adj[v].append(u)
    # every technology gets a random weight; a path uses each one exactly once
    # when (with overwhelming probability) its weights add up to the sum of all
    rng = random.Random(SEED)
    weight = [rng.getrandbits(BITS) for _ in range(m + 1)]
    goal = sum(weight[1:]) & MASK
    own = [0] * n
    for v in range(n):
        own[v] = sum(weight[take()] for _ in range(take())) & MASK
    # depth[v]: the weights on the path from the root to v
    parent, order = [-1] * n, [0]
    depth = [0] * n
    depth[0] = own[0]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                depth[u] = (depth[v] + own[u]) & MASK
                order.append(u)
    # small to large: below[v] maps depth -> a vertex of the subtree of v; two
    # vertices from different children of x (or x itself) join through x
    below = [None] * n
    for x in reversed(order):
        if own[x] == goal:
            print(x + 1, x + 1)
            return
        mine = {depth[x]: x}
        target = (goal + 2 * depth[x] - own[x]) & MASK
        for y in adj[x]:
            if y == parent[x]:
                continue
            other = below[y]
            below[y] = None
            if len(other) > len(mine):
                mine, other = other, mine
            for d, u in other.items():
                v = mine.get((target - d) & MASK)
                if v is not None:
                    print(u + 1, v + 1)
                    return
            mine.update(other)
        below[x] = mine
    print("No solution")


main()
