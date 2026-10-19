"""Stick lengths from a seed and a mode: mode 1 short sticks, 2 long
sticks, 3 one short and one long stick, 4 equal sticks,
5 independent lengths across the full range."""

import random
import sys

LONGEST = 10000
SHORT = 10


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        a, b = rng.randint(1, SHORT), rng.randint(1, SHORT)
    elif mode == 2:
        a, b = rng.randint(LONGEST // 2, LONGEST), rng.randint(LONGEST // 2, LONGEST)
    elif mode == 3:
        a, b = rng.randint(1, SHORT), rng.randint(LONGEST // 2, LONGEST)
    elif mode == 5:
        a, b = rng.randint(1, LONGEST), rng.randint(1, LONGEST)
    else:
        a = b = rng.randint(1, LONGEST)
    print(a, b)


main()
