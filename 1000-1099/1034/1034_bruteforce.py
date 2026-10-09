import sys
from itertools import combinations

MOVED = 3


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    col = [0] * n
    for i in range(n):
        col[int(data[1 + 2 * i]) - 1] = int(data[2 + 2 * i]) - 1
    # the diagonals r + c and r - c taken by the queens
    sums = {r + c for r, c in enumerate(col)}
    diffs = {r - c for r, c in enumerate(col)}
    count = 0
    for rows in combinations(range(n), MOVED):
        free_sums = sums - {r + col[r] for r in rows}
        free_diffs = diffs - {r - col[r] for r in rows}
        # all three queens move only when the columns are shifted cyclically
        for shift in range(1, MOVED):
            cells = [(r, col[rows[(k + shift) % MOVED]]) for k, r in enumerate(rows)]
            new_sums = {r + c for r, c in cells}
            new_diffs = {r - c for r, c in cells}
            if (
                len(new_sums) == MOVED
                and len(new_diffs) == MOVED
                and not new_sums & free_sums
                and not new_diffs & free_diffs
            ):
                count += 1
    print(count)


main()
