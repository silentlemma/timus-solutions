import sys

SIZE = 8
DIAGONALS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def can_capture(board):
    """Some checker has a checker of the other color next to it on a
    diagonal and a free square right behind that one."""
    for (c, r), color in board.items():
        for dc, dr in DIAGONALS:
            over, land = (c + dc, r + dr), (c + 2 * dc, r + 2 * dr)
            inside = 0 <= land[0] < SIZE and 0 <= land[1] < SIZE
            if inside and board.get(over, color) != color and land not in board:
                return True
    return False


def main():
    moves = sys.stdin.read().split()
    board = {}
    for number, move in enumerate(moves, 1):
        square = (ord(move[0].lower()) - ord("a"), int(move[1:]) - 1)
        board[square] = number % 2  # white moves on the odd lines
        if can_capture(board):
            print(number)
            return
    print("Draw")


main()
