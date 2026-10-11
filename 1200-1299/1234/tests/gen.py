"""A brick and a hole: a seed and a mode. Mode 1 draws all five lengths
anywhere; mode 2 makes the brick's best face a little longer than the
hole but no wider, so only a turned fit can work."""

import random
import sys

LOW, HIGH = 10, 100
LONGER = 15


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        v = [rng.randint(LOW, HIGH) for _ in range(5)]
    else:
        a = rng.randint(LOW + 1, HIGH - 1)
        b = rng.randint(LOW, a)
        q = rng.randint(LOW, b)
        p = rng.randint(a + 1, min(HIGH, a + LONGER))
        c = rng.randint(p, HIGH)
        brick, hole = [p, q, c], [a, b]
        rng.shuffle(brick)
        rng.shuffle(hole)
        v = brick + hole
    sys.stdout.write(" ".join("%d.%d" % divmod(x, 10) for x in v) + "\n")


if __name__ == "__main__":
    main()
