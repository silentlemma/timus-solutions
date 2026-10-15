"""One test from a seed and a mode: mode 1 a small web with repeated
threads, mode 2 100000 knots and threads at random with every thread cut,
mode 3 a long chain cut in random order, mode 4 a star, mode 5 a dense web
on few knots with some threads cut."""

import random
import sys

MOST = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(2, 8)
        threads = [tuple(rng.sample(range(1, n + 1), 2)) for _ in range(rng.randint(1, 12))]
    elif mode == 2:
        n = MOST
        threads = [tuple(rng.sample(range(1, n + 1), 2)) for _ in range(MOST)]
    elif mode == 3:
        n = MOST
        threads = [(i, i + 1) for i in range(1, n)]
    elif mode == 4:
        n = MOST
        threads = [(1, i) for i in range(2, n + 1)]
    else:
        n = rng.randint(5, 30)
        threads = [tuple(rng.sample(range(1, n + 1), 2)) for _ in range(rng.randint(50, 300))]
    m = len(threads)
    q = m if mode in (2, 3) else rng.randint(1, m)
    cuts = rng.sample(range(1, m + 1), q)
    print(n, m)
    for a, b in threads:
        print(a, b)
    print(q)
    print(*cuts)


main()
