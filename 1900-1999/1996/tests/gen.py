"""Usage: gen.py SEED MODE; random_mid,random_long,all_ones,all_changes,periodic,no_match,one_window,longer,threshold,late_exact."""

import random
import sys

MAXIMUM = 250000
BYTE_WIDTH = 8


def generate(seed, mode):
    rng = random.Random(seed)
    n = MAXIMUM
    if mode in ("random_mid", "random_long", "threshold"):
        m = {"random_mid": n // 2, "random_long": 220000, "threshold": n - 2048}[mode]
        return [rng.randrange(2) for _ in range(n)], [rng.randrange(2) for _ in range(m)]
    if mode == "all_ones":
        return [255] * n, [255] * (n - 2048)
    if mode == "all_changes":
        return [254] * n, [255] * (n // 2)
    if mode == "periodic":
        return [2 * (i % 2) for i in range(n)], [2 * (i % 2) + 1 for i in range(n // 2)]
    if mode == "no_match":
        return [0] * n, [0] * (n // 2 - 1) + [2]
    if mode == "one_window":
        a = [rng.randrange(256) for _ in range(n)]
        return a, [v ^ 1 for v in a]
    if mode == "longer":
        return [0] * (n - 1), [0] * n
    if mode == "late_exact":
        m = n // 2
        return [0] * m + [1] * m, [1] * m
    raise ValueError(mode)


if __name__ == "__main__":
    text, pattern = generate(int(sys.argv[1]), sys.argv[2])
    print(len(text), len(pattern))
    print(" ".join(format(value, "0" + str(BYTE_WIDTH) + "b") for value in text))
    print(" ".join(format(value, "0" + str(BYTE_WIDTH) + "b") for value in pattern))
