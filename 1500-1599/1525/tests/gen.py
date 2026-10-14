"""One test from a seed and a mode, with 100000 instructions unless small.
Mode 1 takes the largest room and random moves, mode 2 a random room,
mode 3 long runs of one move, which push every start to a wall, mode 4
is small."""

import random
import sys

LARGEST = 100000
SMALL = 6
MOVES = "udlrfb"


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        sizes = [rng.randint(1, SMALL) for _ in range(3)]
        program = "".join(rng.choice(MOVES) for _ in range(rng.randint(0, SMALL)))
    else:
        sizes = [LARGEST] * 3 if mode == 1 else [rng.randint(1, LARGEST) for _ in range(3)]
        if mode == 3:
            program = "".join(
                rng.choice(MOVES) * rng.randint(1, LARGEST // 10) for _ in range(SMALL * 2)
            )
            program = program[:LARGEST]
        else:
            program = "".join(rng.choice(MOVES) for _ in range(LARGEST))
    print(*sizes)
    print(program)


main()
