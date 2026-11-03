import sys

SIZE = 4
PATTERN = 3
CELLS = SIZE * SIZE
ALL = (1 << CELLS) - 1
HALF = CELLS // 2


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
    # Moves commute, so split their set in half and match the two XOR effects.
    # Duplicate left effects need only their cheapest number of moves.
    left = {}
    effect = 0
    for step in range(1 << HALF):
        if step:
            effect ^= moves[(step & -step).bit_length() - 1]
        count = (step ^ (step >> 1)).bit_count()
        left[effect] = min(left.get(effect, CELLS + 1), count)
    best, effect = CELLS + 1, 0
    for step in range(1 << HALF):
        if step:
            effect ^= moves[HALF + (step & -step).bit_length() - 1]
        count = (step ^ (step >> 1)).bit_count()
        for target in (board ^ effect, board ^ ALL ^ effect):
            if target in left:
                best = min(best, count + left[target])
    print("Impossible" if best > CELLS else best)


main()
