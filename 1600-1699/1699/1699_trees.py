import sys

LOG = 17  # 2^17 > 100000 cells
QUERY = 4  # r1 c1 r2 c2


def main():
    data = sys.stdin.buffer.read().split()
    h, w = int(data[0]), int(data[1])
    grid = b"".join(data[2:2 + h])
    open_cell = [c == ord("#") for c in grid]
    cells = h * w
    pos = 2 + h
    q = int(data[pos])
    queries = [int(x) for x in data[pos + 1:pos + 1 + QUERY * q]]
    # the open cells form a tree; root it at the first open cell and keep, for
    # every cell, its parent, depth, the direction of the step from the parent
    # (as the index offset) and the number of turns from the root
    root = open_cell.index(True)
    parent = [-1] * cells
    depth = [0] * cells
    step = [0] * cells
    turns = [0] * cells
    parent[root] = root
    order = [root]
    for v in order:
        r, c = divmod(v, w)
        for u, ok in ((v - w, r > 0), (v + w, r < h - 1), (v - 1, c > 0), (v + 1, c < w - 1)):
            if ok and open_cell[u] and parent[u] < 0:
                parent[u] = v
                depth[u] = depth[v] + 1
                step[u] = u - v
                turns[u] = turns[v] + (v != root and step[v] != u - v)
                order.append(u)
    # closed cells point at themselves, which keeps the jump table in range
    parent = [v if p < 0 else p for v, p in enumerate(parent)]
    up = [parent]
    for _ in range(1, LOG):
        prev = up[-1]
        up.append([prev[prev[v]] for v in range(cells)])

    def lift(v, k):
        bit = 0
        while k:
            if k & 1:
                v = up[bit][v]
            k >>= 1
            bit += 1
        return v

    out = []
    for i in range(q):
        r1, c1, r2, c2 = queries[QUERY * i:QUERY * (i + 1)]
        a, b = (r1 - 1) * w + c1 - 1, (r2 - 1) * w + c2 - 1
        if depth[a] < depth[b]:
            a, b = b, a
        if a == b:
            out.append(0)
            continue
        a1, b1 = a, b
        if depth[a] > depth[b]:
            # lift a to just below b's depth: if it then hangs from b, b is an
            # ancestor and only the way down from b counts
            a1 = lift(a, depth[a] - depth[b] - 1)
            if parent[a1] == b:
                out.append(turns[a] - turns[a1])
                continue
            a1 = parent[a1]
        for bit in range(LOG - 1, -1, -1):
            if up[bit][a1] != up[bit][b1]:
                a1, b1 = up[bit][a1], up[bit][b1]
        # a1 and b1 are the children of the meeting cell on the two sides, the
        # path turns there unless it goes straight through
        straight = step[a1] == -step[b1]
        out.append(turns[a] - turns[a1] + turns[b] - turns[b1] + (0 if straight else 1))
    print("\n".join(map(str, out)))


main()
