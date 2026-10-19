import sys

MOVES = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
LABELS = ("King", "Knight", "Bishop", "Rook", "Queen")


def solve(n, x, y):
    king = (1 + (x > 1) + (x < n)) * (1 + (y > 1) + (y < n)) - 1
    knight = sum(1 <= x + dx <= n and 1 <= y + dy <= n for dx, dy in MOVES)
    bishop = min(x - 1, y - 1) + min(x - 1, n - y) + min(n - x, y - 1) + min(n - x, n - y)
    rook = 2 * (n - 1)
    return [king, knight, bishop, rook, rook + bishop]


if __name__ == "__main__":
    values = map(int, sys.stdin.buffer.read().split())
    for label, count in zip(LABELS, solve(*values)):
        print(f"{label}: {count}")
