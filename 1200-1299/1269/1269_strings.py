import sys
from array import array
from io import BytesIO

ALPHABET = 256
DENSE_ENTRIES = 1 << 19
BRANCH = ALPHABET - 1
LEAF = ALPHABET - 2


def main():
    read = BytesIO(sys.stdin.buffer.read()).readline
    n = int(read())
    words = sorted(read().removesuffix(b"\n").removesuffix(b"\r") for _ in range(n))
    mapping = bytearray(ALPHABET)
    for c in b"".join(words):
        mapping[c] = 1
    width = 1
    for c in range(ALPHABET):
        if mapping[c]:
            mapping[c] = width
            width += 1
    total = sum(len(w) for w in words) + 1
    # Sorted words reuse their common prefix without searching sibling lists.
    child = array("i", [-1]) * total
    sibling = array("i", [-1]) * total
    byte = bytearray(total)
    ends = array("i", [0]) * total  # the longest word ending at a node
    nodes = 1
    path = array("i", [0]) * (max(map(len, words)) + 1)
    previous = b""
    for w in words:
        common = 0
        limit = min(len(previous), len(w))
        while common < limit and previous[common] == w[common]:
            common += 1
        v = path[common]
        for c in w[common:]:
            u = nodes
            nodes += 1
            byte[u] = mapping[c]
            sibling[u] = child[v]
            child[v] = u
            v = u
            common += 1
            path[common] = v
        ends[v] = len(w)
        previous = w
    del words, path, previous
    # Breadth-first numbering keeps each set of children contiguous and puts
    # failure targets before their descendants.
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
    # Cache complete transitions for the first states, within a fixed budget.
    # Copying a failure row fills its inherited transitions in native code.
    fail = array("i", [0]) * nodes
    dense_nodes = min(nodes, DENSE_ENTRIES // width)
    table = array("i", [0]) * (dense_nodes * width)
    # Sparse single-child states need only a byte comparison.
    direct = bytearray([LEAF]) * nodes
    find = label.find
    for u in range(first[0], first[1]):
        table[label[u]] = u
    for v in range(1, nodes):
        f = fail[v]
        if v >= dense_nodes:
            count = first[v + 1] - first[v]
            if count == 1:
                direct[v] = label[first[v]]
            elif count:
                direct[v] = BRANCH
        for u in range(first[v], first[v + 1]):
            c = label[u]
            g = f
            while g >= dense_nodes:
                h = find(c, first[g], first[g + 1])
                if h >= 0:
                    g = h
                    break
                g = fail[g]
            else:
                g = table[g * width + c]
            fail[u] = g
            if longest[g] > longest[u]:
                longest[u] = longest[g]
        if v < dense_nodes:
            offset = v * width
            start = f * width
            table[offset:offset + width] = table[start:start + width]
            for u in range(first[v], first[v + 1]):
                table[offset + label[u]] = u
    widest = max(longest)  # no match is longer than the longest word
    m = int(read())
    for row in range(1, m + 1):
        line = read()
        if line == b"\n" or line == b"\r\n":
            continue
        # Keep carriage returns as data; unused bytes reset the automaton.
        line = line.translate(mapping)
        v, best = 0, len(line) + 1
        for i, c in enumerate(line):
            while v >= dense_nodes:
                kind = direct[v]
                if kind == c:
                    v = first[v]
                    break
                if kind == BRANCH:
                    g = find(c, first[v], first[v + 1])
                    if g >= 0:
                        v = g
                        break
                v = fail[v]
            else:
                v = table[v * width + c]
            h = longest[v]
            if h and i + 2 - h < best:
                best = i + 2 - h
            elif i + 1 - widest >= best:
                break
        if best <= len(line):
            print(row, best)
            return
    print("Passed")


main()
