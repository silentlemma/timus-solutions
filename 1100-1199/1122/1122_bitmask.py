import sys

SIZE = 4
PATTERN = 3
CELLS = SIZE * SIZE
ALL = (1 << CELLS) - 1


def main():
    lines = sys.stdin.read().split()
    board = sum(1 << (r * SIZE + c) for r in range(SIZE) for c in range(SIZE) if lines[r][c] == "B")
    pattern = lines[SIZE : SIZE + PATTERN]
    # the flips of a move in each cell, the pattern clipped at the edges
    moves = []
    for r in range(SIZE):
        for c in range(SIZE):
            mask = 0
            for dr in range(PATTERN):
                for dc in range(PATTERN):
                    rr, cc = r + dr - 1, c + dc - 1
                    if pattern[dr][dc] == "1" and 0 <= rr < SIZE and 0 <= cc < SIZE:
                        mask |= 1 << (rr * SIZE + cc)
            moves.append(mask)
    # moves commute and a second move in a cell undoes the first, so a
    # solution is a set of cells; flips[s] is the effect of the set s
    flips = [0] * (1 << CELLS)
    best = None
    for s in range(1, 1 << CELLS):
        low = (s & -s).bit_length() - 1
        flips[s] = flips[s & (s - 1)] ^ moves[low]
    for s in range(1 << CELLS):
        if flips[s] in (board, board ^ ALL):
            count = bin(s).count("1")
            if best is None or count < best:
                best = count
    print("Impossible" if best is None else best)


main()
