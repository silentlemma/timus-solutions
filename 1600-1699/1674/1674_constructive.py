import sys

BLOCK = 4  # rows or columns added at a time
SMALLEST = 4  # boards with a shorter side have no tour, apart from 2 x 2
BOTTOM = SMALLEST - 1  # the last row of a strip

NO_TOUR = (5, 5)  # the one board with both sides at least 4 and no tour
ODD_BASE = (5, 9)  # the base when both sides are of the form 4k + 1

# closed tours of small boards, as lists of (row, column) ending at the start,
# printed by 1674_constructive_table.py
BASES = {
    (5, 6): [(0, 0), (0, 1), (1, 2), (2, 2), (2, 3), (1, 3), (0, 2), (0, 3), (1, 4), (0, 4), (0, 5),
             (1, 5), (2, 4), (2, 5), (3, 5), (3, 4), (4, 5), (4, 4), (3, 3), (4, 3), (4, 2), (3, 2),
             (4, 1), (4, 0), (3, 0), (3, 1), (2, 0), (2, 1), (1, 0), (1, 1), (0, 0)],
    (5, 7): [(0, 0), (0, 1), (1, 2), (2, 2), (2, 3), (1, 3), (0, 2), (0, 3), (1, 4), (0, 4), (0, 5),
             (1, 5), (0, 6), (1, 6), (2, 5), (2, 6), (3, 6), (3, 5), (4, 6), (4, 5), (3, 4), (2, 4),
             (3, 3), (4, 4), (4, 3), (3, 2), (4, 2), (3, 1), (4, 1), (4, 0), (3, 0), (2, 1), (2, 0),
             (1, 0), (1, 1), (0, 0)],
    (6, 6): [(0, 0), (0, 1), (1, 2), (1, 3), (0, 2), (0, 3), (1, 4), (0, 4), (0, 5), (1, 5), (2, 4),
             (2, 5), (3, 5), (3, 4), (2, 3), (2, 2), (3, 2), (3, 3), (4, 4), (4, 5), (5, 5), (5, 4),
             (4, 3), (5, 3), (5, 2), (4, 2), (5, 1), (5, 0), (4, 0), (4, 1), (3, 0), (3, 1), (2, 0),
             (2, 1), (1, 0), (1, 1), (0, 0)],
    (6, 7): [(0, 0), (0, 1), (1, 2), (1, 3), (0, 2), (0, 3), (1, 4), (0, 4), (0, 5), (1, 5), (0, 6),
             (1, 6), (2, 5), (2, 4), (3, 5), (2, 6), (3, 6), (4, 5), (4, 6), (5, 6), (5, 5), (4, 4),
             (5, 4), (4, 3), (3, 4), (2, 3), (2, 2), (3, 3), (3, 2), (4, 2), (5, 3), (5, 2), (4, 1),
             (5, 1), (5, 0), (4, 0), (3, 1), (3, 0), (2, 0), (2, 1), (1, 0), (1, 1), (0, 0)],
    (7, 7): [(0, 0), (0, 1), (1, 2), (1, 3), (0, 2), (0, 3), (1, 4), (0, 4), (0, 5), (1, 5), (0, 6),
             (1, 6), (2, 5), (2, 4), (3, 5), (2, 6), (3, 6), (4, 5), (4, 6), (5, 6), (5, 5), (6, 6),
             (6, 5), (5, 4), (6, 4), (5, 3), (4, 4), (3, 4), (2, 3), (2, 2), (3, 3), (3, 2), (4, 3),
             (4, 2), (5, 2), (6, 3), (6, 2), (5, 1), (6, 1), (6, 0), (5, 0), (4, 1), (4, 0), (3, 0),
             (3, 1), (2, 0), (2, 1), (1, 0), (1, 1), (0, 0)],
    (5, 9): [(0, 0), (0, 1), (1, 2), (2, 2), (2, 3), (1, 3), (0, 2), (0, 3), (1, 4), (2, 4), (2, 5),
             (1, 5), (0, 4), (0, 5), (1, 6), (0, 6), (0, 7), (1, 7), (0, 8), (1, 8), (2, 7), (2, 8),
             (3, 8), (3, 7), (4, 8), (4, 7), (3, 6), (2, 6), (3, 5), (4, 6), (4, 5), (3, 4), (4, 4),
             (3, 3), (4, 3), (4, 2), (3, 2), (4, 1), (4, 0), (3, 0), (3, 1), (2, 0), (2, 1), (1, 0),
             (1, 1), (0, 0)],
}


