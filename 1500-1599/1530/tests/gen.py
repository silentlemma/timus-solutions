"""One test from a seed and a mode, n = 100000 unless small. Mode 1 takes
random p and q, mode 2 a compatible pair, mode 3 p of all ones, mode 4 a
compatible pair with q as large as p allows, mode 5 is small."""

import random
import sys

LARGEST = 100000
SMALL = 8


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 5 else LARGEST
    p = [rng.choice("01") for _ in range(n)]
    q = [rng.choice("01") for _ in range(n)]
    if mode == 3:
        p = ["1"] * n
    if mode in (2, 4):
        q = [("0" if a == "1" else ("1" if mode == 4 else b)) for a, b in zip(p, q)]
    print(n)
    print("".join(p))
    print("".join(q))


main()
