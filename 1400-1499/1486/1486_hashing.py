import sys

MOD = (1 << 61) - 1
ROW_BASE = 911382323
COL_BASE = 972663749


def find(grid, n, m, k):
    """Two different equal k x k squares as ((r1, c1), (r2, c2)), or None."""
    width = m - k + 1
    # hash of every window of k letters in every row
    power = pow(ROW_BASE, k, MOD)
    rows = []
    for line in grid:
        h, out = 0, []
        for j in range(m):
            h = (h * ROW_BASE + line[j]) % MOD
            if j >= k:
                h = (h - line[j - k] * power) % MOD
            if j >= k - 1:
                out.append(h)
        rows.append(out)
    # then of every window of k row hashes in every column
    power = pow(COL_BASE, k, MOD)
    seen = {}
    col = [0] * width
    for i in range(n):
        row = rows[i]
        old = rows[i - k] if i >= k else None
        for j in range(width):
            h = (col[j] * COL_BASE + row[j]) % MOD
            if old is not None:
                h = (h - old[j] * power) % MOD
            col[j] = h
            if i >= k - 1:
                here = (i - k + 1, j)
                other = seen.setdefault(h, here)
                if other != here and same(grid, other, here, k):
                    return other, here
    return None


def same(grid, a, b, k):
    return all(grid[a[0] + t][a[1] : a[1] + k] == grid[b[0] + t][b[1] : b[1] + k] for t in range(k))


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2 : 2 + n]
    # equal k x k squares contain equal (k - 1) x (k - 1) ones, so the
    # largest size can be found by binary search
    lo, hi, best = 1, min(n, m), None
    while lo <= hi:
        k = (lo + hi) // 2
        pair = find(grid, n, m, k)
        if pair:
            best, lo = (k, pair), k + 1
        else:
            hi = k - 1
    if best is None:
        print(0)
        return
    k, (a, b) = best
    print(k)
    print(a[0] + 1, a[1] + 1)
    print(b[0] + 1, b[1] + 1)


main()
