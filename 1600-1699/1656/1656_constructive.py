def main():
    data = list(map(int, open(0).read().split()))
    n, heights = data[0], sorted(data[1:], reverse=True)
    mid = n // 2
    # cells by (nearer, farther) distance from the centre row and column:
    # along any row or column this grows outwards on each side
    cells = sorted(
        ((min(abs(r - mid), abs(c - mid)), max(abs(r - mid), abs(c - mid)), r, c)
         for r in range(n) for c in range(n))
    )
    grid = [[0] * n for _ in range(n)]
    for h, (_, _, r, c) in zip(heights, cells):
        grid[r][c] = h
    print("\n".join(" ".join(map(str, row)) for row in grid))


main()
