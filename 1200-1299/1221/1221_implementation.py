import sys


def largest(n, grid):
    # black[i][j]: black cells among the first j of row i
    black = []
    for row in grid:
        acc = [0]
        for v in row:
            acc.append(acc[-1] + v)
        black.append(acc)

    def ones(i, lo, hi):
        """Black cells of row i in columns lo..hi."""
        return black[i][hi + 1] - black[i][lo]

    def fits(ci, cj, r):
        # row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
        for d in range(-r, r + 1):
            i, side = ci + d, abs(d)
            left, right = cj - r, cj + r
            inner = r - side
            if ones(i, left, cj - inner - 1) != side or ones(i, cj + inner + 1, right) != side:
                return False
            if ones(i, cj - inner, cj + inner):
                return False
        return True

    # the white square needs a cell on every side of the centre, so r >= 1
    for r in range((n - 1) // 2, 0, -1):
        for ci in range(r, n - r):
            top, mid = grid[ci - r], grid[ci]
            for cj in range(r, n - r):
                # quick tests first: a white centre and tip, a black corner
                if mid[cj] or top[cj] or not top[cj - r]:
                    continue
                if fits(ci, cj, r):
                    return 2 * r + 1
    return 0


def main():
    tokens = sys.stdin.read().split()
    pos, out = 0, []
    while True:
        n = int(tokens[pos])
        pos += 1
        if n == 0:
            break
        # the cells may come with or without spaces between them
        cells = []
        while len(cells) < n * n:
            cells.extend(int(c) for c in tokens[pos])
            pos += 1
        grid = [cells[i * n : (i + 1) * n] for i in range(n)]
        best = largest(n, grid)
        out.append(str(best) if best else "No solution")
    print("\n".join(out))


main()
