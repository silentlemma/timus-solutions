"""Checker: the expected number of parts, then n rows of n lowercase
letters whose 4-connected one-letter regions are exactly that many parts,
all different up to rotation with the chessboard colours kept."""

import sys

TURNS = 4


class Bad(Exception):
    pass


def canonical(cells):
    """The smallest description of a coloured part over its rotations."""
    best = None
    for _ in range(TURNS):
        low_x = min(x for x, _, _ in cells)
        low_y = min(y for _, y, _ in cells)
        key = tuple(sorted((x - low_x, y - low_y, c) for x, y, c in cells))
        best = key if best is None or key < best else best
        cells = [(y, -x, c) for x, y, c in cells]
    return best


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    want = int(open(expected).read().split()[0])
    words = open(output).read().split()
    if not words or words[0] != str(want):
        raise Bad("expected %d parts" % want)
    board = words[1:]
    if len(board) != n or any(len(row) != n or not row.isalpha() or not row.islower()
                              for row in board):
        raise Bad("the board must be %d rows of %d lowercase letters" % (n, n))
    seen = [[False] * n for _ in range(n)]
    parts = set()
    count = 0
    for i in range(n):
        for j in range(n):
            if seen[i][j]:
                continue
            seen[i][j] = True
            stack, cells = [(i, j)], []
            while stack:
                x, y = stack.pop()
                cells.append((x, y, (x + y) % 2))
                for u, v in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= u < n and 0 <= v < n and not seen[u][v] and board[u][v] == board[x][y]:
                        seen[u][v] = True
                        stack.append((u, v))
            count += 1
            parts.add(canonical(cells))
    if count != want:
        raise Bad("the board has %d parts, not %d" % (count, want))
    if len(parts) != count:
        raise Bad("two parts are the same")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
