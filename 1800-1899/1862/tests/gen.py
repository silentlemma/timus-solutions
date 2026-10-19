"""A height from a seed and a mode: mode 1 a small one, 2 a large one,
3 one near a multiple of the modulus."""

import random
import sys

MOD = 10 ** 9 + 7
LIMIT = 10 ** 18


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randint(2, 60))
    elif mode == 2:
        print(rng.randint(2, LIMIT))
    else:
        print(rng.randint(1, LIMIT // MOD - 1) * MOD + rng.randint(-2, 2))


main()
