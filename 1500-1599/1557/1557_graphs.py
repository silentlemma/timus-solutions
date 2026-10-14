import sys
from collections import Counter

MASK = (1 << 64) - 1
GOLDEN = 0x9E3779B97F4A7C15
MIX1 = 0xBF58476D1CE4E5B9
MIX2 = 0x94D049BB133111EB
SHIFT1 = 30
SHIFT2 = 27
SHIFT3 = 31


def mix(x):
    """A splitmix64 step: well-spread 64-bit labels from a counter."""
    x = (x + GOLDEN) & MASK
    x = ((x ^ (x >> SHIFT1)) * MIX1) & MASK
    x = ((x ^ (x >> SHIFT2)) * MIX2) & MASK
    return x ^ (x >> SHIFT3)


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    ends = [int(v) - 1 for v in data[2 : 2 + 2 * m]]
    adj = [[] for _ in range(n)]
    for e in range(m):
        u, v = ends[2 * e], ends[2 * e + 1]
        adj[u].append((v, e))
        adj[v].append((u, e))
    # a spanning tree in breadth-first order
    parent_edge = [-1] * n
    parent = [-1] * n
    seen = [False] * n
    seen[0] = True
    order = [0]
    for v in order:
        for u, e in adj[v]:
            if not seen[u]:
                seen[u] = True
                parent[u], parent_edge[u] = v, e
                order.append(u)
    in_tree = [False] * m
    for e in parent_edge:
        if e >= 0:
            in_tree[e] = True
    # every other channel gets a random label; a tree channel gets the XOR
    # of the labels of the channels whose cycles pass through it, which is
    # the XOR over the subtree below it
    label = [0] * m
    below = [0] * n
    for e in range(m):
        if not in_tree[e]:
            label[e] = mix(e)
            below[ends[2 * e]] ^= label[e]
            below[ends[2 * e + 1]] ^= label[e]
    for v in reversed(order[1:]):
        label[parent_edge[v]] = below[v]
        below[parent[v]] ^= below[v]
    # a bridge (label 0) cuts with any other channel; two other channels cut
    # together exactly when no cycle passes through just one of them
    bridges = label.count(0)
    rest = m - bridges
    total = m * (m - 1) // 2 - rest * (rest - 1) // 2
    for c in Counter(x for x in label if x).values():
        total += c * (c - 1) // 2
    print(total)


main()
