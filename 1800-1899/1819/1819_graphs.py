import random
import sys

SEED = 2010
BITS = 64


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    ends = [int(x) - 1 for x in data[2:2 + 2 * k]]
    head = [-1] * n
    nxt = [0] * (2 * k)
    for half in range(2 * k):
        v = ends[half]
        nxt[half] = head[v]
        head[v] = half
    # iterative DFS: half-edge h runs from ends[h] to ends[h ^ 1], and the
    # half-edges of a vertex are chained through head and nxt
    comp = [-1] * n
    tin = [0] * n
    parent = [-1] * n
    up_edge = [-1] * n
    order = []
    it = head[:]
    for root in range(n):
        if comp[root] >= 0:
            continue
        comp[root] = root
        tin[root] = len(order)
        order.append(root)
        stack = [root]
        while stack:
            v = stack[-1]
            h = it[v]
            if h < 0:
                stack.pop()
                continue
            it[v] = nxt[h]
            w = ends[h ^ 1]
            if comp[w] < 0:
                comp[w] = root
                parent[w] = v
                up_edge[w] = h >> 1
                tin[w] = len(order)
                order.append(w)
                stack.append(w)
    rng = random.Random(SEED)
    # every non-tree edge joins a vertex and its ancestor; mark it with a
    # random value at both ends, so after summing over subtrees the edge
    # above v carries the xor of the non-tree edges passing over it
    cover = [0] * n
    count = [0] * n
    for e in range(k):
        a, b = ends[2 * e], ends[2 * e + 1]
        if up_edge[a] == e or up_edge[b] == e:
            continue
        if tin[a] < tin[b]:
            a, b = b, a
        r = rng.getrandbits(BITS)
        cover[a] ^= r
        cover[b] ^= r
        count[a] += 1
        count[b] -= 1
    for v in reversed(order):
        p = parent[v]
        if p >= 0:
            cover[p] ^= cover[v]
            count[p] += count[v]
    # a pair of edges is a cut exactly when it is a tree edge covered by
    # nothing but that non-tree edge, or two tree edges covered by the same
    # set; tree edges get values making a path xor to zero iff it crosses none
    value = [0] * n
    first = {}
    for v in order:
        if parent[v] < 0:
            continue
        if count[v] < 2:
            # a bridge or an edge with one cover: crossing it separates
            value[v] = rng.getrandbits(BITS)
            continue
        # edges with one cover set lie on a chain and cut the tree into
        # pieces closed into a ring; a path inside the ring crosses all of
        # them or none of them, so the class must xor to zero
        rep = first.setdefault(cover[v], v)
        if rep != v:
            value[v] = rng.getrandbits(BITS)
            value[rep] ^= value[v]
    label = [0] * n
    for v in order:
        if parent[v] >= 0:
            label[v] = label[parent[v]] ^ value[v]
    rest = data[2 + 2 * k:]
    out = []
    for i in range(int(rest[0])):
        a = int(rest[2 * i + 1]) - 1
        b = int(rest[2 * i + 2]) - 1
        same = comp[a] == comp[b] and label[a] == label[b]
        out.append("Yes" if same else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
