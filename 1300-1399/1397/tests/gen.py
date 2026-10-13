"""Several games in one input: a seed and a mode.

Mode 1: ten games of 1000 random points.
Mode 2: sixty small random games.
Mode 3: ten games on a circle.
Mode 4: ten games of points in a few tight clusters.
Mode 5: eighty tiny lattice games with repeated points and distance ties.
Mode 6: ten maximal games with 998 coincident points and two distinct outliers.
"""

import math
import random
import sys

N = 500
TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    games = []
    if mode == 1:
        for _ in range(10):
            games.append([(rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)) for _ in range(2 * N)])
    elif mode == 2:
        for _ in range(60):
            n = rng.randint(1, 30)
            games.append([(rng.randint(-50, 50), rng.randint(-50, 50)) for _ in range(2 * n)])
    elif mode == 3:
        for _ in range(10):
            games.append(
                [
                    (round(TOP * math.cos(t)), round(TOP * math.sin(t)))
                    for t in (rng.uniform(0, 2 * math.pi) for _ in range(2 * N))
                ]
            )
    elif mode == 5:
        sites = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for _ in range(80):
            n = rng.randint(2, 4)
            pool = rng.sample(sites, rng.randint(2, 4))
            games.append([rng.choice(pool) for _ in range(2 * n)])
    elif mode == 6:
        for _ in range(10):
            cx, cy = rng.randint(-5000, 5000), rng.randint(-5000, 5000)
            dx, dy = rng.randint(1, 5000), rng.randint(1, 5000)
            game = [(cx, cy)] * (2 * N - 2)
            game += [(cx + dx, cy), (cx, cy - dy)]
            rng.shuffle(game)
            games.append(game)
    else:
        for _ in range(10):
            centres = [(rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)) for _ in range(3)]
            game = []
            for _ in range(2 * N):
                cx, cy = rng.choice(centres)
                game.append((cx + rng.randint(-5, 5), cy + rng.randint(-5, 5)))
            games.append(game)
    lines = []
    for game in games:
        lines.append(str(len(game) // 2))
        lines += ["%d %d" % p for p in game]
    print("\n".join(lines))


main()
