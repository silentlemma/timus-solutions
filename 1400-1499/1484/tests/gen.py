"""One test from a seed and a mode: mode 1 picks X, Y and N at random
(often a rating no set of votes can show), mode 2 shows the true rating
of N random votes, mode 3 does the same for a million votes."""

import random
import sys

LARGEST = 1000000
SMALL = 1000
TOP = 10


def shown(total, n):
    """The rating rounded to tenths, as tenths: half a tenth rounds up."""
    return (20 * total + n) // (2 * n)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    y = rng.randint(10, 100)
    if mode == 1:
        x, n = rng.randint(10, 100), rng.randint(1, SMALL)
    else:
        n = LARGEST if mode == 3 else rng.randint(1, SMALL)
        x = shown(sum(rng.randint(1, TOP) for _ in range(min(n, SMALL))) * (n // min(n, SMALL)), n)
    print("%d.%d %d.%d %d" % (x // 10, x % 10, y // 10, y % 10, n))


main()
