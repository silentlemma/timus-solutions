"""seed mode:1 small,2 full,3 independent,4 tangent,5 perturbed,6 collector,
7 first-chain,8 second-chain,9 collinear,10 internal tangent,11 disjoint,
12 guaranteed feasible. All families preserve distinct integer terminals.
"""

import random
import sys

COORDINATE_BOUND = 10000
TERMINALS = 3
FULL = 2
INDEPENDENT = 3
TANGENT = 4
PERTURBED = 5
COLLECTOR = 6
FIRST_CHAIN = 7
SECOND_CHAIN = 8
COLLINEAR = 9
INTERNAL = 10
DISJOINT = 11
FEASIBLE = 12


def make_case(seed, mode):
    rng = random.Random(seed)
    if mode in (1, FULL):
        bound = 10 if mode == 1 else COORDINATE_BOUND
        radius = rng.randint(1, bound)
        points = set()
        while len(points) < TERMINALS:
            points.add((rng.randint(-bound, bound), rng.randint(-bound, bound)))
        points = sorted(points)
        rng.shuffle(points)
    elif mode == INDEPENDENT:
        radius = rng.randint(1, COORDINATE_BOUND // 2)
        points = [(0, 0), (-2 * radius, 0), (2 * radius, 0)]
    elif mode in (TANGENT, PERTURBED):
        radius = rng.randint(1, COORDINATE_BOUND - 1)
        shift = rng.choice((-1, 1)) if mode == PERTURBED else 0
        points = [(-radius + shift, 0), (radius, radius), (radius, -radius)]
    elif mode in (COLLECTOR, FIRST_CHAIN, SECOND_CHAIN):
        definitions = {
            COLLECTOR: (8, [(-10, -11), (4, 5), (10, 1)]),
            FIRST_CHAIN: (4, [(-8, 6), (2, 11), (-5, 3)]),
            SECOND_CHAIN: (5, [(-12, 0), (-11, -2), (-2, -10)]),
        }
        radius, points = definitions[mode]
        scale = rng.randint(1, 800)
        radius *= scale
        points = [(x * scale, y * scale) for x, y in points]
    elif mode in (COLLINEAR, INTERNAL):
        radius = rng.randint(1, COORDINATE_BOUND // TERMINALS)
        points = [(0, 0), (TERMINALS * radius, 0), (radius, 0)]
        if mode == COLLINEAR:
            points[2] = (2 * radius, 0)
    elif mode == DISJOINT:
        radius = rng.randint(1, 2)
        points = [
            (-COORDINATE_BOUND, -COORDINATE_BOUND),
            (COORDINATE_BOUND, COORDINATE_BOUND),
            (COORDINATE_BOUND - 1, COORDINATE_BOUND),
        ]
    elif mode == FEASIBLE:
        radius = rng.randint(2, 6000)
        offset = rng.randint(1, radius // 2)
        points = [
            (-radius // 2, -offset),
            (-radius // 2, offset),
            (radius // 2, offset),
        ]
    else:
        raise ValueError("unknown mode")
    if rng.randrange(2):
        points = [(-x, y) for x, y in points]
    if rng.randrange(2):
        points = [(y, x) for x, y in points]
    if rng.randrange(2):
        points[1], points[2] = points[2], points[1]
    return radius, points


def main():
    radius, points = make_case(int(sys.argv[1]), int(sys.argv[2]))
    print(radius)
    for x, y in points:
        print(x, y)


if __name__ == "__main__":
    main()
