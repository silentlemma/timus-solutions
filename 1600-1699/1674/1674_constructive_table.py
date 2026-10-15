"""Print the table BASES of the solutions: a closed tour of each small base
board, as "rows columns" and then the (row, column) cells in order, ending
at the start.

A tour starts in the top left corner, moves like a king, never passes a cell
straight through, never crosses itself (two diagonals of one square), and
holds the two moves the solutions replace when they join blocks: down the
right edge from the top, (0, M-1)-(1, M-1), and along the bottom from the
left corner, (N-1, 0)-(N-1, 1). A search takes the cells row by row and
gives each its moves to later neighbours (see tours). A tour is taken only
if every board the solutions build from it, with up to eight more rows and
columns and turned on its side, is a valid tour as well.
"""

import sys

BASES = [(5, 6), (5, 7), (6, 6), (6, 7), (7, 7), (5, 9)]
BLOCK = 4
SMALLEST = 4
BOTTOM = SMALLEST - 1
DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
GROWTH = (0, BLOCK, 2 * BLOCK)  # extra rows and columns tried in the check


def square(a, b):
    """The unit square of a diagonal move, or None for a straight one."""
    if a[0] != b[0] and a[1] != b[1]:
        return (min(a[0], b[0]), min(a[1], b[1]))
    return None


def tours(n, m):
    """Closed tours of the n x m board in the order of the search.

    The cells are taken row by row; each picks moves to the neighbours after
    it (east, south-east, south, south-west) so that it has exactly two. The
    two moves of a cell must not be opposite, a south-east move must not cross
    the south-west move of the next cell, no neighbour may get a third move,
    and a move may close a cycle only as the last move of the whole tour.
    """
    cells = n * m
    forward = [(0, 1), (1, 1), (1, 0), (1, -1)]  # E, SE, S, SW
    required = {frozenset(((0, m - 1), (1, m - 1))), frozenset(((n - 1, 0), (n - 1, 1)))}
    links = {(r, c): [] for r in range(n) for c in range(m)}
    parent = list(range(cells))
    size = [1] * cells
    count = [0]

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def opposite(a, b, cell):
        return a[0] + b[0] == 2 * cell[0] and a[1] + b[1] == 2 * cell[1]

    def add(a, b):
        """Join a and b; returns the undo record, or None if not allowed."""
        if len(links[b]) >= 2:
            return None
        for x in links[a]:
            if opposite(x, b, a):
                return None
        for x in links[b]:
            if opposite(x, a, b):
                return None
        ra, rb = find(a[0] * m + a[1]), find(b[0] * m + b[1])
        if ra == rb and count[0] + 1 < cells:
            return None  # a cycle before every cell is on it
        links[a].append(b)
        links[b].append(a)
        count[0] += 1
        if ra == rb:
            return (a, b, None)
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return (a, b, rb)

    def undo(record):
        a, b, joined = record
        links[a].pop()
        links[b].pop()
        count[0] -= 1
        if joined is not None:
            root = parent[joined]
            size[root] -= size[joined]
            parent[joined] = joined

    def options(cell):
        """The forward moves of a cell that are allowed on their own."""
        r, c = cell
        out = []
        for dr, dc in forward:
            other = (r + dr, c + dc)
            if not (0 <= other[0] < n and 0 <= other[1] < m):
                continue
            if (dr, dc) == (1, -1) and (r, c - 1) in links and (r + 1, c) in links[(r, c - 1)]:
                continue  # crosses the south-east move of the cell on the left
            out.append(other)
        return out

    def place(index):
        if index == cells:
            yield trace()
            return
        cell = divmod(index, m)
        need = 2 - len(links[cell])
        if need < 0:
            return
        moves = options(cell)
        # the required moves start at their upper or left end
        must = [x for x in moves if frozenset((cell, x)) in required]
        for choice in subsets(moves, need):
            if any(x not in choice for x in must):
                continue
            records = []
            for other in choice:
                record = add(cell, other)
                if record is None:
                    break
                records.append(record)
            else:
                yield from place(index + 1)
            for record in reversed(records):
                undo(record)

    def trace():
        """The tour from the top left corner, first to the smaller of its neighbours."""
        start = (0, 0)
        prev, cur = start, min(links[start])
        path = [start]
        while cur != start:
            path.append(cur)
            a, b = links[cur]
            prev, cur = cur, (b if a == prev else a)
        return path + [start]

    yield from place(0)


