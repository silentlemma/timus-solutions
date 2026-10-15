"""One test from a seed and a mode: a random finishing order of n skiers
(mode 1 small, mode 2 2000 skiers, mode 3 2000 skiers finishing almost in
the starting order)."""

import random
import sys

MOST = 2000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 10) if mode == 1 else MOST
    order = list(range(1, n + 1))
    if mode == 3:
        for _ in range(n // 10):
            i = rng.randrange(n - 1)
            order[i], order[i + 1] = order[i + 1], order[i]
    else:
        rng.shuffle(order)
    print(n)
    print(*order)


main()
