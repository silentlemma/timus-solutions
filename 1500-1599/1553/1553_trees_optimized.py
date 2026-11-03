import sys
from array import array

OUTPUT_LINES = 1024


def main():
    tokens = (part for line in sys.stdin.buffer for part in line.split())
    n = int(next(tokens))
    first = array("i", [-1]) * n
    to = array("i", [0]) * (2 * n - 2)
    link = array("i", [0]) * (2 * n - 2)
    for edge in range(n - 1):
        a, b = int(next(tokens)) - 1, int(next(tokens)) - 1
        j = 2 * edge
        to[j], link[j], first[a] = b, first[a], j
        to[j + 1], link[j + 1], first[b] = a, first[b], j + 1

    parent = array("i", [-1]) * n
    depth = array("i", [0]) * n
    order = array("i", [0]) * n
    end = 1
    for i in range(n):
        v = order[i]
        edge = first[v]
        while edge != -1:
            u = to[edge]
            if u != parent[v]:
                parent[u] = v
                depth[u] = depth[v] + 1
                order[end] = u
                end += 1
            edge = link[edge]
    size = array("i", [1]) * n
    heavy = array("i", [-1]) * n
    for i in range(n - 1, 0, -1):
        v = order[i]
        p = parent[v]
        size[p] += size[v]
        if heavy[p] == -1 or size[v] > size[heavy[p]]:
            heavy[p] = v
    head = array("i", [0]) * n
    index = array("i", [0]) * n
    position = 0
    for v in order:
        if v == 0 or heavy[parent[v]] != v:
            u = v
            while u != -1:
                head[u] = v
                index[u] = position
                position += 1
                u = heavy[u]
    del first, to, link, order, size, heavy
    tree = array("i", [0]) * (2 * n)

    def segment_max(left, right):
        left += n
        right += n + 1
        best = 0
        while left < right:
            if left & 1:
                if tree[left] > best:
                    best = tree[left]
                left += 1
            if right & 1:
                right -= 1
                if tree[right] > best:
                    best = tree[right]
            left >>= 1
            right >>= 1
        return best

    output = []
    write = sys.stdout.write
    q = int(next(tokens))
    for _ in range(q):
        kind, u, v = next(tokens), int(next(tokens)) - 1, int(next(tokens))
        if kind == b"I":
            at = index[u] + n
            value = tree[at] + v
            tree[at] = value
            at >>= 1
            # Values only grow: an unchanged ancestor leaves all above it unchanged.
            while at and tree[at] < value:
                tree[at] = value
                at >>= 1
            continue
        v -= 1
        best = 0
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            value = segment_max(index[head[u]], index[u])
            if value > best:
                best = value
            u = parent[head[u]]
        left, right = index[u], index[v]
        if left > right:
            left, right = right, left
        value = segment_max(left, right)
        if value > best:
            best = value
        output.append(str(best) + "\n")
        if len(output) == OUTPUT_LINES:
            write("".join(output))
            output.clear()
    write("".join(output))


main()
