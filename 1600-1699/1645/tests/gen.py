"""One test from a seed and a mode: a random finishing order of n skiers
(mode 1 small, mode 2 2000 skiers, mode 3 2000 skiers finishing almost in
the starting order, mode 4 2000 skiers shuffled within ordered blocks of 50)."""

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
    elif mode == 4:
        for start in range(0, n, 50):
            block = order[start : start + 50]
            rng.shuffle(block)
            order[start : start + 50] = block
    else:
        rng.shuffle(order)
    print(n)
    print(*order)


main()
