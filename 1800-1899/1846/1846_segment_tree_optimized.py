import sys
from math import gcd

OUTPUT_BLOCK = 1024


def main():
    lines = sys.stdin.buffer.read().splitlines()
    q = int(lines.pop(0))
    # Lists avoid boxing array cells on every tree access; values still share
    # one leaf and one multiplicity counter per distinct number.
    tree = [0] * (2 * q)
    counts = [0] * q
    leaves = {}
    output = []
    for line in lines:
        x = int(line[2:])
        index = leaves.get(x)
        if index is None:
            index = len(leaves)
            leaves[x] = index
        counts[index] += 1 if line[:1] == b"+" else -1
        v = q + index
        value = x if counts[index] else 0
        if tree[v] != value:
            tree[v] = value
            v //= 2
            while v:
                value = gcd(tree[2 * v], tree[2 * v + 1])
                if tree[v] == value:
                    break
                tree[v] = value
                v //= 2
        output.append(str(tree[1] or 1))
        if len(output) == OUTPUT_BLOCK:
            sys.stdout.write("\n".join(output) + "\n")
            output.clear()
    if output:
        sys.stdout.write("\n".join(output) + "\n")


main()
