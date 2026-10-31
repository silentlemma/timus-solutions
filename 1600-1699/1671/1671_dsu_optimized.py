import sys
from array import array
from itertools import islice


def main():
    # consume lines incrementally instead of retaining all input tokens.
    tokens = (int(word) for line in sys.stdin.buffer for word in line.split())
    n, m = next(tokens), next(tokens)
    # endpoints, edge indices and answers are at most 100000, fitting unsigned int.
    ends = array("I", islice(tokens, 2 * m))
    q = next(tokens)
    cuts = array("I", (edge - 1 for edge in islice(tokens, q)))
    del tokens
    parent = [-1] * (n + 1)

    def find(v):
        root = v
        while parent[root] >= 0:
            root = parent[root]
        while v != root:
            parent[v], v = root, parent[v]
        return root

    pieces = n

    def join(edge):
        nonlocal pieces
        a, b = find(ends[2 * edge]), find(ends[2 * edge + 1])
        if a == b:
            return
        # roots store negative sizes; attach the smaller tree to the larger.
        if parent[a] > parent[b]:
            a, b = b, a
        parent[a] += parent[b]
        parent[b] = a
        pieces -= 1

    # run backwards: start from the web after all cuts and put the threads
    # back one by one, last cut first
    cut = bytearray(m)
    for edge in cuts:
        cut[edge] = 1
    for edge in range(m):
        if not cut[edge]:
            join(edge)
    for k in range(q - 1, -1, -1):
        edge = cuts[k]
        # a processed cut is replaced by its answer, avoiding another array.
        cuts[k] = pieces
        join(edge)
    print(" ".join(map(str, cuts)))


main()
