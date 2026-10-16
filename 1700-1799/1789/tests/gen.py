"""One input from a seed and a mode: mode 1 a random even n in 14..30,
mode 2 a random odd n in 65..95. Usage: gen.py SEED MODE.
"""

import random
import sys


def main():
    seed, mode = (int(value) for value in sys.argv[1:])
    rng = random.Random(seed)
    if mode == 1:
        print(rng.randrange(14, 31, 2))
    elif mode == 2:
        print(rng.randrange(65, 96, 2))
    else:
        raise ValueError("unknown mode")


main()
