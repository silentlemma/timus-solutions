"""Generate seed/mode: 1 small; 2 many components; 3 zero; 4 positive bound;
5 empty; 6 points; 7 alternating signs; 8 random full bounds; 9 shifted components."""

import random
import sys

MAX_COUNT = 10
MAX_REFERENCE = 1000
BRANCHES = [0, 512, 256, 128, 64, 32, 16, 8, 4, 2]


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        return [rng.randrange(-4, 5) for _ in range(rng.randrange(1, 6))]
    if mode == 2:
        return BRANCHES.copy()
    if mode == 3:
        return [0] * MAX_COUNT
    if mode == 4:
        return [MAX_REFERENCE] * MAX_COUNT
    if mode == 5:
        return [
            rng.randrange(-MAX_REFERENCE, MAX_REFERENCE + 1)
            for _ in range(MAX_COUNT - 1)
        ] + [-2]
    if mode == 6:
        return [rng.randrange(0, MAX_REFERENCE + 1) for _ in range(MAX_COUNT - 1)] + [
            -1
        ]
    if mode == 7:
        return [MAX_REFERENCE if i % 2 else -MAX_REFERENCE for i in range(MAX_COUNT)]
    if mode == 8:
        return [
            rng.randrange(-MAX_REFERENCE, MAX_REFERENCE + 1) for _ in range(MAX_COUNT)
        ]
    if mode == 9:
        return [-MAX_REFERENCE] + BRANCHES[1:]
    raise ValueError("Unknown mode")


def main():
    constants = generate(*map(int, sys.argv[1:]))
    print(len(constants))
    print(*constants)


if __name__ == "__main__":
    main()
