from sys import stdin

SIDE = 4
CELLS = SIDE * SIDE
HALF = CELLS // 2
STEPS = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))


def minimum_moves(moves):
    effects = [0]
    for move in moves:
        effects += [effect ^ move for effect in effects]
    minimum = {}
    for subset, effect in enumerate(effects):
        count = subset.bit_count()
        if count < minimum.get(effect, CELLS + 1):
            minimum[effect] = count
    return minimum


board = 0
moves = []
for row, cells in enumerate(stdin.read().split()):
    for column, color in enumerate(cells):
        if color == "b":
            board |= 1 << (SIDE * row + column)
        move = 0
        for dr, dc in STEPS:
            r, c = row + dr, column + dc
            if 0 <= r < SIDE and 0 <= c < SIDE:
                move |= 1 << (SIDE * r + c)
        moves.append(move)

left = minimum_moves(moves[:HALF])
right = minimum_moves(moves[HALF:])
best = CELLS + 1
for target in (board, board ^ ((1 << CELLS) - 1)):
    # The required XOR of the right half is determined by the left half.
    for effect, count in left.items():
        other = right.get(effect ^ target)
        if other is not None:
            best = min(best, count + other)
print("Impossible" if best > CELLS else best)
