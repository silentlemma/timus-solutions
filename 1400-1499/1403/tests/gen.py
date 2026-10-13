"""Orders: a seed and a mode, 1000 orders each. Mode 1 is random, mode 2
gives every order time enough, mode 3 crowds the orders into the first
50 days, mode 4 uses deadlines past 100 000 and equal rewards."""

import random
import sys

N = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(N)
    for _ in range(N):
        if mode == 1:
            d, r = rng.randint(1, 100000), rng.randint(1, 100000)
        elif mode == 2:
            d, r = rng.randint(N, 100000), rng.randint(1, 100000)
        elif mode == 3:
            d, r = rng.randint(1, 50), rng.randint(1, 100000)
        else:
            d, r = rng.choice((rng.randint(1, 300), rng.randint(100001, 200000))), 7
        print(d, r)


main()
