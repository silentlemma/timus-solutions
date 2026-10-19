"""Match all nine rotated input photographs to distinct 4x4 crops of the answer."""
from pathlib import Path
import sys


PIECE_SIDE = 4
GRID_SIDE = 3
PIECE_COUNT = GRID_SIDE * GRID_SIDE
STRIDE = PIECE_SIDE - 1
BOARD_SIDE = GRID_SIDE * STRIDE + 1
MAX_COLOR = 99
TURN_COUNT = 4


def rotations(piece):
    result = set()
    current = [list(row) for row in piece]
    for _ in range(TURN_COUNT):
        result.add(tuple(map(tuple, current)))
        current = [[current[PIECE_SIDE - 1 - c][r] for c in range(PIECE_SIDE)]
                   for r in range(PIECE_SIDE)]
    return result


def check(pieces, text):
    try:
        board = [list(map(int, line.split())) for line in text.splitlines()]
    except ValueError:
        return False
    if len(board) != BOARD_SIDE or any(len(row) != BOARD_SIDE for row in board):
        return False
    if any(not 0 <= value <= MAX_COLOR for row in board for value in row):
        return False
    choices = [rotations(piece) for piece in pieces]
    allowed = []
    for top in range(0, BOARD_SIDE - PIECE_SIDE + 1, STRIDE):
        for left in range(0, BOARD_SIDE - PIECE_SIDE + 1, STRIDE):
            crop = tuple(tuple(board[top + r][left:left + PIECE_SIDE])
                         for r in range(PIECE_SIDE))
            allowed.append([i for i, variants in enumerate(choices) if crop in variants])
    matched = [-1] * PIECE_COUNT

    def augment(slot, seen):
        for photo in allowed[slot]:
            if photo in seen:
                continue
            seen.add(photo)
            if matched[photo] < 0 or augment(matched[photo], seen):
                matched[photo] = slot
                return True
        return False

    return all(augment(slot, set()) for slot in range(PIECE_COUNT))


def main():
    values = list(map(int, Path(sys.argv[1]).read_text().split()))
    pixels = PIECE_SIDE * PIECE_SIDE
    pieces = [[[values[i * pixels + r * PIECE_SIDE + c] for c in range(PIECE_SIDE)]
               for r in range(PIECE_SIDE)] for i in range(PIECE_COUNT)]
    if not check(pieces, Path(sys.argv[3]).read_text()):
        print('Expected a 10x10 pattern using each rotated photograph once')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
