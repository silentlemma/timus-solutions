"""One test from a seed and a mode: mode 1 random colours, mode 2 two or
three colours, mode 3 every count divisible by 2, 3, 5 or more, mode 4
exactly two colours with odd counts."""

import random
import sys

EDGES = 30
COLOURS = 30
SPLITS = (2, 3, 5, 6, 10, 15)
PER_LINE = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        rods = [rng.randint(1, COLOURS) for _ in range(EDGES)]
    elif mode == 2:
        palette = rng.sample(range(1, COLOURS + 1), rng.choice((2, 3)))
        rods = [rng.choice(palette) for _ in range(EDGES)]
    elif mode == 3:
        size = rng.choice(SPLITS)
        rods = [c for c in (rng.randint(1, COLOURS) for _ in range(EDGES // size)) for _ in range(size)]
    else:
        a, b = rng.sample(range(1, COLOURS + 1), 2)
        pairs = (rng.randint(1, COLOURS) for _ in range(EDGES // 2 - 1))
        rods = [a, b] + [c for c in pairs for _ in range(2)]
    rng.shuffle(rods)
    for i in range(0, EDGES, PER_LINE):
        print(" ".join(map(str, rods[i:i + PER_LINE])))


main()
