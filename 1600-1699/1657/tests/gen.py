"""One test from a seed and a mode: mode 1 the snake of a random folding
(a random Hamiltonian path through the cube, so it always folds), mode 2
a random snake (mostly impossible), mode 3 a folding snake with one cube
switched between straight and turning."""

import random
import sys

SIDE = 3
STEPS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def random_path(rng):
    cells = [(x, y, z) for x in range(SIDE) for y in range(SIDE) for z in range(SIDE)]
    while True:
        path = [rng.choice(cells)]
        seen = {path[0]}
        while len(path) < len(cells):
            x, y, z = path[-1]
            options = [(x + a, y + b, z + c) for a, b, c in STEPS]
            options = [p for p in options if p in cells and p not in seen]
            if not options:
                break
            nxt = rng.choice(options)
            path.append(nxt)
            seen.add(nxt)
        if len(path) == len(cells):
            return path


def snake_of(path):
    marks = ["F"]
    for k in range(1, len(path) - 1):
        before = tuple(b - a for a, b in zip(path[k - 1], path[k]))
        after = tuple(b - a for a, b in zip(path[k], path[k + 1]))
        marks.append("F" if before == after else "T")
    return "".join(marks + ["F"])


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        snake = "F" + "".join(rng.choice("FT") for _ in range(25)) + "F"
    else:
        snake = snake_of(random_path(rng))
        if mode == 3:
            k = rng.randint(1, 25)
            snake = snake[:k] + ("F" if snake[k] == "T" else "T") + snake[k + 1 :]
    print(snake)


main()
