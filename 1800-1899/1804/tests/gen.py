"""Usage: gen.py SEED MODE.

Mode 1: 200 random first games with scores 0..30.
Mode 2: 200 low-scoring first games with scores 0..3.
Mode 3: 199 random one-goal margins with scores 10..28.
Mode 4: 200 random games with two-digit scores and margins of at least two,
        reaching the maximum input byte length allowed by the sentence format.
"""

import random
import sys

TESTS = 200
MOST = 30
FEW = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (3, 4):
        count = TESTS - 1 if mode == 3 else TESTS
        print(count)
        for _ in range(count):
            where = rng.choice(["home", "away"])
            if mode == 3:
                x = rng.randint(10, 27)
                y = x + 1
            else:
                x, y = rng.sample(range(10, MOST + 1), 2)
                while abs(x - y) < 2:
                    x, y = rng.sample(range(10, MOST + 1), 2)
            if rng.randrange(2):
                x, y = y, x
            print("The Machinegunners played %s game, scored %d goals, and conceded %d goals."
                  % (where, x, y))
        return
    top = MOST if mode == 1 else FEW
    print(TESTS)
    for _ in range(TESTS):
        where = rng.choice(["home", "away"])
        x, y = rng.randint(0, top), rng.randint(0, top)
        print("The Machinegunners played %s game, scored %d goals, and conceded %d goals."
              % (where, x, y))


main()
