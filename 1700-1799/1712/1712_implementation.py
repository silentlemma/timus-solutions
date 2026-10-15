import sys

SIZE = 4


def main():
    rows = sys.stdin.read().split()
    grille, square = rows[:SIZE], rows[SIZE:2 * SIZE]
    password = []
    # read the windows row by row, then turn the grille clockwise:
    # the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
    for _ in range(SIZE):
        for r in range(SIZE):
            for c in range(SIZE):
                if grille[r][c] == "X":
                    password.append(square[r][c])
        grille = ["".join(grille[SIZE - 1 - c][r] for c in range(SIZE)) for r in range(SIZE)]
    print("".join(password))


main()