def subsets(items, k):
    if k == 0:
        yield []
        return
    for i in range(len(items)):
        for rest in subsets(items[i + 1:], k - 1):
            yield [items[i]] + rest


def strip(m):
    """The closed tour of the 4 x m board used by the solutions."""
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


def build(base, bn, bm, n, m):
    """The moves of the n x m board the solutions build from a base tour."""
    edges = set()

    def mark(a, b):
        edges.add(frozenset((a, b)))

    def erase(a, b):
        edges.discard(frozenset((a, b)))

    def draw(path, dr, dc, swap):
        cells = [((c, r) if swap else (r, c)) for r, c in path]
        for (r1, c1), (r2, c2) in zip(cells, cells[1:]):
            mark((r1 + dr, c1 + dc), (r2 + dr, c2 + dc))

    draw(base, 0, 0, False)
    for cur in range(bm, m, BLOCK):
        draw(strip(bn), 0, cur, True)
        erase((0, cur - 1), (1, cur - 1))
        erase((0, cur), (1, cur))
        erase((2, cur), (1, cur + 1))
        mark((0, cur - 1), (1, cur))
        mark((1, cur - 1), (2, cur))
        mark((0, cur), (1, cur + 1))
    for cur in range(bn, n, BLOCK):
        draw(strip(m), cur, 0, False)
        erase((cur - 1, 0), (cur - 1, 1))
        erase((cur, 0), (cur, 1))
        erase((cur, 2), (cur + 1, 1))
        mark((cur - 1, 0), (cur, 1))
        mark((cur - 1, 1), (cur, 2))
        mark((cur, 0), (cur + 1, 1))
    return edges


def valid(edges, n, m):
    links = {(r, c): [] for r in range(n) for c in range(m)}
    squares = set()
    for e in edges:
        a, b = tuple(e)
        if a not in links or b not in links:
            return False
        links[a].append(b)
        links[b].append(a)
        sq = square(a, b)
        if sq is not None:
            if sq in squares:
                return False
            squares.add(sq)
    for cell, nb in links.items():
        if len(nb) != 2:
            return False
        (r1, c1), (r2, c2) = nb
        if r1 + r2 == 2 * cell[0] and c1 + c2 == 2 * cell[1]:
            return False
    seen = {(0, 0)}
    prev, cur = (0, 0), links[(0, 0)][0]
    while cur != (0, 0):
        seen.add(cur)
        a, b = links[cur]
        prev, cur = cur, (b if a == prev else a)
    return len(seen) == n * m


def usable(tour, n, m):
    edges = {frozenset(p) for p in zip(tour, tour[1:])}
    if frozenset(((0, m - 1), (1, m - 1))) not in edges:
        return False
    if frozenset(((n - 1, 0), (n - 1, 1))) not in edges:
        return False
    flipped = [(c, r) for r, c in tour]
    for base, bn, bm in ((tour, n, m), (flipped, m, n)):
        for extra_rows in GROWTH:
            for extra_cols in GROWTH:
                rows, cols = bn + extra_rows, bm + extra_cols
                if not valid(build(base, bn, bm, rows, cols), rows, cols):
                    return False
    return True


def main():
    sys.setrecursionlimit(10000)
    for n, m in BASES:
        for tour in tours(n, m):
            if usable(tour, n, m):
                print(n, m, " ".join("%d %d" % cell for cell in tour), flush=True)
                break


main()
