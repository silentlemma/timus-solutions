import sys

SIDE = 3  # seats on each side of the aisle
MASKS = 1 << SIDE
RIGHT_START = 6  # the right seats in a row description
LETTERS = "ABCDEF"


def best_side(rows, offset):
    """The largest set of free, pairwise non-adjacent seats on one side, as a
    mask per row; seats in a row and in the next row may not share a column
    or stand next to each other."""
    n = len(rows)
    best = [[-1] * MASKS for _ in range(n + 1)]
    source = [[0] * MASKS for _ in range(n + 1)]
    best[0][0] = 0
    for r, row in enumerate(rows):
        free = sum(1 << s for s in range(SIDE) if row[offset + s] == ".")
        for cur in range(MASKS):
            if cur & ~free or cur & (cur << 1):
                continue
            count = bin(cur).count("1")
            for prev in range(MASKS):
                if best[r][prev] < 0 or (prev | prev << 1 | prev >> 1) & cur:
                    continue
                if best[r][prev] + count > best[r + 1][cur]:
                    best[r + 1][cur] = best[r][prev] + count
                    source[r + 1][cur] = prev
    mask = max(range(MASKS), key=lambda m: best[n][m])
    chosen = [0] * n
    for r in range(n, 0, -1):
        chosen[r - 1] = mask
        mask = source[r][mask]
    return chosen


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    rows = data[2:2 + n]
    seats = []
    for side in range(2):
        chosen = best_side(rows, side * RIGHT_START)
        for r in range(n):
            for s in range(SIDE):
                if chosen[r] >> s & 1:
                    seats.append("%d%s" % (r + 1, LETTERS[side * SIDE + s]))
    if len(seats) < k:
        print("PORAZHENIE")
    else:
        print("\n".join(["POBEDA"] + seats[:k]))


main()
