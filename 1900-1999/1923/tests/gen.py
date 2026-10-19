"""Arguments: seed mode. Modes 1..9 emit valid maps and 100 alternating moves."""

import random
import sys

SIDE = 50
MOVES = 100
COLORS = 10


def generate(seed, mode):
    rng = random.Random(seed)
    rows, columns = (2, SIDE) if mode == 8 else (SIDE, 2) if mode == 9 else (SIDE, SIDE)
    board = []
    for row in range(rows):
        line = []
        for column in range(columns):
            if mode == 2:
                color = column % COLORS
            elif mode == 3:
                color = row % COLORS
            elif mode == 4:
                color = 0
            elif mode == 5:
                color = int(column >= columns // 2)
            elif mode == 6:
                color = (row + column) % COLORS
            elif mode == 7:
                color = (row // 2 + column // 3) % COLORS
            else:
                color = rng.randrange(COLORS)
            line.append(str(color))
        board.append("".join(line))
    if board[-1][0] == board[0][-1]:
        board[0] = board[0][:-1] + str((int(board[-1][0]) + 1) % COLORS)
    alliances = [int(board[-1][0]), int(board[0][-1])]
    moves = []
    for turn in range(MOVES):
        color = rng.choice([value for value in range(COLORS) if value not in alliances])
        alliances[turn % 2] = color
        moves.append(color)
    return board, moves


def render(board, moves):
    return (
        f"{len(board)} {len(board[0])}\n"
        + "\n".join(board)
        + f"\n{len(moves)}\n"
        + " ".join(map(str, moves))
        + "\n"
    )


if __name__ == "__main__":
    print(render(*generate(int(sys.argv[1]), int(sys.argv[2]))), end="")
