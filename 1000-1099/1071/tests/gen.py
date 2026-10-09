"""A random pair: a seed, the largest x and the mode (0 any y below x, 1 y
made by crossing out digits of x in a random base)."""

import random
import sys

ANY, CROSSED = 0, 1


def main():
    seed, top, mode = (int(v) for v in sys.argv[1:4])
    rng = random.Random(seed)
    while True:
        x = rng.randint(2, top)
        if mode == ANY:
            y = rng.randint(1, x - 1)
        else:
            base = rng.choice([rng.randint(2, 40), rng.randint(2, x)])
            digits = []
            v = x
            while v:
                digits.append(v % base)
                v //= base
            kept = [d for d in reversed(digits) if rng.random() < 0.5]
            y = 0
            for d in kept:
                y = y * base + d
        if 1 <= y < x:
            break
    sys.stdout.write("%d %d\n" % (x, y))


if __name__ == "__main__":
    main()
