"""One test from a seed and a mode: mode 1 small and random, mode 2 300 x
1500 random, mode 3 300 x 300 with a staircase (each monster beaten by
the fighters from its own number on), mode 4 300 x 1500 sparse, mode 5
300 x 300 where the fighters split into closed groups."""

import random
import sys

MOST_N = 300
MOST_M = 1500


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, 8)
        m = rng.randint(n, 10)
        rows = [[int(rng.random() < 0.5) for _ in range(m)] for _ in range(n)]
    elif mode == 2:
        n, m = MOST_N, MOST_M
        p = rng.choice((0.01, 0.1, 0.5))
        rows = [[int(rng.random() < p) for _ in range(m)] for _ in range(n)]
    elif mode == 3:
        n = m = MOST_N
        order = list(range(m))
        rng.shuffle(order)
        rows = [[int(order.index(j) >= i) for j in range(m)] for i in range(n)]
    elif mode == 4:
        n, m = MOST_N, MOST_M
        rows = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in rng.sample(range(m), rng.randint(1, 3)):
                rows[i][j] = 1
    else:
        n = m = MOST_N
        size = rng.choice((2, 3, 5, 10))
        rows = [[int(i // size == j // size and rng.random() < 0.7 or i == j) for j in range(m)]
                for i in range(n)]
    print(n, m)
    for row in rows:
        print("".join(map(str, row)))


main()
