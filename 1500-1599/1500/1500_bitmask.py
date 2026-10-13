import sys
from itertools import combinations

HALF = 10  # categories are split into a low and a high half of the mask
FIELDS = 3  # two crossings and a category
HEADER = 3  # K, N and M


def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    k, n, m = data[:HEADER]
    roads = data[HEADER:]
    # by_category[u][c]: the crossings next to u along roads of category c
    by_category = [[0] * k for _ in range(n)]
    for i in range(m):
        a, b, c = roads[FIELDS * i : FIELDS * (i + 1)]
        by_category[a][c] |= 1 << b
        by_category[b][c] |= 1 << a

    # the neighbours of u under a set of categories, from two half tables
    low_size = min(k, HALF)
    high_size = k - low_size

    def table(u, offset, size):
        out = [0] * (1 << size)
        for s in range(1, 1 << size):
            low = s & -s
            out[s] = out[s ^ low] | by_category[u][offset + low.bit_length() - 1]
        return out

    low = [table(u, 0, low_size) for u in range(n)]
    high = [table(u, low_size, high_size) for u in range(n)]
    low_mask = (1 << low_size) - 1

    def connects(s):
        lo, hi = s & low_mask, s >> low_size
        reach = todo = 1  # crossing 0
        while todo:
            bit = todo & -todo
            todo ^= bit
            u = bit.bit_length() - 1
            fresh = (low[u][lo] | high[u][hi]) & ~reach
            reach |= fresh
            todo |= fresh
            if reach & 2:  # crossing 1
                return True
        return False

    # fewer permits first; the categories come out in increasing order
    for size in range(1, k + 1):
        for chosen in combinations(range(k), size):
            s = 0
            for c in chosen:
                s |= 1 << c
            if connects(s):
                print(size)
                print(" ".join(map(str, chosen)))
                return


main()
