import sys
from array import array

ADD, ASK = 1, 2  # record kinds; any other kind ends the input
ADD_LEN = 5  # the kind, then x y z K
ASK_LEN = 7  # the kind, then x1 y1 z1 x2 y2 z2


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    side = n + 1
    # a 3D Fenwick tree, indices from 1; 64-bit cells keep memory flat
    tree = array("q", [0]) * (side * side * side)

    def add(x, y, z, k):
        i = x
        while i <= n:
            j = y
            while j <= n:
                base = (i * side + j) * side
                w = z
                while w <= n:
                    tree[base + w] += k
                    w += w & -w
                j += j & -j
            i += i & -i

    def prefix(x, y, z):
        total = 0
        i = x
        while i > 0:
            j = y
            while j > 0:
                base = (i * side + j) * side
                w = z
                while w > 0:
                    total += tree[base + w]
                    w -= w & -w
                j -= j & -j
            i -= i & -i
        return total

    out = []
    pos = 1
    while True:
        kind = int(data[pos])
        if kind == ADD:
            x, y, z, k = (int(v) for v in data[pos + 1 : pos + ADD_LEN])
            add(x + 1, y + 1, z + 1, k)
            pos += ADD_LEN
        elif kind == ASK:
            x1, y1, z1, x2, y2, z2 = (int(v) for v in data[pos + 1 : pos + ASK_LEN])
            x2, y2, z2 = x2 + 1, y2 + 1, z2 + 1
            # inclusion and exclusion over the eight corners of the box
            total = (
                prefix(x2, y2, z2)
                - prefix(x1, y2, z2)
                - prefix(x2, y1, z2)
                - prefix(x2, y2, z1)
                + prefix(x1, y1, z2)
                + prefix(x1, y2, z1)
                + prefix(x2, y1, z1)
                - prefix(x1, y1, z1)
            )
            out.append(total)
            pos += ASK_LEN
        else:
            break
    sys.stdout.write("".join("%d\n" % v for v in out))


main()
