"""One test from a seed and a mode: mode 1 draws 100 submissions from a
few teams, mode 2 from many teams (few repeats), mode 3 uses names of 30
characters, mode 4 has no submissions or a single one."""

import random
import sys

LARGEST = 100
LONGEST = 30
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def name(rng, length):
    return "".join(rng.choice(ALPHABET) for _ in range(length))


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        n = rng.randint(0, 1)
        teams = [name(rng, rng.randint(1, LONGEST))]
    else:
        n = LARGEST
        count = {1: 10, 2: 90, 3: 30}[mode]
        length = LONGEST if mode == 3 else rng.randint(1, 8)
        teams = list({name(rng, length) for _ in range(count)})
    print(n)
    for _ in range(n):
        print(rng.choice(teams))


main()
