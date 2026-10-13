"""A seed and a mode, with 25 counterclockwise vertices in every mode.

Mode 1: irregular radial polygon with uneven angular spacing and deep bays.
Mode 2: random strictly convex polygon sampled from an integer parabola.
Mode 3: random x-monotone polygon with jagged upper and lower chains.
"""

import math
import random
import sys

N = 25
TOP = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        points = []
        for i in range(N):
            angle = 2 * math.pi * (i + rng.uniform(-0.3, 0.3)) / N
            radius = rng.randint(65, 490)
            points.append((round(500 + radius * math.cos(angle)),
                           round(500 + radius * math.sin(angle))))
    elif mode == 2:
        xs = sorted(rng.sample(range(-22, 23), N))
        points = [(500 + 22 * x, 10 + 2 * x * x) for x in xs]
    elif mode == 3:
        lower_xs = sorted(rng.sample(range(1, TOP), 11))
        upper_xs = sorted(rng.sample(range(1, TOP), 10), reverse=True)
        points = [(0, 0)]
        points += [(x, rng.randint(0, 460)) for x in lower_xs]
        points += [(TOP, 0), (TOP, TOP)]
        points += [(x, rng.randint(540, TOP)) for x in upper_xs]
        points += [(0, TOP)]
    else:
        raise ValueError("mode must be 1, 2, or 3")
    return points


def main():
    seed, mode = map(int, sys.argv[1:])
    points = generate(seed, mode)
    print(len(points))
    for x, y in points:
        print(x, y)


if __name__ == "__main__":
    main()
