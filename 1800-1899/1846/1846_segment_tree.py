import sys
from math import gcd


def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    size = 1
    while size < q:
        size *= 2
    # every addition gets its own leaf; an empty leaf holds 0, which does
    # not change a gcd
    tree = [0] * (2 * size)
    leaves = {}  # value -> leaves that hold it
    out = []
    for k in range(q):
        x = int(data[2 + 2 * k])
        if data[1 + 2 * k] == b"+":
            leaves.setdefault(x, []).append(k)
            v, value = k + size, x
        else:
            v, value = leaves[x].pop() + size, 0
        tree[v] = value
        v >>= 1
        while v:
            # once a node keeps its value, so do all above it
            value = gcd(tree[2 * v], tree[2 * v + 1])
            if tree[v] == value:
                break
            tree[v] = value
            v >>= 1
        out.append(tree[1] or 1)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
