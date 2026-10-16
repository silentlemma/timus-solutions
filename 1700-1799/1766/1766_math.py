import sys

SIDE = 8


def main():
    v = [int(w) for w in sys.stdin.read().split()]
    grid = [v[r * SIDE:(r + 1) * SIDE] for r in range(SIDE)]
    # moving from u to a neighbour v with weight w(v) / W(u), where W(u) sums
    # the weights around u, the walk is balanced by w(u) W(u) in every cell,
    # and after so many steps it has settled into that distribution
    score = [[0] * SIDE for _ in range(SIDE)]
    for r in range(SIDE):
        for c in range(SIDE):
            around = sum(grid[y][x]
                         for y in range(max(0, r - 1), min(SIDE, r + 2))
                         for x in range(max(0, c - 1), min(SIDE, c + 2))
                         if (y, x) != (r, c))
            score[r][c] = grid[r][c] * around
    total = sum(map(sum, score))
    for row in score:
        print(" ".join("%.15f" % (s / total) for s in row))


main()
