import sys


def combine(a, b):
    """Bit k + j for every bit k of a and bit j of b: the sums of counts."""
    result, k = 0, 0
    while b:
        if b & 1:
            result |= a << k
        b >>= 1
        k += 1
    return result


def solve(points):
    n = len(points)
    edges = sorted(
        ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2, i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    # the single-linkage tree: nodes 0 .. n-1 are the objects, then each
    # component formed after a group of equal distances is a new node
    kids = [[] for _ in range(n)]
    width = [0] * n  # the largest squared distance inside a node
    out = [None] * n  # the squared distance at which a node meets the rest
    parent = list(range(n))
    members = [[i] for i in range(n)]
    comp_width = [0] * n
    comp_node = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    i = 0
    while i < len(edges):
        w = edges[i][0]
        grown = {}  # a component's root -> the nodes it swallowed in this group
        while i < len(edges) and edges[i][0] == w:
            _, a, b = edges[i]
            i += 1
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            far = max(comp_width[ra], comp_width[rb])
            for p in members[ra]:
                px, py = points[p]
                for q in members[rb]:
                    d = (px - points[q][0]) ** 2 + (py - points[q][1]) ** 2
                    if d > far:
                        far = d
            parent[rb] = ra
            members[ra] += members[rb]
            comp_width[ra] = far
            grown[ra] = grown.pop(ra, [comp_node[ra]]) + grown.pop(rb, [comp_node[rb]])
        for root, swallowed in grown.items():
            for c in swallowed:
                out[c] = w
            comp_node[root] = len(kids)
            kids.append(swallowed)
            width.append(comp_width[root])
            out.append(None)

    # a node can be a base when it is narrower than its distance to the rest,
    # and counts[v] has bit k set when node v splits into k bases
    counts = []
    for v in range(len(kids)):
        mask = 1 << 1 if out[v] is None or width[v] < out[v] else 0
        if kids[v]:
            total = 1
            for c in kids[v]:
                total = combine(total, counts[c])
            mask |= total
        counts.append(mask)
    root = counts[-1]
    return "".join("1" if root >> k & 1 else "0" for k in range(1, n + 1))


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    out = []
    while True:
        n = int(data[pos])
        pos += 1
        if n == 0:
            break
        coords = [int(x) for x in data[pos : pos + 2 * n]]
        pos += 2 * n
        out.append(solve(list(zip(coords[0::2], coords[1::2]))))
    sys.stdout.write("\n".join(out) + "\n")


main()
