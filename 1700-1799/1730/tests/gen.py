"""One test from a seed and a mode: mode 1 shares with power-of-two
denominators up to 1024, written unreduced, mode 2 any shares, mostly
impossible, mode 3 ten animals with 1/1024 to 1015/1024, mode 4 a
single animal."""

import random
import string
import sys

LEAVES = 1024
MOST = 10
TOP = 1500
NAME = 19


def split(rng, total, parts):
    cuts = sorted(rng.sample(range(1, total), parts - 1))
    return [b - a for a, b in zip([0] + cuts, cuts + [total])]


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    m = 1 if mode == 4 else MOST if mode == 3 else rng.randint(1, MOST)
    names = set()
    while len(names) < m:
        names.add("".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, NAME))))
    names = list(names)
    if mode == 2:
        denominator = rng.randint(m, TOP)
    else:
        denominator = LEAVES if mode == 3 else 2 ** rng.randint(m.bit_length(), MOST)
    counts = [1] * (m - 1) + [denominator - m + 1] if mode == 3 else split(rng, denominator, m)
    if m == 1:
        counts = [denominator]
    shares = []
    for c in counts:
        k = rng.randint(1, TOP // denominator)
        shares.append("%d/%d" % (c * k, denominator * k))
    print("-".join(names))
    print(" ".join(shares))


main()
