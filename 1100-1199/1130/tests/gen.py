"""Random vectors no longer than L: a seed, N, L and a mode. Mode 0 takes
random integer points of the disk, mode 1 points near its rim, mode 2
vectors close to three directions 120 degrees apart, mode 3 copies of a
few vectors mixed with zero vectors."""

import math
import random
import sys

DIRECTIONS = 3
FEW = 4
RIM = 0.9


def point(rng, length, low):
    while True:
        x = rng.randint(-length, length)
        y = rng.randint(-length, length)
        if low * length * length <= x * x + y * y <= length * length:
            return x, y


def main():
    seed, n, length, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    vectors = []
    if mode == 1:
        vectors = [point(rng, length, RIM * RIM) for _ in range(n)]
    elif mode == 2:
        for _ in range(n):
            angle = 2 * math.pi * rng.randrange(DIRECTIONS) / DIRECTIONS + rng.uniform(-0.1, 0.1)
            r = length * rng.uniform(RIM, 1)
            x, y = int(r * math.cos(angle)), int(r * math.sin(angle))
            vectors.append((x, y))
    elif mode == 3:
        few = [point(rng, length, RIM * RIM) for _ in range(FEW)] + [(0, 0)]
        vectors = [rng.choice(few) for _ in range(n)]
    else:
        vectors = [point(rng, length, 0) for _ in range(n)]
    lines = [str(n), str(length)] + ["%d %d" % v for v in vectors]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
