import sys

MOD = 10**9


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    # count values from the top, so that "larger" becomes a prefix
    flipped = [n + 1 - int(x) for x in data[2 : 2 + n]]
    # ends[i]: decreasing runs of the current length that end at position i
    ends = [1] * n
    for _ in range(k - 1):
        tree = [0] * (n + 1)
        nxt = [0] * n
        for i, v in enumerate(flipped):
            # the runs one shorter that end earlier at a larger value
            s, j = 0, v - 1
            while j:
                s += tree[j]
                j &= j - 1
            nxt[i] = s % MOD
            add, j = ends[i], v
            while j <= n:
                tree[j] += add
                j += j & -j
        ends = nxt
    print(sum(ends) % MOD)


main()
