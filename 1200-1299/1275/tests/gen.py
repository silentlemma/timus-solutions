"""A feast: a seed and a mode. The goblets are made by starting from F at
every knight and applying random servant visits backwards, so the plan
exists and has at most as many visits as were applied. Mode 1 draws a
small table, mode 2 up to 1000 knights and many visits, mode 3 an even
cycle (N = 2K or N divisible by K with an even quotient), mode 4 random
goblets, often impossible."""

import random
import sys

KNIGHTS = 1000
TOP = 1000
VISITS = 30000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode in (1, 4) else rng.randint(2, KNIGHTS)
    if mode == 3:
        n = 2 * rng.randint(1, KNIGHTS // 2)
        k = rng.choice([n // 2] + [d for d in range(1, n) if n % d == 0 and (n // d) % 2 == 0])
    else:
        k = rng.randint(1, n - 1)
    f = rng.randint(0, 20 if mode == 1 else TOP)
    goblets = [f] * n
    if mode == 4:
        goblets = [rng.randint(0, 6) for _ in range(n)]
        f = rng.randint(0, 6)
    else:
        budget = rng.randint(0, 40 if mode == 1 else VISITS // 2)
        for _ in range(budget):
            i = rng.randrange(n)
            j = (i + k) % n
            step = rng.choice([1, -1])
            if 0 <= goblets[i] - step <= TOP and 0 <= goblets[j] - step <= TOP:
                goblets[i] -= step
                goblets[j] -= step
    sys.stdout.write("%d %d %d\n%s\n" % (n, k, f, " ".join(map(str, goblets))))


if __name__ == "__main__":
    main()
