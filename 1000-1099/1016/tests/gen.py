"""The cube on the board (faces in the input order near, far, top, right,
bottom, left) and a random query; a seed and the largest face value."""

import random
import sys

FACES = 6
NEAR, FAR, TOP, RIGHT, BOTTOM, LEFT = range(FACES)
SIZE = 8
# a roll towards a neighbour: the face that comes to each position
ROLLS = {
    (0, 1): {FAR: TOP, BOTTOM: FAR, NEAR: BOTTOM, TOP: NEAR},
    (0, -1): {NEAR: TOP, BOTTOM: NEAR, FAR: BOTTOM, TOP: FAR},
    (1, 0): {RIGHT: TOP, BOTTOM: RIGHT, LEFT: BOTTOM, TOP: LEFT},
    (-1, 0): {LEFT: TOP, BOTTOM: LEFT, RIGHT: BOTTOM, TOP: RIGHT},
}


def roll(faces, step):
    new = list(faces)
    for to, frm in ROLLS[step].items():
        new[to] = faces[frm]
    return tuple(new)


def cell(name):
    return ord(name[0]) - ord("a"), int(name[1:]) - 1


def name(x, y):
    return "%s%d" % (chr(ord("a") + x), y + 1)


def main():
    seed, top = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    cells = [name(x, y) for x in range(SIZE) for y in range(SIZE)]
    start, end = rng.sample(cells, 2)
    print(start, end, " ".join(str(rng.randint(0, top)) for _ in range(FACES)))


if __name__ == "__main__":
    main()
