import sys

SIZE = 4
CELLS = SIZE * SIZE
STEPS = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    rows = sys.stdin.read().split()
    # the board as 16 bits, bit r * 4 + c set for a black piece
    board = 0
    for r in range(SIZE):
        for c in range(SIZE):
            if rows[r][c] == "b":
                board |= 1 << (r * SIZE + c)
    # the pieces turned by a move at each cell
    move = []
    for r in range(SIZE):
        for c in range(SIZE):
            m = 0
            for dr, dc in STEPS:
                if 0 <= r + dr < SIZE and 0 <= c + dc < SIZE:
                    m |= 1 << ((r + dr) * SIZE + c + dc)
            move.append(m)
    # moves commute and a move made twice cancels, so a solution is a set of
    # cells; the boards reached by all 2^16 sets are built one cell at a time
    full = (1 << CELLS) - 1
    reached = [board]
    for m in move:
        reached += [b ^ m for b in reached]
    counts = [0]
    for _ in move:
        counts += [k + 1 for k in counts]
    best = min((k for b, k in zip(reached, counts) if b in (0, full)), default=None)
    print("Impossible" if best is None else best)


main()
