"""Generate one N,K input. Modes:

random SEED N: fixed N and a seeded uniform K from 0 through N*(N-1)//2.
"""

import random
import sys


def main():
    mode, seed, n = sys.argv[1:]
    seed, n = int(seed), int(n)
    if mode != "random" or not 1 <= n <= 100:
        raise ValueError("usage: gen.py random SEED N, with 1 <= N <= 100")
    rng = random.Random(seed)
    k = rng.randint(0, n * (n - 1) // 2)
    sys.stdout.buffer.write(f"{n} {k}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
