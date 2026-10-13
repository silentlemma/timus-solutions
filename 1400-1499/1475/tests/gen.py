"""1000 tests from a seed and a mode. Mode 1 draws H and l with random
numbers of digits up to 100, mode 2 keeps both near 10^100, mode 3 puts
the k-th bounce exactly on the lowest point or just off it."""

import random
import sys

TESTS = 1000
DIGITS = 100
TALLEST = 10
SHIFTS = (-1, 0, 0, 1)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    top = 10**DIGITS
    lines = [str(TESTS)]
    while len(lines) <= TESTS:
        drop = rng.randint(1, TALLEST)
        if mode == 1:
            height = rng.randint(1, 10 ** rng.randint(0, DIGITS))
            run = rng.randint(1, 10 ** rng.randint(0, DIGITS))
        elif mode == 2:
            height = top - rng.randint(0, top // 10)
            run = top - rng.randint(0, top // 10)
        else:
            # H = l = 2 h k (k + 1) lands bounce k on the lowest point exactly
            k = rng.randint(1, 10 ** rng.randint(1, DIGITS // 2 - 1))
            height = run = 2 * drop * k * (k + 1)
            height += rng.choice(SHIFTS)
            if height < 1 or height > top:
                continue
        lines.append("%d %d %d" % (height, run, drop))
    print("\n".join(lines))


main()
