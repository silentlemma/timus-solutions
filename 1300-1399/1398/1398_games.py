import sys
from functools import lru_cache

BLACK, DRAW, WHITE = 0, 1, 2  # results, better for white upwards
SIZE = 8
SECOND = 6  # the black pawn may move two squares from rank 7
DIAGONALS = ((1, 1), (1, -1), (-1, 1), (-1, -1))


def sees(bf, br, qf, qr):
    """Can the bishop reach square (qf, qr) on an otherwise empty board?"""
    for df, dr in DIAGONALS:
        f, r = bf + df, br + dr
        while 0 <= f < SIZE and 0 <= r < SIZE:
            if (f, r) == (qf, qr):
                return True
            f, r = f + df, r + dr
    return False


@lru_cache(maxsize=None)
def white(bf, br, pf, pr):
    best = BLACK
    for df, dr in DIAGONALS:
        f, r = bf + df, br + dr
        while 0 <= f < SIZE and 0 <= r < SIZE:
            if (f, r) == (pf, pr):
                return WHITE  # the bishop takes the pawn
            best = max(best, black(f, r, pf, pr))
            f, r = f + df, r + dr
    return best


@lru_cache(maxsize=None)
def black(bf, br, pf, pr):
    results = []
    if (bf, br) in ((pf - 1, pr - 1), (pf + 1, pr - 1)):
        results.append(BLACK)  # the pawn takes the bishop and cannot be stopped
    if (bf, br) != (pf, pr - 1):
        if pr - 1 == 0:
            # a queen: white wins only by taking it at once
            results.append(WHITE if sees(bf, br, pf, 0) else BLACK)
        else:
            results.append(white(bf, br, pf, pr - 1))
            if pr == SECOND and (bf, br) != (pf, pr - 2):
                results.append(white(bf, br, pf, pr - 2))
    return min(results) if results else DRAW  # a blocked pawn is a draw


def main():
    bishop, pawn = sys.stdin.read().split()[:2]
    bf, br = ord(bishop[0]) - ord("a"), int(bishop[1]) - 1
    pf, pr = ord(pawn[0]) - ord("a"), int(pawn[1]) - 1
    print(("BLACK", "DRAW", "WHITE")[white(bf, br, pf, pr)])


main()
