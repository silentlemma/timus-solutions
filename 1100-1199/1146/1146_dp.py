import sys


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n = next(tok)
    grid = [[next(tok) for _ in range(n)] for _ in range(n)]
    best = grid[0][0]
    for top in range(n):
        # column sums of the rows from top to bottom, then the best run of
        # neighbouring columns by Kadane's scan
        cols = [0] * n
        for bottom in range(top, n):
            row = grid[bottom]
            run = 0
            for c in range(n):
                cols[c] += row[c]
                run = cols[c] if run < 0 else run + cols[c]
                if run > best:
                    best = run
    print(best)


main()
