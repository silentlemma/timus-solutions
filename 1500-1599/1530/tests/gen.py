"""One test from a seed and a mode, n = 100000 unless small. Mode 1 takes
random p and q, mode 2 a compatible pair, mode 3 p of all ones, mode 4 a
compatible pair with q as large as p allows, mode 5 is small, mode 6 carries
across n-1 ones of p, mode 7 carries across n-1 ones of q with p zero, and
mode 8 has a random compatible prefix and a final clash after a long tail."""

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
    if mode == 6:
        p = ["0"] + ["1"] * (n - 1)
        q = ["1"] + ["0"] * (n - 1)
    if mode == 7:
        p = ["0"] * n
        q = ["0"] + ["1"] * (n - 1)
    if mode == 8:
        middle = n // 2
        q = [("0" if a == "1" else b) for a, b in zip(p, q)]
        p[middle - 1] = q[middle - 1] = "0"
        p[middle:] = ["0"] * (n - middle)
        q[middle:] = ["1"] * (n - middle)
        p[-1] = "1"
    print(n)
    print("".join(p))
    print("".join(q))


main()
