"""A random key sequence: a seed, its length and the share of cursor keys
in percent."""

import random
import sys

KEYS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:;-!?., "
PERCENT = 100


def main():
    seed, length, moves = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    line = []
    for _ in range(length):
        if rng.randrange(PERCENT) < moves:
            line.append(rng.choice("<>"))
        else:
            line.append(rng.choice(KEYS))
    sys.stdout.write("".join(line) + "\n")


if __name__ == "__main__":
    main()
