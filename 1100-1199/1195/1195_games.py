import sys

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
# outcomes for crosses: win, draw, loss
WIN, DRAW, LOSS = 1, 0, -1


def won(board, mark):
    return any(all(board[i] == mark for i in line) for line in LINES)


def play(board, mark, other):
    # the best outcome for the side about to move with mark
    free = [i for i in range(len(board)) if board[i] == "#"]
    if not free:
        return DRAW
    best = LOSS
    for i in free:
        board[i] = mark
        result = WIN if won(board, mark) else -play(board, other, mark)
        board[i] = "#"
        best = max(best, result)
    return best


def main():
    board = list("".join(sys.stdin.read().split()))
    # three moves each have been made, so crosses move now
    result = play(board, "X", "O")
    print({WIN: "Crosses win", DRAW: "Draw", LOSS: "Ouths win"}[result])


main()
