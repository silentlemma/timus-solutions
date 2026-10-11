import sys


def main():
    words = sys.stdin.read().split()
    n = int(words[0])
    children = [[] for _ in range(n + 1)]
    value = [0] * (n + 1)
    pos = 1
    for v in range(2, n + 1):
        kind, parent = words[pos], int(words[pos + 1])
        pos += 2
        children[parent].append(v)
        if kind == "L":
            value[v] = int(words[pos])
            pos += 1
    # breadth-first order from the root, then values from the leaves up:
    # the first player moves at even depths and takes the largest result
    order, depth = [1], [0] * (n + 1)
    for v in order:
        for c in children[v]:
            depth[c] = depth[v] + 1
            order.append(c)
    for v in reversed(order):
        if children[v]:
            results = [value[c] for c in children[v]]
            value[v] = max(results) if depth[v] % 2 == 0 else min(results)
    print({1: "+1", 0: "0", -1: "-1"}[value[1]])


main()
