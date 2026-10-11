"""Road maps: a seed, M, N, a mode and an offset. Mode 1 is a random
forest (N is ignored), mode 2 adds a road from a city to its grandparent, closing a cycle, mode 3
adds a loop at a city, mode 4 adds a second road between two cities. The
length S is the longest route in the forest plus the offset."""

import random
import sys

LONGEST = 32000


def diameter(m, roads):
    adj = [[] for _ in range(m + 1)]
    for p, q, r in roads:
        adj[p].append((q, r))
        adj[q].append((p, r))

    def far(s):
        dist = {s: 0}
        stack = [s]
        while stack:
            v = stack.pop()
            for u, r in adj[v]:
                if u not in dist:
                    dist[u] = dist[v] + r
                    stack.append(u)
        return max(dist.items(), key=lambda kv: kv[1])

    return max(far(far(v)[0])[1] for v in range(1, m + 1))


def main():
    seed, m, n, mode, offset = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    roads = [
        (v, rng.randint(1, v - 1), rng.randint(1, LONGEST))
        for v in range(2, m + 1)
        if rng.random() < 0.9
    ]
    best = diameter(m, roads)
    # every road joins a city to an earlier one, its parent in the tree
    par = {v: q for v, q, _ in roads}
    deep = [v for v in par if par[v] in par]
    if mode == 2 and deep:
        v = rng.choice(deep)
        roads.append((v, par[par[v]], rng.randint(1, LONGEST)))
    elif mode == 3:
        v = rng.randint(1, m)
        roads.append((v, v, rng.randint(1, LONGEST)))
    elif mode == 4 and roads:
        p, q, _ = rng.choice(roads)
        roads.append((q, p, rng.randint(1, LONGEST)))
    rng.shuffle(roads)
    s = min(2 * 10**6, max(1, best + offset))
    lines = ["%d %d %d" % (m, len(roads), s)] + ["%d %d %d" % r for r in roads]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
