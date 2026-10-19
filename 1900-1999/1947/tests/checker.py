"""Check WIN priority, any legal winning tile move, or complete one-move impossibility."""

from collections import Counter
from pathlib import Path
import re
import sys

SIDE = 5
PORT_COUNT = 4
MIN_TILES = 3
TILE_COUNT = 12
TOP, RIGHT, BOTTOM, LEFT = range(PORT_COUNT)
TILE_LINKS = {"/": ((TOP, LEFT), (RIGHT, BOTTOM)), "\\": ((TOP, RIGHT), (BOTTOM, LEFT))}
MOTION = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


def winning(board):
    parent = list(range(PORT_COUNT * SIDE * SIDE))

    def find(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def join(first, second):
        parent[find(first)] = find(second)

    for index, tile in enumerate(board):
        if tile == "*":
            continue
        for first, second in TILE_LINKS[tile]:
            join(PORT_COUNT * index + first, PORT_COUNT * index + second)
        row, column = divmod(index, SIDE)
        if column + 1 < SIDE and board[index + 1] != "*":
            join(PORT_COUNT * index + RIGHT, PORT_COUNT * (index + 1) + LEFT)
        if row + 1 < SIDE and board[index + SIDE] != "*":
            join(PORT_COUNT * index + BOTTOM, PORT_COUNT * (index + SIDE) + TOP)
    groups = {}
    for index, tile in enumerate(board):
        if tile == "*":
            continue
        row, column = divmod(index, SIDE)
        for port in range(PORT_COUNT):
            root = find(PORT_COUNT * index + port)
            cells, mask = groups.setdefault(root, (set(), 0))
            cells.add(index)
            if (
                (port == TOP and row == 0)
                or (port == RIGHT and column + 1 == SIDE)
                or (port == BOTTOM and row + 1 == SIDE)
                or (port == LEFT and column == 0)
            ):
                mask |= 1 << port
            groups[root] = cells, mask
    return any(
        len(cells) >= MIN_TILES and mask.bit_count() >= 2
        for cells, mask in groups.values()
    )


def moves(board):
    row, column = divmod(board.index("*"), SIDE)
    for direction, (dr, dc) in MOTION.items():
        for amount in range(1, SIDE):
            far_row, far_column = row - dr * amount, column - dc * amount
            if not (0 <= far_row < SIDE and 0 <= far_column < SIDE):
                continue
            changed = list(board)
            for step in range(1, amount + 1):
                source_row, source_column = row - dr * step, column - dc * step
                changed[SIDE * (source_row + dr) + source_column + dc] = board[
                    SIDE * source_row + source_column
                ]
            changed[SIDE * far_row + far_column] = "*"
            yield direction + str(amount), "".join(changed)


def valid_answers(board):
    if winning(board):
        return {"WIN"}
    answers = {command for command, changed in moves(board) if winning(changed)}
    return answers if answers else {"FAIL"}


def check(input_path, actual_path):
    rows = Path(input_path).read_text(encoding="utf-8").split()
    board = "".join(rows)
    if len(rows) != SIDE or any(len(row) != SIDE for row in rows):
        raise ValueError("invalid board dimensions")
    if Counter(board) != Counter({"/": TILE_COUNT, "\\": TILE_COUNT, "*": 1}):
        raise ValueError("invalid tile counts")
    words = Path(actual_path).read_text(encoding="utf-8").split()
    if len(words) != 1 or not re.fullmatch(r"WIN|FAIL|[LRUD][1-4]", words[0]):
        return False, "invalid output shape"
    valid = words[0] in valid_answers(board)
    return valid, "OK" if valid else "not an allowed winning result"


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise ValueError("usage: checker.py INPUT EXPECTED ACTUAL")
        accepted, reason = check(sys.argv[1], sys.argv[3])
    except (OSError, ValueError, KeyError, IndexError):
        accepted, reason = False, "invalid input or output"
    print(reason)
    sys.exit(0 if accepted else 1)
