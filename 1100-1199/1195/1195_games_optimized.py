from sys import stdin, stdout

LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
WIN_MASKS = tuple(sum(1 << cell for cell in line) for line in LINES)
WIN, DRAW, LOSS = 1, 0, -1


def won(mark):
    for line in WIN_MASKS:
        if mark & line == line:
            return True
    return False


def play(current, other, free):
    if not free:
        return DRAW
    best = LOSS
    options = free
    while options:
        bit = options & -options
        moved = current | bit
        result = WIN if won(moved) else -play(other, moved, free ^ bit)
        if result == WIN:
            return WIN
        if result > best:
            best = result
        options -= bit
    return best


crosses = ouths = free = 0
for cell, mark in enumerate("".join(stdin.read().split())):
    if mark == "X":
        crosses |= 1 << cell
    elif mark == "O":
        ouths |= 1 << cell
    else:
        free |= 1 << cell
result = play(crosses, ouths, free)
stdout.write(str("Crosses win" if result == WIN else "Draw" if result == DRAW else "Ouths win"))
