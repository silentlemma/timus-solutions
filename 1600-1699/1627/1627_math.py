import sys

MOD = 10**9


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    grid = data[2 : 2 + n]
    ids = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                ids[i, j] = len(ids)
    v = len(ids)
    # the Laplacian of the bedroom graph; by the matrix-tree theorem any
    # cofactor counts its spanning trees (0 when it is disconnected)
    lap = [[0] * v for _ in range(v)]
    for (i, j), u in ids.items():
        for w in (ids.get((i + 1, j)), ids.get((i, j + 1))):
            if w is not None:
                lap[u][u] += 1
                lap[w][w] += 1
                lap[u][w] -= 1
                lap[w][u] -= 1
    a = [row[: v - 1] for row in lap[: v - 1]]
    # Bareiss elimination keeps every entry an exact integer
    size, sign, prev = v - 1, 1, 1
    for k in range(size - 1):
        pivot_row = next((r for r in range(k, size) if a[r][k]), -1)
        if pivot_row < 0:
            print(0)
            return
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot, row_k = a[k][k], a[k]
        for i in range(k + 1, size):
            row_i, f = a[i], a[i][k]
            for j in range(k + 1, size):
                row_i[j] = (row_i[j] * pivot - f * row_k[j]) // prev
            row_i[k] = 0
        prev = pivot
    det = sign * a[size - 1][size - 1] if size else 1
    print(det % MOD)


main()
