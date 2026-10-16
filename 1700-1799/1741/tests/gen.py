"""One test from a seed and a mode: mode 1 a few versions and updates,
mode 2 10000 versions and 10000 random updates, mode 3 a chain of 9999
updates of the largest size, mode 4 many updates of each kind between
nearby versions."""

import random
import sys

KINDS = ("Pirated", "Cracked", "Licensed")
MOST = 10000
FEW = 8
BIG = 10 ** 6
NEAR = 5


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    updates = []
    if mode == 1:
        n = rng.randint(2, FEW)
        for _ in range(rng.randint(1, 3 * FEW)):
            x = rng.randint(1, n - 1)
            updates.append((x, rng.randint(x + 1, n), rng.randint(1, 20), rng.choice(KINDS)))
    elif mode == 2:
        n = MOST
        for _ in range(MOST):
            x = rng.randint(1, n - 1)
            updates.append((x, rng.randint(x + 1, n), rng.randint(1, BIG), rng.choice(KINDS)))
    elif mode == 3:
        n = MOST
        kinds = ("Cracked", "Licensed")
        updates = [(x, x + 1, BIG, rng.choice(kinds)) for x in range(1, n)]
    else:
        n = MOST // 4
        for _ in range(MOST):
            x = rng.randint(1, n - 1)
            y = min(n, x + rng.randint(1, NEAR))
            updates.append((x, y, rng.randint(1, BIG), rng.choice(KINDS)))
    print(n, len(updates))
    print("\n".join("%d %d %d %s" % u for u in updates))


main()
