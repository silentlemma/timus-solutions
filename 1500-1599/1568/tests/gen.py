"""One test from a seed and a mode: an order of n cars. Mode 1 is random
with n = 10000, mode 2 reversed, mode 3 has exactly 2^13 runs of numbers
in order and mode 4 one run more, mode 5 is small."""

import random
import sys

LARGEST = 10000
SMALL = 12
RUNS = 2**13


def with_runs(rng, n, runs):
    """An order of 1..n whose numbers split into exactly the given number of
    runs that already stand in order."""
    cuts = sorted(rng.sample(range(1, n), runs - 1))
    bounds = [0] + cuts + [n]
    blocks = [list(range(bounds[i] + 1, bounds[i + 1] + 1)) for i in range(runs)]
    # later runs go first, so each run starts before the one it follows
    order = []
    for block in reversed(blocks):
        order.extend(block)
    return order


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        cars = list(range(1, LARGEST + 1))
        rng.shuffle(cars)
    elif mode == 2:
        cars = list(range(LARGEST, 0, -1))
    elif mode in (3, 4):
        cars = with_runs(rng, LARGEST, RUNS + (mode == 4))
    else:
        n = rng.randint(1, SMALL)
        cars = list(range(1, n + 1))
        rng.shuffle(cars)
    print(len(cars))
    print(*cars)


main()
