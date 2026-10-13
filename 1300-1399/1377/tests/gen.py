"""Mode random: random SEED N M prints two distinct uniformly sampled
graves in an N by M cemetery (2 <= N, M <= 100).
"""

import random
import sys


def main():
    mode, seed, n, m = sys.argv[1:]
    if mode != "random":
        raise ValueError("unknown mode")
    seed, n, m = int(seed), int(n), int(m)
    if not (2 <= n <= 100 and 2 <= m <= 100):
        raise ValueError("dimensions must be between 2 and 100")
    rng = random.Random(seed)
    first, second = rng.sample(range(n * m), 2)
    sys.stdout.reconfigure(newline="\n")
    print(n, m)
    for cell in (first, second):
        print(cell // m + 1, cell % m + 1)


if __name__ == "__main__":
    main()
