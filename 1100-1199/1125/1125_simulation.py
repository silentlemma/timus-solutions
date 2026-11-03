from math import isqrt
import sys

COLOUR_XOR = ord("W") ^ ord("B")


def main():
    stream = sys.stdin.buffer
    m, n = map(int, stream.readline().split())
    if m == 0 or n == 0:
        sys.stdout.write("\n" * m)
        return
    board = [bytearray(stream.readline().strip()) for _ in range(m)]
    offsets = [
        (dr, dc)
        for dr in range(1 - m, m)
        for dc in range(1 - n, n)
        if isqrt(dr * dr + dc * dc) ** 2 == dr * dr + dc * dc
    ]
    # Each odd visit is undone by toggling all its valid integer-distance cells.
    for r in range(m):
        for c, value in enumerate(stream.readline().split()):
            if int(value) & 1:
                for dr, dc in offsets:
                    a, b = r + dr, c + dc
                    if 0 <= a < m and 0 <= b < n:
                        board[a][b] ^= COLOUR_XOR
    sys.stdout.write("\n".join(row.decode() for row in board) + "\n")


main()
