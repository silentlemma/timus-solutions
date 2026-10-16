"""One test from a seed: 200 first games with random venue and scores
from 0 to 30, mode 2 limits the scores to 0..3 so that ties abound."""

import random
import sys

TESTS = 200
MOST = 30
FEW = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = MOST if mode == 1 else FEW
    print(TESTS)
    for _ in range(TESTS):
        where = rng.choice(["home", "away"])
        x, y = rng.randint(0, top), rng.randint(0, top)
        print("The Machinegunners played %s game, scored %d goals, and conceded %d goals."
              % (where, x, y))


main()
