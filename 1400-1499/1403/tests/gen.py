"""Orders: a seed and a mode, 1000 orders each. Mode 1 is random, mode 2
gives every order time enough, mode 3 crowds the orders into the first
50 days, mode 4 uses short or large legal deadlines and equal rewards."""

import random
import sys

N = 1000
MAX_VALUE = 100000
SHORT_DEADLINE = 300


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(N)
    for _ in range(N):
        if mode == 1:
            d, r = rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)
        elif mode == 2:
            d, r = rng.randint(N, MAX_VALUE), rng.randint(1, MAX_VALUE)
        elif mode == 3:
            d, r = rng.randint(1, 50), rng.randint(1, MAX_VALUE)
        else:
            d, r = rng.choice((rng.randint(1, SHORT_DEADLINE), rng.randint(N + 1, MAX_VALUE))), 7
        print(d, r)


main()
