import sys

ROWS = 7
COLUMNS = 9
CONNECT = 4
MAX_MOVES = ROWS * COLUMNS
FIRST_WIN = 2 * (CONNECT - 1)
DIRECTIONS = ((1, 0), (0, 1), (1, 1), (-1, 1))


def main():
    moves = [digit - ord("1") for digit in sys.stdin.buffer.read().strip()]
    lines = []
    for row_step, column_step in DIRECTIONS:
        shift = column_step * ROWS + row_step
        mask = 0
        for column in range(COLUMNS):
            for row in range(ROWS):
                end_row = row + (CONNECT - 1) * row_step
                end_column = column + (CONNECT - 1) * column_step
                if 0 <= end_row < ROWS and end_column < COLUMNS:
                    mask |= 1 << (column * ROWS + row)
        lines.append((shift, 2 * shift, mask))

    wins = 0
    draws = 0
    size = len(moves)
    for start in range(size):
        heights = [0] * COLUMNS
        boards = [0, 0]
        placed = 0
        for turn in range(min(MAX_MOVES, size - start)):
            column = moves[start + turn]
            row = heights[column]
            if row == ROWS:
                continue
            player = turn % 2
            board = boards[player] | (1 << (column * ROWS + row))
            boards[player] = board
            heights[column] = row + 1
            placed += 1
            if turn >= FIRST_WIN:
                for shift, double_shift, mask in lines:
                    pairs = board & (board >> shift)
                    # Masks prevent a shifted run from crossing a column boundary.
                    if pairs & (pairs >> double_shift) & mask:
                        wins += 1
                        break
                else:
                    if placed == MAX_MOVES:
                        draws += 1
                    continue
                break

    print(wins, draws)


if __name__ == "__main__":
    main()
