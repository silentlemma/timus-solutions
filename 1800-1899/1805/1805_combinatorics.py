import sys

TURNS = 4


def main():
    n, k = map(int, sys.stdin.read().split())
    # the four cells a quarter turn takes into each other form an orbit; a
    # grille opens exactly one cell of every orbit
    orbit = [[-1] * n for _ in range(n)]
    orbits = 0
    for r in range(n):
        for c in range(n):
            if orbit[r][c] < 0:
                rr, cc = r, c
                for _ in range(TURNS):
                    orbit[rr][cc] = orbits
                    rr, cc = cc, n - 1 - rr
                orbits += 1
    # left[o]: cells of orbit o not passed yet, None once its window is cut
    left = [TURNS] * orbits
    rows = []
    for r in range(n):
        row = []
        for c in range(n):
            o = orbit[r][c]
            if left[o] is None:
                row.append("0")
                continue
            left[o] -= 1
            # grilles with a 0 here: every open orbit picks one of its
            # remaining cells
            with_zero = 1
            for rest in left:
                if rest is not None:
                    with_zero *= rest
            if k <= with_zero:
                row.append("0")
            else:
                k -= with_zero
                row.append("1")
                left[o] = None
        rows.append("".join(row))
    print("\n".join(rows))


main()
