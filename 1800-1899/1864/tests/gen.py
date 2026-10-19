"""Friends and their juice from a seed and a mode: mode 1 a few friends,
2 the most friends at random, 3 the most friends where one bought all
and the rest nothing, 4 the most friends who bought nearly the same."""

import random
import sys

MOST = 100
JUICE = 100


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 6) if mode == 1 else MOST
    if mode == 3:
        bought = [0] * n
        bought[rng.randrange(n)] = rng.randint(1, JUICE)
    elif mode == 4:
        base = rng.randint(1, JUICE - 1)
        bought = [base + rng.randint(0, 1) for _ in range(n)]
    else:
        bought = [rng.randint(0, JUICE) for _ in range(n)]
        if not any(bought):
            bought[0] = 1
    print(n)
    print(*bought)


main()
