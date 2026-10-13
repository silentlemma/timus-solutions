import sys

SIZE = 8
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6
TO_FILE = 3  # a move reads like e2-e4
TO_RANK = 4
KNIGHT_STEPS = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
STRAIGHT = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIAGONAL = ((1, 1), (1, -1), (-1, 1), (-1, -1))
HOME = {1: 1, -1: SIZE - 2}  # the rank a pawn may step two squares from


def inside(f, r):
    return 0 <= f < SIZE and 0 <= r < SIZE


def reaches(board, f, r, tf, tr):
    """Can the piece on (f, r) move to (tf, tr), ignoring checks?"""
    piece = board[r][f]
    side, kind = (1 if piece > 0 else -1), abs(piece)
    target = board[tr][tf]
    if (f, r) == (tf, tr) or target * side > 0:
        return False
    df, dr = tf - f, tr - r
    if kind == PAWN:
        if df == 0 and target == 0:
            if dr == side:
                return True
            return dr == 2 * side and r == HOME[side] and board[r + side][f] == 0
        return abs(df) == 1 and dr == side and target * side < 0
    if kind == KNIGHT:
        return (df, dr) in KNIGHT_STEPS
    if kind == KING:
        return max(abs(df), abs(dr)) == 1
    lines = {BISHOP: DIAGONAL, ROOK: STRAIGHT, QUEEN: DIAGONAL + STRAIGHT}[kind]
    sf, sr = (df > 0) - (df < 0), (dr > 0) - (dr < 0)
    if (sf, sr) not in lines or (df and dr and abs(df) != abs(dr)):
        return False
    f, r = f + sf, r + sr
    while (f, r) != (tf, tr):
        if board[r][f]:
            return False
        f, r = f + sf, r + sr
    return True


def in_check(board, side):
    """Is any king of this side attacked?"""
    kings = [(f, r) for r in range(SIZE) for f in range(SIZE) if board[r][f] == KING * side]
    for r in range(SIZE):
        for f in range(SIZE):
            if board[r][f] * side < 0:
                for kf, kr in kings:
                    if reaches(board, f, r, kf, kr):
                        return True
    return False


def legal(board, side, f, r, tf, tr):
    """Move if it is legal and return the taken piece, or None."""
    if not (inside(f, r) and inside(tf, tr)) or board[r][f] * side <= 0:
        return None
    if not reaches(board, f, r, tf, tr):
        return None
    taken, board[tr][tf], board[r][f] = board[tr][tf], board[r][f], 0
    if in_check(board, side):
        board[r][f], board[tr][tf] = board[tr][tf], taken
        return None
    return taken


def has_move(board, side):
    for r in range(SIZE):
        for f in range(SIZE):
            if board[r][f] * side > 0:
                for tr in range(SIZE):
                    for tf in range(SIZE):
                        taken = legal(board, side, f, r, tf, tr)
                        if taken is not None:
                            board[r][f], board[tr][tf] = board[tr][tf], taken
                            return True
    return False


def main():
    words = sys.stdin.read().split()
    # row r is rank r + 1, so the first input line is row 7
    board = [[int(words[(SIZE - 1 - r) * SIZE + f]) for f in range(SIZE)] for r in range(SIZE)]
    count = int(words[SIZE * SIZE])
    side = 1 if words[SIZE * SIZE + 1] == "White" else -1
    out = []
    for move in words[SIZE * SIZE + 2 : SIZE * SIZE + 2 + count]:
        f, r = ord(move[0]) - ord("a"), int(move[1]) - 1
        tf, tr = ord(move[TO_FILE]) - ord("a"), int(move[TO_RANK]) - 1
        if legal(board, side, f, r, tf, tr) is None:
            out.append("Incorrect")
            break
        side = -side
        check, free = in_check(board, side), has_move(board, side)
        out.append(("Mate" if check else "Draw") if not free else ("Check" if check else "Correct"))
        if not free:
            break
    out.append("")
    out += [" ".join(map(str, board[r])) for r in range(SIZE - 1, -1, -1)]
    print("\n".join(out))


main()
