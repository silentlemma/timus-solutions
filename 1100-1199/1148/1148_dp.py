import sys
from array import array

# counts are kept only for every STRIDE-th height, so that the table fits in
# the memory limit; the heights between are recomputed by recursion
STRIDE = 4


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    total, height, base = next(tok), next(tok), next(tok)

    # a tower with h levels whose lowest has m bricks uses at most this many
    def most(h, m):
        return m * h + h * (h - 1) // 2

    # offset[h][m] starts the stored counts for h levels and m bricks below,
    # kept only for the widths that a tower can reach at that height
    offset = {}
    size = 0
    for h in range(STRIDE, height + 1, STRIDE):
        depth = height - h
        low = base - depth
        while low < 1:
            low += 2
        for m in range(low, base + depth + 1, 2):
            offset[h, m] = size
            size += most(h, m) + 1
    memo = array("q", [-1]) * size

    def count(n, h, m):
        # towers of h levels starting with m bricks that use at most n bricks
        if m == 0 or n < m:
            return 0
        if h == 1:
            return 1
        n = min(n, most(h, m))
        key = offset.get((h, m))
        if key is not None and memo[key + n] >= 0:
            return memo[key + n]
        ways = count(n - m, h - 1, m - 1) + count(n - m, h - 1, m + 1)
        if key is not None:
            memo[key + n] = ways
        return ways

    out = [str(count(total, height, base))]
    for k in tok:
        if k < 0:
            break
        # lexicographic order: the narrower next level comes first
        n, m, levels = total, base, [base]
        for h in range(height, 1, -1):
            fewer = count(n - m, h - 1, m - 1)
            n -= m
            if k <= fewer:
                m -= 1
            else:
                k -= fewer
                m += 1
            levels.append(m)
        out.append(" ".join(map(str, levels)))
    sys.stdout.write("\n".join(out) + "\n")


main()
