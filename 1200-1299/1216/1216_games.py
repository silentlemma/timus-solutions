import sys

NONE, PAWN, QUEEN, ROOK, BISHOP, KNIGHT = range(len("-PQRBN"))
PROMOTIONS = (QUEEN, ROOK, BISHOP, KNIGHT)
STRAIGHT = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIAGONAL = ((1, 1), (1, -1), (-1, 1), (-1, -1))
KING = STRAIGHT + DIAGONAL
JUMPS = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
RAYS = {QUEEN: KING, ROOK: STRAIGHT, BISHOP: DIAGONAL}
# the double steps start from these rows, counted from 0
WHITE_START = 1
EN_PASSANT_ROW = 3
# the search goes two plies deeper per row the white pawn climbs
DEPTH = 10000


def solve(n, white, black, king):
    memo = {}

    def inside(x, y):
        return 0 <= x < n and 0 <= y < n

    def piece_moves(kind, bx, by, kx, ky):
        """Squares the black piece can reach, ignoring the white pawn."""
        if kind == KNIGHT:
            for dx, dy in JUMPS:
                x, y = bx + dx, by + dy
                if inside(x, y) and (x, y) != (kx, ky):
                    yield x, y
            return
        for dx, dy in RAYS[kind]:
            x, y = bx + dx, by + dy
            while inside(x, y) and (x, y) != (kx, ky):
                yield x, y
                x, y = x + dx, y + dy

    def black_fails(wx, wy, kind, bx, by, kx, ky):
        """White to win against every reply, black to move."""
        if max(abs(kx - wx), abs(ky - wy)) == 1:
            return False  # the king takes the pawn
        if kind == PAWN and by - 1 == wy and abs(bx - wx) == 1:
            return False
        if kind not in (NONE, PAWN):
            for x, y in piece_moves(kind, bx, by, kx, ky):
                if (x, y) == (wx, wy):
                    return False
        moves = []
        for dx, dy in KING:
            x, y = kx + dx, ky + dy
            # the pawn attacks the two squares diagonally in front of it
            attacked = y == wy + 1 and abs(x - wx) == 1
            if inside(x, y) and not attacked and (kind == NONE or (x, y) != (bx, by)):
                moves.append((kind, bx, by, x, y))
        if kind == PAWN:
            ahead = by - 1
            if ahead >= 0 and (bx, ahead) not in ((wx, wy), (kx, ky)):
                if ahead == 0:
                    moves += [(p, bx, ahead, kx, ky) for p in PROMOTIONS]
                else:
                    moves.append((PAWN, bx, ahead, kx, ky))
                    two = by - 2
                    if by == n - 2 and (bx, two) not in ((wx, wy), (kx, ky)):
                        moves.append((PAWN, bx, two, kx, ky))
        elif kind != NONE:
            moves += [(kind, x, y, kx, ky) for x, y in piece_moves(kind, bx, by, kx, ky)]
        if not moves:
            return False  # nothing to move: the pawn has not promoted
        return all(white_wins(wx, wy, *m) for m in moves)

    def white_wins(wx, wy, kind, bx, by, kx, ky):
        key = (wx, wy, kind, bx, by, kx, ky)
        if key in memo:
            return memo[key]
        memo[key] = result = False
        blocker = (bx, by) if kind != NONE else None

        def free(x, y):
            return (x, y) != (kx, ky) and (x, y) != blocker

        options = []
        if free(wx, wy + 1):
            options.append((wx, wy + 1, kind, bx, by))
            if wy == WHITE_START and free(wx, wy + 2):
                # a black pawn beside the landing square takes it en passant
                beside = kind == PAWN and by == EN_PASSANT_ROW and abs(bx - wx) == 1
                if not beside:
                    options.append((wx, wy + 2, kind, bx, by))
        for dx in (-1, 1):
            if blocker == (wx + dx, wy + 1):
                options.append((wx + dx, wy + 1, NONE, -1, -1))
        for x, y, left, lx, ly in options:
            if y == n - 1 or black_fails(x, y, left, lx, ly, kx, ky):
                result = True
                break
        memo[key] = result
        return result

    return white_wins(*white, PAWN, *black, *king)


def main():
    sys.setrecursionlimit(DEPTH)
    n, *squares = sys.stdin.read().split()
    pos = [(ord(t[0]) - ord("a"), int(t[1:]) - 1) for t in squares]
    n = int(n)
    print("WHITE WINS" if solve(n, *pos) else "BLACK WINS")


main()
