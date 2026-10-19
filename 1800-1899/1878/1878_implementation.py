import sys

SIDE = 4
TURNS = 4
# quadrants (top left, top right, bottom left, bottom right) in the order a
# quarter turn moves a square through them
RING = {(0, 0): 0, (0, 1): 1, (1, 1): 2, (1, 0): 3}


def main():
    cells = list(map(int, sys.stdin.read().split()))
    # every layer holds one square of each colour, one per quadrant; the
    # cube is solved when the colour 1 squares of all layers share a quadrant
    where = [RING[(k // SIDE * 2 // SIDE, k % SIDE * 2 // SIDE)]
             for k, c in enumerate(cells) if c == 1]
    print(min(sum(min((p - t) % TURNS, (t - p) % TURNS) for p in where) for t in range(TURNS)))


main()
