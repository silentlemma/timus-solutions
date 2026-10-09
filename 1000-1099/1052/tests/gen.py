"""Random rabbits: a seed, N, the number of planted lines and the most
points on a line. Each planted line gets a random direction (small
coordinates, any signs) and up to that many points along it; the rest are
random. All points are distinct and within [-2000, 2000]."""

import random
import sys

LIMIT = 2000


def main():
    seed, n, lines, most = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    points = set()
    for _ in range(lines):
        while True:
            dx, dy = rng.randint(-7, 7), rng.randint(-7, 7)
            if (dx, dy) != (0, 0):
                break
        x, y = rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)
        k = rng.randint(most // 2, most)
        steps = rng.sample(range(-k * 3, k * 3), k)
        for s in steps:
            q = (x + s * dx, y + s * dy)
            if len(points) < n and abs(q[0]) <= LIMIT and abs(q[1]) <= LIMIT:
                points.add(q)
    while len(points) < n:
        points.add((rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)))
    order = list(points)
    rng.shuffle(order)
    sys.stdout.write("\n".join([str(n)] + ["%d %d" % q for q in order]) + "\n")


if __name__ == "__main__":
    main()
