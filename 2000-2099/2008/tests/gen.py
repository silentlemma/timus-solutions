"""Usage: gen.py SEED MODE.

Modes: max,zero,equal,beyond,apex,above,oneway,sign,fall,diagonal_low,diagonal_high,random.
"""

import random
import sys

LIMIT = 10000
BOUNDARY_SPEED = 7
APEX_SPEED = 14
DIAGONAL_SPEED = 486


def generate(seed, mode):
    if mode in ("max", "zero"):
        return LIMIT if mode == "max" else 0, (LIMIT, LIMIT), (0, 0), (LIMIT, 0)
    if mode in ("equal", "beyond"):
        return BOUNDARY_SPEED, (0, 1), (0, 0), (5 if mode == "equal" else 6, 0)
    if mode in ("apex", "above"):
        return APEX_SPEED, (0, 10 if mode == "apex" else 11), (0, 0), (1, 0)
    if mode == "oneway":
        return BOUNDARY_SPEED, (1, 1), (0, 0), (0, 10)
    if mode == "sign":
        return BOUNDARY_SPEED, (0, LIMIT), (0, 0), (1, 0)
    if mode == "fall":
        return BOUNDARY_SPEED, (0, 0), (0, 1), (5, 1)
    if mode in ("diagonal_low", "diagonal_high"):
        speed = DIAGONAL_SPEED + (mode == "diagonal_high")
        return speed, (LIMIT, LIMIT), (0, 0), (1, 0)
    if mode != "random":
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    points = []
    while len(points) < 3:
        point = rng.randint(0, LIMIT), rng.randint(0, LIMIT)
        if point not in points:
            points.append(point)
    return rng.randint(0, 500), *points


if __name__ == "__main__":
    speed, *points = generate(int(sys.argv[1]), sys.argv[2])
    print(speed)
    for point in points:
        print(*point)
