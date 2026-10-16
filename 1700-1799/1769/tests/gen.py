"""One test from a seed and a mode: mode 1 up to 30 random digits, mode 2
100 000 random digits, mode 3 the numbers from a random start written
one after another up to 100 000 digits, mode 4 100 000 copies of one
digit."""

import random
import sys

FEW = 30
MOST = 100000
START = 50000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        s = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, FEW)))
    elif mode == 2:
        s = "".join(rng.choice("0123456789") for _ in range(MOST))
    elif mode == 3:
        parts, total, x = [], 0, rng.randint(1, START)
        while total < MOST:
            parts.append(str(x))
            total += len(parts[-1])
            x += 1
        s = "".join(parts)[:MOST]
    else:
        s = rng.choice("0123456789") * MOST
    print(s)


main()
