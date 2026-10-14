"""One test from a seed and a mode: two periods of one length up to nine.
Mode 1 uses any digits, mode 2 only 0 and 9, mode 3 makes the sum a block
of nines or one more than that, mode 4 repeats a short block."""

import random
import sys

LONGEST = 9


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    k = rng.randint(1, LONGEST)
    top = 10**k
    if mode == 3:
        a = rng.randrange(top)
        b = (top - 1 - a + rng.randint(0, 1)) % top
        a, b = str(a).zfill(k), str(b).zfill(k)
    else:
        digits = "09" if mode == 2 else "0123456789"
        size = rng.choice([d for d in range(1, k + 1) if k % d == 0]) if mode == 4 else k
        a = "".join(rng.choice(digits) for _ in range(size)) * (k // size)
        b = "".join(rng.choice(digits) for _ in range(size)) * (k // size)
    print("(%s)" % a)
    print("(%s)" % b)


main()
