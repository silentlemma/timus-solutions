"""Generate seed mode inputs; mode random gives independent lines within all bounds."""

import random
import sys

COORDINATE_BOUND = 1000
DIMENSION = 3
POINTS = 4


def main():
    seed, mode = sys.argv[1:]
    assert mode == "random"
    rng = random.Random(int(seed))
    points = [
        [rng.randint(-COORDINATE_BOUND, COORDINATE_BOUND) for _ in range(DIMENSION)]
        for _ in range(POINTS)
    ]
    assert points[0] != points[1] and points[2] != points[-1]
    for row in points:
        print(*row)


if __name__ == "__main__":
    main()
