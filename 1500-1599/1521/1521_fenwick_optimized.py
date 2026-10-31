import sys
from array import array

# flush bounded batches instead of retaining the entire elimination order.
OUTPUT_BATCH = 1024


def main():
    n, k = map(int, sys.stdin.buffer.read().split())
    # a fenwick tree over the circle: 1 for a soldier still marching
    # initially every interval is full, so its count is lowbit(i) <= n <= 100000.
    tree = array("I", (i & -i for i in range(n + 1)))
    top = 1 << (n.bit_length() - 1)
    output = []
    rank = 0
    for left in range(n, 0, -1):
        # the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left
        # descend to the (rank + 1)-th remaining soldier
        pos, need, step = 0, rank + 1, top
        while step:
            nxt = pos + step
            if nxt <= n:
                count = tree[nxt]
                if count < need:
                    pos = nxt
                    need -= count
                else:
                    # this fenwick interval contains the soldier being removed.
                    tree[nxt] = count - 1
            step >>= 1
        output.append(str(pos + 1))
        if len(output) == OUTPUT_BATCH or left == 1:
            sys.stdout.write(" ".join(output) + (" " if left > 1 else "\n"))
            output.clear()


main()
