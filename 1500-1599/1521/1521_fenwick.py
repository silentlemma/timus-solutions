import sys


def main():
    n, k = map(int, sys.stdin.read().split())
    # a Fenwick tree over the circle: 1 for a soldier still marching
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] += 1
        parent = i + (i & -i)
        if parent <= n:
            tree[parent] += tree[i]
    top = 1 << n.bit_length()
    order = []
    rank, left = 0, n
    for _ in range(n):
        # the soldier k places ahead, counting among those still marching
        rank = (rank + k - 1) % left
        # descend to the (rank + 1)-th remaining soldier
        pos, need, step = 0, rank + 1, top
        while step:
            nxt = pos + step
            if nxt <= n and tree[nxt] < need:
                pos = nxt
                need -= tree[nxt]
            step >>= 1
        pos += 1
        order.append(pos)
        while pos <= n:
            tree[pos] -= 1
            pos += pos & -pos
        left -= 1
    print(" ".join(map(str, order)))


main()
