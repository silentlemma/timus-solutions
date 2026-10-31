import sys
from array import array


def main():
    n, x, y = map(int, sys.stdin.read().split())
    size = 1 << n
    # n <= 9 gives labels <= 87381; "I" cells take 4 bytes on the judge's platform,
    # enough for values up to 2^32 - 1.
    board = [array("I", [0]) * size for _ in range(size)]
    count = 0

    def tile(top, left, side, hr, hc):
        nonlocal count
        count += 1
        label = count
        half = side // 2
        middle_row, middle_col = top + half - 1, left + half - 1
        # reverse order matches the simple solution's last-in-first-out stack.
        for dr in (1, 0):
            for dc in (1, 0):
                r0, c0 = top + dr * half, left + dc * half
                if r0 <= hr < r0 + half and c0 <= hc < c0 + half:
                    r, c = hr, hc
                else:
                    r, c = middle_row + dr, middle_col + dc
                    board[r][c] = label
                if half > 1:
                    tile(r0, c0, half, r, c)

    tile(0, 0, size, x - 1, y - 1)
    # retain at most one output row, not the complete decimal board.
    for row in board:
        sys.stdout.write(" ".join(map(str, row)) + "\n")


main()
