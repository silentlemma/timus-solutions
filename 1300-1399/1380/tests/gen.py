"""A chess record: a seed and a mode. Mode 1 plays a random legal game of
up to 60 moves from the starting position, mode 2 does the same but slips
in one move from a square without a piece of the side to move, mode 3
starts from a random position with two kings on each side."""

import random
import sys

SIZE = 8
MOVES = 60
PIECES = 12  # pieces besides the kings in mode 3
START = [
    [-4, -2, -3, -5, -6, -3, -2, -4],
    [-1] * SIZE,
    [0] * SIZE,
    [0] * SIZE,
    [0] * SIZE,
    [0] * SIZE,
    [1] * SIZE,
    [4, 2, 3, 5, 6, 3, 2, 4],
]
KNIGHT = {(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)}


def reaches(board, f, r, tf, tr):
    """Can the piece on (f, r) go to (tf, tr), checks aside?"""
    piece, target = board[r][f], board[tr][tf]
    side, kind = (1 if piece > 0 else -1), abs(piece)
    df, dr = tf - f, tr - r
    if (df, dr) == (0, 0) or target * side > 0:
        return False
    if kind == 1:
        home = 1 if side > 0 else SIZE - 2
        if df == 0 and target == 0:
            return dr == side or (dr == 2 * side and r == home and board[r + side][f] == 0)
        return abs(df) == 1 and dr == side and target * side < 0
    if kind == 2:
        return (df, dr) in KNIGHT
    if kind == 6:
        return max(abs(df), abs(dr)) == 1
    straight, diagonal = df == 0 or dr == 0, abs(df) == abs(dr)
    if not (
        (kind == 3 and diagonal)
        or (kind == 4 and straight)
        or (kind == 5 and (straight or diagonal))
    ):
        return False
    sf, sr = (df > 0) - (df < 0), (dr > 0) - (dr < 0)
    f, r = f + sf, r + sr
    while (f, r) != (tf, tr):
        if board[r][f]:
            return False
        f, r = f + sf, r + sr
    return True


def attacked(board, side):
    kings = [(f, r) for r in range(SIZE) for f in range(SIZE) if board[r][f] == 6 * side]
    return any(
        board[r][f] * side < 0 and reaches(board, f, r, kf, kr)
        for r in range(SIZE)
        for f in range(SIZE)
        for kf, kr in kings
    )


def moves(board, side):
    out = []
    for r in range(SIZE):
        for f in range(SIZE):
            if board[r][f] * side <= 0:
                continue
            for tr in range(SIZE):
                for tf in range(SIZE):
                    if reaches(board, f, r, tf, tr):
                        taken, board[tr][tf], board[r][f] = board[tr][tf], board[r][f], 0
                        if not attacked(board, side):
                            out.append((f, r, tf, tr))
                        board[r][f], board[tr][tf] = board[tr][tf], taken
    return out


def square(f, r):
    return "abcdefgh"[f] + str(r + 1)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    rows = [row[:] for row in START]
    while True:
        if mode == 3:
            rows = [[0] * SIZE for _ in range(SIZE)]
            extra = [rng.choice([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) for _ in range(PIECES)]
            for piece in [6, 6, -6, -6] + extra:
                rows[rng.randrange(SIZE)][rng.randrange(SIZE)] = piece
        board = [rows[SIZE - 1 - r][:] for r in range(SIZE)]  # row r is rank r + 1
        if moves(board, 1):  # the record needs at least one move
            break
    side, record = 1, []
    bad_at = rng.randrange(MOVES // 2) if mode == 2 else -1
    for i in range(MOVES):
        if i == bad_at:
            # a move from a square without a piece of the side to move
            other = [(f, r) for r in range(SIZE) for f in range(SIZE) if board[r][f] * side <= 0]
            f, r = rng.choice(other)
            record.append(square(f, r) + "-" + square(rng.randrange(SIZE), rng.randrange(SIZE)))
            break
        options = moves(board, side)
        if not options:
            break
        f, r, tf, tr = rng.choice(options)
        board[tr][tf], board[r][f] = board[r][f], 0
        record.append(square(f, r) + "-" + square(tf, tr))
        side = -side
    for row in rows:
        print(*row)
    print(len(record))
    print("White")
    print("\n".join(record))


main()
