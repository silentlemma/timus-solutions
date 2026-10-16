import sys

FAR = 1 << 40


def main():
    data = sys.stdin.buffer.read().split()
    n, s, k = int(data[0]), int(data[1]), int(data[2])
    size = 1
    while size <= n:
        size *= 2
    # latest[node]: the last obstacle whose lanes cover the node's whole range,
    # and the cost of a lane comes from the latest obstacle covering it, as
    # min(left[t] + x, right[t] - x), or from the start as |x - s| if none
    latest = [0] * (2 * size)
    left = [0] * (k + 1)
    right = [0] * (k + 1)

    def cost(x):
        t = 0
        node = x + size
        while node:
            if latest[node] > t:
                t = latest[node]
            node >>= 1
        if t == 0:
            return abs(x - s)
        return min(left[t] + x, right[t] - x)

    for t in range(1, k + 1):
        lo, hi = int(data[1 + 2 * t]), int(data[2 + 2 * t])
        # the cost stays one per lane apart, so going round the obstacle
        # only needs the lanes just beside it
        below = cost(lo - 1) if lo > 1 else FAR
        above = cost(hi + 1) if hi < n else FAR
        left[t] = below - (lo - 1)
        right[t] = above + hi + 1
        a, b = lo + size, hi + size + 1
        while a < b:
            if a & 1:
                latest[a] = t
                a += 1
            if b & 1:
                b -= 1
                latest[b] = t
            a >>= 1
            b >>= 1
    print(min(cost(x) for x in range(1, n + 1)))


main()
