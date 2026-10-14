"""Checker: the expected number k of tiles, then n rows of m characters 0
and 1 where the 1 cells can be covered by k tiles and the 0 cells have
exactly one tiling."""

import sys

NEAR = ((0, 1), (1, 0), (0, -1), (-1, 0))


def fail(reason):
    print(reason)
    sys.exit(1)


def neighbours(cells, n, m):
    out = {}
    for r, c in cells:
        out[r, c] = [(r + dr, c + dc) for dr, dc in NEAR if (r + dr, c + dc) in cells]
    return out


def tileable(cells, n, m):
    """A perfect matching of the cells exists (augmenting paths)."""
    near = neighbours(cells, n, m)
    mate = {}

    def augment(u, seen):
        for v in near[u]:
            if v not in seen:
                seen.add(v)
                if v not in mate or augment(mate[v], seen):
                    mate[v] = u
                    return True
        return False

    black = [u for u in cells if (u[0] + u[1]) % 2 == 0]
    return 2 * len(black) == len(cells) and all(augment(u, set()) for u in black)


def unique(cells, n, m):
    """Exactly one tiling: matching forced cells must use up every cell."""
    near = neighbours(cells, n, m)
    free = set(cells)
    while free:
        forced = next((u for u in free if sum(v in free for v in near[u]) <= 1), None)
        if forced is None:
            return False
        partner = [v for v in near[forced] if v in free]
        if not partner:
            return False
        free -= {forced, partner[0]}
    return True


def main():
    source, expected, output = sys.argv[1:4]
    n, m = (int(x) for x in open(source).read().split())
    want = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if not got or not got[0].isdigit() or int(got[0]) != want:
        fail("expected %d tiles" % want)
    rows = got[1:]
    if len(rows) != n or any(len(row) != m or set(row) - set("01") for row in rows):
        fail("expected %d rows of %d characters 0 and 1" % (n, m))
    ones = {(r, c) for r in range(n) for c in range(m) if rows[r][c] == "1"}
    zeros = {(r, c) for r in range(n) for c in range(m)} - ones
    if len(ones) != 2 * want or not tileable(ones, n, m):
        fail("the marked cells are not %d tiles" % want)
    if not unique(zeros, n, m):
        fail("the rest of the board does not have exactly one tiling")


main()
