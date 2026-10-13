import sys


def main():
    n, x, y, *_ = map(int, sys.stdin.read().split())
    size = 1 << n
    board = [[0] * size for _ in range(size)]
    count = 0
    # each square has one cell that is already taken: the hole or a piece of
    # the tromino in the middle of the square above it
    stack = [(0, 0, size, x - 1, y - 1)]
    while stack:
        top, left, side, hr, hc = stack.pop()
        if side == 1:
            continue
        half = side // 2
        count += 1
        for dr in (0, 1):
            for dc in (0, 1):
                r0, c0 = top + dr * half, left + dc * half
                if r0 <= hr < r0 + half and c0 <= hc < c0 + half:
                    stack.append((r0, c0, half, hr, hc))
                else:
                    # the cell of this quarter next to the middle of the square
                    r, c = top + half - 1 + dr, left + half - 1 + dc
                    board[r][c] = count
                    stack.append((r0, c0, half, r, c))
    sys.stdout.write("\n".join(" ".join(map(str, row)) for row in board) + "\n")


main()
