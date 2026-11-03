import sys
from array import array

ADD, ASK = 1, 2  # record kinds; any other kind ends the input
ADD_LEN = 5  # the kind, then x y z K
ASK_LEN = 7  # the kind, then x1 y1 z1 x2 y2 z2


def main():
    lines = iter(sys.stdin.buffer)
    n = int(next(lines))
    side = n + 1
    # Each node sums nonnegative sectors: at most100002*20000<2**31.
    # Python totals remain unbounded for inclusion-exclusion intermediates.
    tree = array("i", [0]) * (side * side * side)

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

    write = sys.stdout.write
    for line in lines:
        record = list(map(int, line.split()))
        kind = record[0]
        if kind == ADD:
            _, x, y, z, k = record
            add(x + 1, y + 1, z + 1, k)
        elif kind == ASK:
            _, x1, y1, z1, x2, y2, z2 = record
            x2, y2, z2 = x2 + 1, y2 + 1, z2 + 1
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
            write("%d\n" % total)
        else:
            break


main()
