"""Pigeons from "MODE SEED": mode 1 a few random pigeons, mode 2 100 random
pigeons, mode 3 100 pigeons close to a halves pattern, mode 4 100 pigeons
close to an alternating pattern."""

import random
import sys

LEFT = ("<@..", ".OO=", r"./\.")
RIGHT = ("..@>", "=OO.", r"./\.")
MAX_N = 100
SMALL_N = 8
FLIPS = 10


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = 2 * rng.randint(1, SMALL_N // 2)
    else:
        n = MAX_N
    if mode <= 2:
        left = [rng.randint(0, 1) for _ in range(n)]
    elif mode == 3:
        left = [int(i < n // 2) for i in range(n)]
    else:
        left = [i % 2 for i in range(n)]
    if mode >= 3:
        for i in rng.sample(range(n), rng.randint(0, FLIPS)):
            left[i] ^= 1
    print(n)
    for line in range(len(LEFT)):
        print(".".join(LEFT[line] if x else RIGHT[line] for x in left))


main()
