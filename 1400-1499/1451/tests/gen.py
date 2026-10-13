"""Modes:
random SEED: three distinct uniform seven-decimal houses in [-1000, 1000]^2.
near120 SEED: rotated unequal arms, with a corner 0.01--0.1 degrees below 120.
"""

import math
import random
import sys


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "random":
        points = set()
        houses = []
        while len(houses) < 3:
            p = (rng.randint(-10000000000, 10000000000),
                 rng.randint(-10000000000, 10000000000))
            if p not in points:
                points.add(p)
                houses.append(tuple(c / 10000000 for c in p))
    elif mode == "near120":
        x, y = rng.uniform(-100, 100), rng.uniform(-100, 100)
        rotation = rng.uniform(-math.pi, math.pi)
        angle = math.radians(120 - rng.uniform(0.01, 0.1))
        short, long = rng.uniform(20, 100), rng.uniform(700, 850)
        houses = [(x, y),
                  (x + short * math.cos(rotation), y + short * math.sin(rotation)),
                  (x + long * math.cos(rotation + angle),
                   y + long * math.sin(rotation + angle))]
        rng.shuffle(houses)
    else:
        raise ValueError("expected random SEED or near120 SEED")
    sys.stdout.reconfigure(newline="\n")
    print(" ".join(f"{c:.7f}" for p in houses for c in p))


if __name__ == "__main__":
    main()
