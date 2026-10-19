"""A permutation and a vector from a seed.

Mode 1: small sizes. Mode 2: one cycle through all 5 * 10^4 teams. Mode 3: a
random permutation of 5 * 10^4. Mode 4: cycles of every length 1, 2, 3, ...
Mode 5: the identity. Modes 2-5 take m = 5 * 10^4 and the largest q.
Mode 6: maximum m, minimum n, with weights only on odd powers.
Mode 7: minimum m, maximum n, with one shuffled long cycle.
Mode 8: maximum dimensions, a random permutation, and six nonzero powers.
Mode 9: maximum dimensions, repeated 33-cycles and five fixed points,
        with every weight equal to the maximum.
Mode 10: medium random permutation and weights chosen from zero, one,
         the maximum, and random values.
"""

import random
import sys

MAX = 5 * 10 ** 4
SMALL = 12
TOP = 10 ** 9


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 6:
        n, m = 2, MAX
        p = [2, 1]
        q = [TOP if t % 2 else 0 for t in range(1, m + 1)]
    elif mode == 7:
        n, m = MAX, 2
        order = rng.sample(range(1, n + 1), n)
        p = [0] * n
        for i, x in enumerate(order):
            p[x - 1] = order[(i + 1) % n]
        q = [TOP, TOP - 1]
    elif mode == 8:
        n = m = MAX
        p = rng.sample(range(1, n + 1), n)
        q = [0] * m
        for t in (1, 32, 33, 32768, MAX - 1, MAX):
            q[t - 1] = TOP - rng.randrange(SMALL)
    elif mode == 9:
        n = m = MAX
        size = 33
        covered = n - n % size
        order = rng.sample(range(1, covered + 1), covered)
        p = list(range(1, n + 1))
        for pos in range(0, covered, size):
            cycle = order[pos:pos + size]
            for i, x in enumerate(cycle):
                p[x - 1] = cycle[(i + 1) % size]
        q = [TOP] * m
    elif mode == 10:
        n, m = 193, 257
        p = rng.sample(range(1, n + 1), n)
        q = [rng.choice((0, 1, TOP, rng.randint(0, TOP))) for _ in range(m)]
    elif mode == 1:
        n, m = rng.randint(2, SMALL), rng.randint(2, SMALL)
        p = rng.sample(range(1, n + 1), n)
        q = [rng.randint(0, TOP) for _ in range(m)]
    else:
        n = m = MAX
        q = [TOP - rng.randint(0, SMALL) for _ in range(m)]
        order = rng.sample(range(1, n + 1), n)
        if mode == 2:
            sizes = [n]
        elif mode == 3:
            sizes = None
        elif mode == 4:
            sizes, k = [], 1
            while sum(sizes) + k <= n:
                sizes.append(k)
                k += 1
            sizes.append(n - sum(sizes))
        else:
            sizes = [1] * n
        if sizes is None:
            p = order
        else:
            p = [0] * n
            pos = 0
            for size in sizes:
                cycle = order[pos:pos + size]
                for i, x in enumerate(cycle):
                    p[x - 1] = cycle[(i + 1) % size]
                pos += size
    print(m, n)
    print(*p)
    print(*q)


main()
