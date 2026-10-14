"""One test from a seed and a mode, keeping machine B no slower than
every toy on A (or on C). Mode 1 takes 100000 toys with B dominated by A,
mode 2 with B dominated by C, mode 3 takes the largest times, mode 4 is
small, mode 5 gives every toy the same times. Mode 6 has only early toys
and a continuously busy C; mode 7 has only late toys and a slow A;
mode 8 alternates opposite extreme triples. Modes 6-8 accept an optional
toy count (default 100000); mode 8 requires a positive even count."""

import random
import sys

LARGEST = 100000
TOP = 10**6
SMALL = 8


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7, 8):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else LARGEST
        if not 1 <= n <= LARGEST or (mode == 8 and n % 2):
            raise ValueError("invalid toy count")
        print(n)
        for i in range(n):
            if mode == 8:
                toy = (TOP, 1, 1) if i % 2 == 0 else (1, 1, TOP)
            else:
                short = rng.randint(1, 1000)
                b = rng.randint(1, 1000)
                long = rng.randint(TOP // 2, TOP)
                toy = (short, b, long) if mode == 6 else (long, b, short)
            print(*toy)
        return
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST
    limit = TOP if mode == 3 else rng.randint(2, TOP)
    cap = rng.randint(1, limit)  # no b exceeds this, and the dominated side starts here
    toys = []
    for _ in range(n):
        b = rng.randint(1, cap)
        dominant = rng.randint(cap, limit)
        free = rng.randint(1, limit)
        if mode == 2 or (mode == 4 and seed % 2):
            toys.append((free, b, dominant))
        else:
            toys.append((dominant, b, free))
    if mode == 5:
        toys = [toys[0]] * n
    print(n)
    print("\n".join("%d %d %d" % t for t in toys))


main()
