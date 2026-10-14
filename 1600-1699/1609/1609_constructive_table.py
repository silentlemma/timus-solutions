"""Print the table PATTERNS of the solutions: for every board n x m with
n <= m <= 10 and nm even, the cells of a smallest set of tiles after which
the rest of the board has exactly one tiling, row by row, as "n m cells".

For k = 0, 1, 2, ... every set of k non-overlapping tiles is tried, the
tiles in a fixed order, and the first set that works is printed. A set
works when the free cells have exactly one tiling, which by Kotzig's
theorem holds exactly when repeatedly covering a cell with a single free
neighbour uses them all up, and when the covered cells also tile in only
one way. The exhaustive failure at k - 1 proves that k is the least.
Slow: the 10 x 10 board alone takes minutes.
"""

import sys

LARGEST = 10


def board(n, m):
    full = (1 << (n * m)) - 1
    not_left = full
    not_right = full
    for r in range(n):
        not_left &= ~(1 << (r * m))
        not_right &= ~(1 << (r * m + m - 1))
    return full, not_left, not_right


def unique_tiling(cells, n, m, not_left, not_right):
    """Whether the cells have exactly one tiling, by peeling forced tiles."""
    while cells:
        right = (cells >> 1) & not_right & cells
        left = (cells << 1) & not_left & cells
        down = (cells >> m) & cells
        up = (cells << m) & cells
        some = right | left | down | up
        if cells & ~some:
            return False  # a cell with no free neighbour
        # cells with exactly one free neighbour
        two = (right & left) | (down & up) | ((right | left) & (down | up))
        single = cells & ~two
        if not single:
            return False  # every cell has two choices: a cycle, more than one tiling
        low = single & -single
        if low & right:
            partner = low << 1
        elif low & left:
            partner = low >> 1
        elif low & down:
            partner = low << m
        else:
            partner = low >> m
        cells &= ~(low | partner)
    return True


def tiles(n, m):
    out = []
    for r in range(n):
        for c in range(m):
            cell = 1 << (r * m + c)
            if c + 1 < m:
                out.append(cell | cell << 1)
            if r + 1 < n:
                out.append(cell | cell << m)
    return out


def smallest(n, m):
    full, not_left, not_right = board(n, m)
    pieces = tiles(n, m)

    def works(covered):
        return (unique_tiling(full & ~covered, n, m, not_left, not_right)
                and unique_tiling(covered, n, m, not_left, not_right))

    def search(start, left, covered):
        if left == 0:
            return covered if works(covered) else None
        for i in range(start, len(pieces)):
            piece = pieces[i]
            if covered & piece:
                continue
            found = search(i + 1, left - 1, covered | piece)
            if found is not None:
                return found
        return None

    k = 0
    while True:
        found = search(0, k, 0)
        if found is not None:
            return found
        k += 1


def main():
    sys.setrecursionlimit(10000)
    for n in range(1, LARGEST + 1):
        for m in range(n, LARGEST + 1):
            if n * m % 2:
                continue
            covered = smallest(n, m)
            cells = "".join("1" if covered >> i & 1 else "0" for i in range(n * m))
            print(n, m, cells, flush=True)


main()
