"""A grid function: a seed and a mode. Mode 1 gives B - A + 1 random values,
mode 2 long runs up and down with flat stretches, mode 3 a zigzag that
changes way at every step, mode 4 a constant function."""

import random
import sys

SIZE = 100000
TOP = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    a = rng.randint(0, 5)
    n = SIZE - a + 1
    if mode == 1:
        values = [rng.randint(-TOP, TOP) for _ in range(n)]
    elif mode == 2:
        values, v, way = [], 0, 1
        while len(values) < n:
            for _ in range(rng.randint(1, 500)):
                v = max(-TOP, min(TOP, v + way * rng.choice([0, 0, 1, 3])))
                values.append(v)
            way = -way
        values = values[:n]
    elif mode == 3:
        values = [TOP if i % 2 else -TOP for i in range(n)]
    else:
        values = [rng.randint(-TOP, TOP)] * n
    print(a, SIZE)
    for i in range(0, n, 20):
        print(*values[i : i + 20])


main()
