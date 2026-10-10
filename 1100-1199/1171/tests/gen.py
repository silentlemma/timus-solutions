"""A space station: a seed, N, the chance of a door in percent and a mode.
Mode 0 gives random food from 1 to 255, mode 1 food from 1 to 3, mode 2 a
few rich rooms among poor ones. Every level above the first gets at least
one door, so a trip down always exists."""

import random
import sys

SIDE = 4
ROOMS = SIDE * SIDE
TOP = 255
PERCENT = 100
RICH = 0.1


def main():
    seed, n, chance, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [str(n)]
    for level in range(n):
        if mode == 1:
            food = [rng.randint(1, 3) for _ in range(ROOMS)]
        elif mode == 2:
            food = [rng.randint(200, TOP) if rng.random() < RICH else 1 for _ in range(ROOMS)]
        else:
            food = [rng.randint(1, TOP) for _ in range(ROOMS)]
        door = [0] * ROOMS
        if level < n - 1:
            door = [int(rng.randrange(PERCENT) < chance) for _ in range(ROOMS)]
            door[rng.randrange(ROOMS)] = 1
        for grid in (food, door):
            for r in range(SIDE):
                lines.append(" ".join(map(str, grid[r * SIDE : (r + 1) * SIDE])))
    lines.append("%d %d" % (rng.randint(1, SIDE), rng.randint(1, SIDE)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
