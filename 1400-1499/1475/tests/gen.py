"""1000 tests from a seed and a mode.

Mode 1: H and l with random numbers of digits up to 100.
Mode 2: both H and l near 10^100.
Mode 3: symmetric roofs at or just off an exact bottom bounce.
Mode 4: H = 1 and random 100-digit l, giving nearly 100-digit answers.
Mode 5: l = 1 and random 100-digit H, giving extremely steep roofs.
Mode 6: asymmetric rational slopes at or just off an exact bottom bounce.
"""

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
        elif mode == 4:
            height = 1
            run = rng.randint(top // 10, top)
        elif mode == 5:
            height = rng.randint(top // 10, top)
            run = 1
        elif mode == 6:
            a, b = rng.choice(((1, 2), (2, 1), (3, 7), (7, 3)))
            square_sum = a * a + b * b
            k = square_sum * rng.randint(1, 10 ** rng.randint(1, DIGITS // 2 - 4))
            # H=a*t, l=b*t and t=4*h*a*k*(k+1)/(a^2+b^2).
            scale = 4 * drop * a * (k * (k + 1) // square_sum)
            height = a * scale
            run = b * scale + rng.choice((-1, 0, 1))
            if not (1 <= height <= top and 1 <= run <= top):
                continue
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
