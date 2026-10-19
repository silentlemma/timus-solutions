import sys

SIDE = 5
PORT_COUNT = 4
MIN_TILES = 3
TOP, RIGHT, BOTTOM, LEFT = range(PORT_COUNT)
ROW_STEP = (-1, 0, 1, 0)
COLUMN_STEP = (0, 1, 0, -1)
OPPOSITE = (BOTTOM, LEFT, TOP, RIGHT)
CONNECTIONS = {
    "/": (LEFT, BOTTOM, RIGHT, TOP),
    "\\": (RIGHT, TOP, LEFT, BOTTOM),
}
MOTIONS = (("L", 0, 1), ("R", 0, -1), ("U", 1, 0), ("D", -1, 0))


def winning(board):
    for side in range(PORT_COUNT):
        for offset in range(SIDE):
            if side == TOP:
                row, column = 0, offset
            elif side == RIGHT:
                row, column = offset, SIDE - 1
            elif side == BOTTOM:
                row, column = SIDE - 1, offset
            else:
                row, column = offset, 0
            incoming = side
            visited = set()
            tiles = 0
            while True:
                index = row * SIDE + column
                tile = board[index]
                state = index, incoming
                if tile == "*" or state in visited:
                    break
                visited.add(state)
                tiles |= 1 << index
                outgoing = CONNECTIONS[tile][incoming]
                row += ROW_STEP[outgoing]
                column += COLUMN_STEP[outgoing]
                if not (0 <= row < SIDE and 0 <= column < SIDE):
                    if outgoing != side and tiles.bit_count() >= MIN_TILES:
                        return True
                    break
                incoming = OPPOSITE[outgoing]
    return False


def shifted(board, row_step, column_step, amount):
    hole = board.index("*")
    row, column = divmod(hole, SIDE)
    if not (
        0 <= row + row_step * amount < SIDE
        and 0 <= column + column_step * amount < SIDE
    ):
        return None
    changed = list(board)
    for _ in range(amount):
        row += row_step
        column += column_step
        following = row * SIDE + column
        changed[hole] = changed[following]
        changed[following] = "*"
        hole = following
    return changed


def solve(board):
    if winning(board):
        return "WIN"
    # The hole travels opposite to the indicated tile motion.
    for direction, row_step, column_step in MOTIONS:
        for amount in range(1, SIDE):
            changed = shifted(board, row_step, column_step, amount)
            if changed is not None and winning(changed):
                return direction + str(amount)
    return "FAIL"


if __name__ == "__main__":
    print(solve("".join(sys.stdin.read().split())))
