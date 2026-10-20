"""python gen.py MODE SEED; modes 1..9 have one unique optimal output string."""

import random
import sys

MAX_CELLS = 100_000
MAX_LENGTH = 100_000
MAX_VALUE = 1_000_000_000
SMALL_SIDE = 5
SMALL_LENGTH = 10
MEDIUM_SIDE = 10
MEDIUM_LENGTH = 24
RECTANGLE_ROWS = 250
EXCURSION_LENGTH = 40_000
MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_ROW = 3
MODE_COLUMN = 4
MODE_TWO_ROWS = 5
MODE_RECTANGLE = 6
MODE_LOOPS = 7
MODE_EXCURSION = 8
MODE_IDENTICAL = 9
STEPS = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}


def unique_optimum(board, program):
    n, m = len(board), len(board[0])
    candidates = set()
    for i, command in enumerate(program):
        remaining = program[:i] + program[i + 1 :]
        for j in range(len(program)):
            candidates.add(remaining[:j] + command + remaining[j:])
    best = None
    count = 0
    for candidate in sorted(candidates):
        x = y = 0
        score = board[0][0]
        for command in candidate:
            dx, dy = STEPS[command]
            x += dx
            y += dy
            if 0 <= x < n and 0 <= y < m:
                score += board[x][y]
        if best is None or score < best:
            best, count = score, 1
        elif score == best:
            count += 1
    return count == 1


def generate(mode, seed):
    rng = random.Random(seed)
    if mode in (MODE_SMALL, MODE_MEDIUM):
        side = SMALL_SIDE if mode == MODE_SMALL else MEDIUM_SIDE
        length_limit = SMALL_LENGTH if mode == MODE_SMALL else MEDIUM_LENGTH
        while True:
            n, m = rng.randint(1, side), rng.randint(1, side)
            board = [[rng.randint(-MAX_VALUE, MAX_VALUE) for _ in range(m)] for _ in range(n)]
            length = rng.randint(2, length_limit)
            program = "".join(rng.choice(tuple(STEPS)) for _ in range(length))
            if unique_optimum(board, program):
                return board, program

    if not MODE_ROW <= mode <= MODE_IDENTICAL:
        raise ValueError("mode must be between 1 and 9")
    if mode == MODE_COLUMN:
        n, m = MAX_CELLS, 1
    elif mode in (MODE_TWO_ROWS, MODE_LOOPS):
        n, m = 2, MAX_CELLS // 2
    elif mode == MODE_RECTANGLE:
        n, m = RECTANGLE_ROWS, MAX_CELLS // RECTANGLE_ROWS
    elif mode == MODE_IDENTICAL:
        n = m = 1
    else:
        n, m = 1, MAX_CELLS
    board = [[rng.randint(1, MAX_VALUE) for _ in range(m)] for _ in range(n)]
    if mode in (MODE_TWO_ROWS, MODE_RECTANGLE, MODE_LOOPS):
        board[1] = [-rng.randint(1, MAX_VALUE) for _ in range(m)]
    program = "R" * (MAX_LENGTH - 1) + "D"
    if mode == MODE_COLUMN:
        program = "D" * (MAX_LENGTH - 1) + "R"
    elif mode == MODE_LOOPS:
        program = "RL" * ((MAX_LENGTH - 2) // 2) + "RD"
    elif mode == MODE_EXCURSION:
        program = (
            "R" * EXCURSION_LENGTH
            + "L" * EXCURSION_LENGTH
            + "R" * (MAX_LENGTH - 2 * EXCURSION_LENGTH - 1)
            + "D"
        )
    elif mode == MODE_IDENTICAL:
        board[0][0] = rng.choice((-MAX_VALUE, MAX_VALUE, 0))
        program = rng.choice(tuple(STEPS)) * MAX_LENGTH
    # In mixed-command large cases, moving the last command to the front is unique.
    # Later insertion visits positive cells instead of zero or negative cells.
    return board, program


def main():
    mode, seed = map(int, sys.argv[1:])
    board, program = generate(mode, seed)
    print(len(board), len(board[0]))
    for row in board:
        print(*row)
    print(program)


if __name__ == "__main__":
    main()
