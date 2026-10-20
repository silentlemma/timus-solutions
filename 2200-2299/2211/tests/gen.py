"""Print one deterministic area: python gen.py MODE SEED."""

import math
import random
import sys

MAX_AREA = 10**9
AREA_MULTIPLE = 6
SMALL_LIMIT = 1000
BOUNDARY_WIDTH = 1000
MIN_TRIANGLE_AREA = 6
PRIME_FACTORS = (2, 3, 5, 7, 11, 13, 17, 19)
HERON_AREAS = (6, 12, 24, 30, 36, 42, 60, 84, 210)
DENSE_AREAS = (698377680, 735134400, 821620800, 918918000, 980179200)
POWER_BASES = (2, 3, 5, 7)
MODE_SMALL = 1
MODE_UNIFORM = 2
MODE_DIVISIBLE = 3
MODE_SMOOTH = 4
MODE_BOUNDARY = 5
MODE_SCALED = 6
MODE_DENSE = 7
MODE_POWER = 8


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL:
        return rng.randint(1, SMALL_LIMIT)
    if mode == MODE_UNIFORM:
        return rng.randint(1, MAX_AREA)
    if mode == MODE_DIVISIBLE:
        return AREA_MULTIPLE * rng.randint(1, MAX_AREA // AREA_MULTIPLE)
    if mode == MODE_SMOOTH:
        area = MIN_TRIANGLE_AREA
        while True:
            choices = [prime for prime in PRIME_FACTORS if area * prime <= MAX_AREA]
            if not choices:
                return area
            area *= rng.choice(choices)
    if mode == MODE_BOUNDARY:
        # Every other seed selects the exact upper bound.
        return MAX_AREA if seed % 2 == 0 else MAX_AREA - rng.randrange(BOUNDARY_WIDTH)
    if mode == MODE_SCALED:
        base = rng.choice(HERON_AREAS)
        limit = math.isqrt(MAX_AREA // base)
        scale = rng.randint(1, limit)
        return base * scale * scale
    if mode == MODE_DENSE:
        return rng.choice(DENSE_AREAS)
    if mode == MODE_POWER:
        base = rng.choice(POWER_BASES)
        choices = []
        area = MIN_TRIANGLE_AREA
        while area <= MAX_AREA:
            choices.append(area)
            area *= base
        return rng.choice(choices)
    raise ValueError("mode must be between 1 and %d" % MODE_POWER)


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), int(sys.argv[2])))
