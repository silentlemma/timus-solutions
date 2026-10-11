"""Two ships and a drop in eight dimensions: a seed and a mode. Mode 1
draws any points and a radius, mode 2 a large drop between two far
ships, mode 3 small coordinates. Both ships are always outside the
drop."""

import random
import sys

TOP = 1000
RADIUS = 3000
DIM = 8


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    span = 10 if mode == 3 else TOP
    while True:
        a = [rng.randint(-span, span) for _ in range(DIM)]
        b = [rng.randint(-span, span) for _ in range(DIM)]
        if mode == 2:
            c = [(x + y) // 2 + rng.randint(-50, 50) for x, y in zip(a, b)]
            c = [max(-TOP, min(TOP, x)) for x in c]
        else:
            c = [rng.randint(-span, span) for _ in range(DIM)]
        d2 = min(sum((x - y) ** 2 for x, y in zip(p, c)) for p in (a, b))
        top = min(RADIUS, int(d2**0.5))
        while top * top >= d2:
            top -= 1
        if top >= 1:
            r = rng.randint(max(1, top // 2), top)
            break
    lines = [" ".join(map(str, p)) for p in (a, b, c)] + ["%d" % r]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
