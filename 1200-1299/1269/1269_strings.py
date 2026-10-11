import sys
from array import array

ALPHABET = 256


def main():
    read = sys.stdin.buffer.readline
    n = int(read())
    words = [read().rstrip(b"\r\n") for _ in range(n)]
    total = sum(len(w) for w in words) + 1
    # build the trie as first-child / next-sibling lists
    child = array("i", [-1]) * total
    sibling = array("i", [-1]) * total
    byte = bytearray(total)
    ends = array("i", [0]) * total  # the longest word ending at a node
    nodes = 1
    for w in words:
        v = 0
        for c in w:
            u = child[v]
            while u >= 0 and byte[u] != c:
                u = sibling[u]
            if u < 0:
                u = nodes
                nodes += 1
                byte[u] = c
                sibling[u] = child[v]
                child[v] = u
            v = u
        ends[v] = max(ends[v], len(w))
    del words
    # renumber in breadth-first order: the children of v then take the
    # numbers first[v] .. first[v + 1] - 1, and label[u] is the byte
    # leading to u, so a child is found with one bytearray.find
    first = array("i", [0]) * (nodes + 1)
    label = bytearray(nodes)
    longest = array("i", [0]) * nodes
    old = array("i", [0])
    for v in range(nodes):
        first[v] = len(old)
        u = child[old[v]]
        while u >= 0:
            label[len(old)] = byte[u]
            longest[len(old)] = ends[u]
            old.append(u)
            u = sibling[u]
    first[nodes] = len(old)
    del child, sibling, byte, ends, old
    # failure links in the same order; a node also takes the longest word
    # of its failure node, which comes earlier
    fail = array("i", [0]) * nodes
    find = label.find
    for v in range(1, nodes):
        for u in range(first[v], first[v + 1]):
            c, f = label[u], fail[v]
            while True:
                g = find(c, first[f], first[f + 1])
                if g >= 0 or not f:
                    break
                f = fail[f]
            fail[u] = max(g, 0)
            longest[u] = max(longest[u], longest[fail[u]])
    # the root moves on every byte, so its moves get a full table
    root = array("i", [0]) * ALPHABET
    for u in range(first[0], first[1]):
        root[label[u]] = u
    widest = max(longest)  # no match is longer than the longest word
    m = int(read())
    for row in range(1, m + 1):
        line = read().rstrip(b"\r\n")
        v, best = 0, len(line) + 1
        for i, c in enumerate(line):
            while v:
                g = find(c, first[v], first[v + 1])
                if g >= 0:
                    v = g
                    break
                v = fail[v]
            else:
                v = root[c]
            h = longest[v]
            if h and i + 2 - h < best:
                best = i + 2 - h
            elif i + 1 - widest >= best:
                break  # no later match can start earlier
        if best <= len(line):
            print(row, best)
            return
    print("Passed")


main()
