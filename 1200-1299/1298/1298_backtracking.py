import sys

MOVES = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))


def main():
    n = int(sys.stdin.read().split()[0])
    seen = [[False] * n for _ in range(n)]
    path = []

    def free(c, r):
        return [
            (c + dc, r + dr)
            for dc, dr in MOVES
            if 0 <= c + dc < n and 0 <= r + dr < n and not seen[c + dc][r + dr]
        ]

    def tour(c, r):
        seen[c][r] = True
        path.append((c, r))
        if len(path) == n * n:
            return True
        # Warnsdorff's rule: try first the squares with the fewest onward
        # moves, and the search still backtracks, so it is exact
        for nc, nr in sorted(free(c, r), key=lambda sq: len(free(*sq))):
            if tour(nc, nr):
                return True
        seen[c][r] = False
        path.pop()
        return False

    if any(tour(c, r) for c in range(n) for r in range(n)):
        sys.stdout.write("".join("%s%d\n" % (chr(ord("a") + c), r + 1) for c, r in path))
    else:
        print("IMPOSSIBLE")


main()
