"""Usage: gen.py SEED MODE; modes: random, inside, near_plane, slender, disjoint."""

import random
import sys

DIMENSIONS = 3
BOUND = 200
INNER_BOUND = 50


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "near_plane":
        points = [[-BOUND, -BOUND, 99], [BOUND, -BOUND, 99], [0, BOUND, 99]]
    elif mode == "slender":
        points = [[-BOUND, -BOUND, -BOUND], [BOUND, 199, 198], [199, 198, 197]]
    elif mode == "disjoint":
        points = [[-BOUND, -BOUND, 101], [BOUND, -BOUND, 101], [0, BOUND, 101]]
    else:
        assert mode in ("random", "inside")
        bound = BOUND if mode == "random" else INNER_BOUND
        while True:
            points = [
                [rng.randint(-bound, bound) for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)
            ]
            a = [points[1][i] - points[0][i] for i in range(DIMENSIONS)]
            b = [points[2][i] - points[0][i] for i in range(DIMENSIONS)]
            normal = [
                a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0],
            ]
            if any(normal):
                break
    axes = list(range(DIMENSIONS))
    rng.shuffle(axes)
    signs = [rng.choice((-1, 1)) for _ in range(DIMENSIONS)]
    points = [[signs[j] * p[axes[j]] for j in range(DIMENSIONS)] for p in points]
    rng.shuffle(points)
    return points


def main():
    for point in generate(int(sys.argv[1]), sys.argv[2]):
        print(*point)


if __name__ == "__main__":
    main()
