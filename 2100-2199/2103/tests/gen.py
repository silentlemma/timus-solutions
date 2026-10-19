"""Print one deterministic input with: python gen.py MODE SEED.

Modes: 1 small, 2 random, 3 maximum target, 4 powers of two, 5 powers of three,
6 coprime residues, 7 direct multiples, 8 one paid step between free jumps,
9 smooth targets needing two paid steps, 10 downward or self, 11 near the limit.
Every input has a unique minimum time; its optimal route may not be unique.
"""

import math
import random
import sys

MAX_START = 7
MAX_TARGET = 1_000_000_000
SMALL_TARGET = 1_000
NEAR_LIMIT = 1_000
THREE = 3
FIVE = 5
SIX = 6
COPRIME_MODULUS = 2 * THREE * FIVE * MAX_START

SMALL = 1
RANDOM = 2
MAXIMUM = 3
POWERS_TWO = 4
POWERS_THREE = 5
COPRIME = 6
MULTIPLES = 7
ONE_STEP = 8
TWO_STEPS = 9
DOWNWARD = 10
NEAR_MAXIMUM = 11


def powers(base):
    values = []
    value = 1
    while value <= MAX_TARGET:
        values.append(value)
        value *= base
    return values


def generate(mode, seed):
    rng = random.Random(seed)
    start = rng.randint(1, MAX_START)
    if mode == SMALL:
        target = rng.randint(1, SMALL_TARGET)
    elif mode == RANDOM:
        target = rng.randint(1, MAX_TARGET)
    elif mode == MAXIMUM:
        start = 1 + seed % MAX_START
        target = MAX_TARGET
    elif mode == POWERS_TWO:
        target = rng.choice(powers(2))
    elif mode == POWERS_THREE:
        target = rng.choice(powers(THREE))
    elif mode == COPRIME:
        target = rng.randint(MAX_TARGET // 2, MAX_TARGET)
        while math.gcd(target, COPRIME_MODULUS) != 1:
            target -= 1
    elif mode == MULTIPLES:
        target = start * rng.randint(1, MAX_TARGET // start)
    elif mode == ONE_STEP:
        start = rng.randint(2, MAX_START)
        before = start * rng.randint(1, MAX_TARGET // (2 * start))
        after = before + rng.choice((-1, 1))
        multiplier = rng.randint(1, MAX_TARGET // after)
        while math.gcd(multiplier, start) != 1:
            multiplier = rng.randint(1, MAX_TARGET // after)
        target = after * multiplier
    elif mode == TWO_STEPS:
        start = SIX
        base = rng.choice((2, THREE))
        target = rng.choice([value for value in powers(base) if value > start])
    elif mode == DOWNWARD:
        target = rng.randint(1, start)
    elif mode == NEAR_MAXIMUM:
        target = MAX_TARGET - rng.randint(0, NEAR_LIMIT)
    else:
        raise ValueError("unknown generator mode")
    return start, target


def main():
    mode, seed = map(int, sys.argv[1:])
    print(*generate(mode, seed))


if __name__ == "__main__":
    main()
