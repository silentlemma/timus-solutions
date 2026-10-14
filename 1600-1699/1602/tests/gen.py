"""One input from SEED MODE.

random: uniform valid floors and hundredth-second speeds.
fast-lift: n=99, k=98, a fast lift and walking four to ten times slower.
near-double: walking takes one hundredth more than twice the lift time per floor.
"""

import random
import sys


def decimal(value):
    return f"{value // 100}.{value % 100:02d}"


def main():
    seed, mode = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "random":
        n = rng.randint(3, 99)
        k = rng.randint(2, n - 1)
        v = rng.randint(11, 9998)
        u = rng.randint(v + 1, 9999)
    elif mode == "fast-lift":
        n, k = 99, 98
        v = rng.randint(11, 49)
        u = rng.randint(4 * v, 10 * v)
    elif mode == "near-double":
        n = rng.randint(30, 99)
        k = rng.randint(2, n - 1)
        v = rng.randint(500, 4500)
        u = 2 * v + 1
    else:
        raise SystemExit(f"unknown mode: {mode}")
    print(n, k, decimal(u), decimal(v))


if __name__ == "__main__":
    main()
