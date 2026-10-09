"""A random ball and two points: a seed and the shape (0 any points, 1 the
ball near the segment AB, 2 A, C and B on one line)."""

import random
import sys

ANY, NEAR, LINE = 0, 1, 2
TOP = 1000


def point(rng):
    return [rng.randint(-TOP, TOP) for _ in range(3)]


def dist2(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def main():
    seed, shape = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        a, b = point(rng), point(rng)
        if shape == NEAR:
            t = rng.random()
            c = [round(x + t * (y - x)) + rng.randint(-50, 50) for x, y in zip(a, b)]
        elif shape == LINE:
            step = [rng.randint(-50, 50) for _ in range(3)]
            k = rng.randint(1, 9)
            c = point(rng)
            a = [x - k * s for x, s in zip(c, step)]
            b = [x + rng.randint(1, 9) * s for x, s in zip(c, step)]
        else:
            c = point(rng)
        if not all(abs(x) <= TOP for x in a + b + c):
            continue
        near = min(dist2(a, c), dist2(b, c))
        if near < 4:
            continue
        r = 1
        while (r + 1) ** 2 < near and rng.random() < 0.999:
            r += 1
        r = rng.randint(max(1, r // 2), r)
        break
    lines = [" ".join(map(str, p)) for p in (a, b, c)] + [str(r)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