def strip(m):
    """A closed tour of the 4 x m board: along the top two rows in a zigzag,
    down the right end, back along the bottom two rows, up the left end."""
    path = [(0, 0), (0, 1), (1, 1)]
    for c in range(2, m - 1):
        path.append((0, c))
        if c < m - 2:
            path.append((1, c))
    path += [(0, m - 1), (1, m - 1), (1, m - 2), (2, m - 1), (BOTTOM, m - 1)]
    for c in range(m - 2, 1, -1):
        path += [(BOTTOM, c), (2, c)]
    path += [(BOTTOM, 1), (BOTTOM, 0), (2, 0), (2, 1), (1, 0), (0, 0)]
    return path


def flip(path):
    return [(c, r) for r, c in path]


def base(n, m):
    if n == SMALLEST:
        return strip(m)
    if m == SMALLEST:
        return flip(strip(n))
    if (n, m) in BASES:
        return BASES[(n, m)]
    return flip(BASES[(m, n)])


def main():
    n, m = (int(w) for w in sys.stdin.read().split())
    grid = [bytearray(b" " * (2 * m - 1)) for _ in range(2 * n - 1)]
    for r in range(n):
        for c in range(m):
            grid[2 * r][2 * c] = ord("o")

    def mark(a, b, ch=None):
        """Draw (or with ch = ' ', erase) the move between cells a and b."""
        if ch is None:
            if a[0] == b[0]:
                ch = "-"
            elif a[1] == b[1]:
                ch = "|"
            else:
                ch = "\\" if b[0] - a[0] == b[1] - a[1] else "/"
        grid[a[0] + b[0]][a[1] + b[1]] = ord(ch)

    def draw(path, dr, dc, swap):
        cells = [((c, r) if swap else (r, c)) for r, c in path]
        for (r1, c1), (r2, c2) in zip(cells, cells[1:]):
            mark((r1 + dr, c1 + dc), (r2 + dr, c2 + dc))

    if (n, m) == (2, 2):
        draw([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)], 0, 0, False)
    elif n < SMALLEST or m < SMALLEST or (n, m) == NO_TOUR:
        print("No")
        return
    else:
        # a base board whose sides leave multiples of 4; two sides of the form
        # 4k + 1 start from 5 x 9 instead, as 5 x 5 has no tour
        if n % BLOCK == 1 and m % BLOCK == 1:
            bn, bm = ODD_BASE if m >= ODD_BASE[1] else ODD_BASE[::-1]
        else:
            bn, bm = SMALLEST + (n - SMALLEST) % BLOCK, SMALLEST + (m - SMALLEST) % BLOCK
        draw(base(bn, bm), 0, 0, False)
        # each new 4-wide block has its own strip tour; three edges at the
        # seam are swapped for three others, which joins the two cycles
        for cur in range(bm, m, BLOCK):
            draw(strip(bn), 0, cur, True)
            mark((0, cur - 1), (1, cur - 1), " ")
            mark((0, cur), (1, cur), " ")
            mark((2, cur), (1, cur + 1), " ")
            mark((0, cur - 1), (1, cur))
            mark((1, cur - 1), (2, cur))
            mark((0, cur), (1, cur + 1))
        for cur in range(bn, n, BLOCK):
            draw(strip(m), cur, 0, False)
            mark((cur - 1, 0), (cur - 1, 1), " ")
            mark((cur, 0), (cur, 1), " ")
            mark((cur, 2), (cur + 1, 1), " ")
            mark((cur - 1, 0), (cur, 1))
            mark((cur - 1, 1), (cur, 2))
            mark((cur, 0), (cur + 1, 1))
    sys.stdout.write("Yes\n" + "\n".join(row.decode() for row in grid) + "\n")


main()
