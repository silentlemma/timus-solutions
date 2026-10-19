"""Check the longest equal-letter segment in all four unoriented directions."""

from pathlib import Path
import sys


def feasible(rows, columns, palette, level):
    target = level - 1
    if palette == 1:
        return max(rows, columns) == target
    if target == 1:
        return palette >= min(rows, 2) * min(columns, 2)
    return max(rows, columns) >= target


def longest_run(board):
    rows, columns = len(board), len(board[0])
    maximum = 0
    for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
        lengths = [[0] * columns for _ in range(rows)]
        for row in range(rows):
            for column in range(columns):
                previous_row, previous_column = row - dr, column - dc
                length = 1
                if (
                    0 <= previous_row < rows
                    and 0 <= previous_column < columns
                    and board[previous_row][previous_column] == board[row][column]
                ):
                    length += lengths[previous_row][previous_column]
                lengths[row][column] = length
                maximum = max(maximum, length)
    return maximum


def check(rows, columns, palette, level, output):
    tokens = output.split()
    if tokens == ["NO"]:
        return not feasible(rows, columns, palette, level), "impossibility declaration"
    if not tokens or tokens[0] != "YES" or len(tokens) != rows + 1:
        return False, "expected YES and the specified number of rows"
    board = tokens[1:]
    if any(len(row) != columns for row in board):
        return False, "wrong row width"
    if any(
        not ("A" <= letter < chr(ord("A") + palette)) for row in board for letter in row
    ):
        return False, "letter outside the allowed alphabet"
    maximum = longest_run(board)
    return maximum == level - 1, "longest equal-letter run must be level minus one"


if __name__ == "__main__":
    arguments = list(map(int, Path(sys.argv[1]).read_text().split()))
    accepted, reason = check(*arguments, Path(sys.argv[3]).read_text())
    print(reason)
    sys.exit(0 if accepted else 1)
