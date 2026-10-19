"""A permutation and a vector from a seed.

Mode 1: small sizes. Mode 2: one cycle through all 5 * 10^4 teams. Mode 3: a
random permutation of 5 * 10^4. Mode 4: cycles of every length 1, 2, 3, ...
Mode 5: the identity. Modes 2-5 take m = 5 * 10^4 and the largest q.
"""

import random
import sys

MAX = 5 * 10 ** 4
SMALL = 12
TOP = 10 ** 9


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
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
