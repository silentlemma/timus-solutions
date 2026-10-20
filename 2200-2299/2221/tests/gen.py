"""Deterministic inputs: python gen.py MODE SEED."""

import math
import random
import sys
from functools import cmp_to_key

MAX_N = 100_000
LIMIT = 10**9
SMALL_N = 80
MEDIUM_MIN = 500
MEDIUM_MAX = 3000
VECTOR_BOUND = 600
JITTER = 100
STRIDE = 1000

SMALL = 1
MEDIUM = 2
RANDOM_MAX = 3
LINE_MAX = 4
CONVEX_MAX = 5
BALANCED_MAX = 6
NEAR_LINE_MAX = 7
ARCH_MAX = 8


def vectors():
    edges = [
        (dx, dy)
        for dx in range(1, VECTOR_BOUND + 1)
        for dy in range(1, VECTOR_BOUND + 1)
        if math.gcd(dx, dy) == 1
    ]

    def compare(a, b):
        cross = a[1] * b[0] - b[1] * a[0]
        return (cross > 0) - (cross < 0)

    edges.sort(key=cmp_to_key(compare))
    return edges


def generate(mode, seed):
    rng = random.Random(seed)
    if mode in (SMALL, MEDIUM, RANDOM_MAX):
        if mode == SMALL:
            n = rng.randint(1, SMALL_N)
        elif mode == MEDIUM:
            n = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        else:
            n = MAX_N
        xs = rng.sample(range(-LIMIT, LIMIT + 1), n)
        ys = rng.sample(range(-LIMIT, LIMIT + 1), n)
        points = list(zip(xs, ys))
    elif mode == LINE_MAX:
        xs = rng.sample(range(-LIMIT, LIMIT + 1), MAX_N)
        slope = rng.choice((-1, 1))
        points = [(x, slope * x) for x in xs]
    elif mode == CONVEX_MAX:
        x, y = 0, 0
        points = []
        for dx, dy in vectors()[:MAX_N]:
            x += dx
            y -= dy
            points.append((x, y))
    elif mode == BALANCED_MAX:
        points = [None] * MAX_N
        pending = [(0, MAX_N)]
        height = MAX_N
        while pending:
            low, high = pending.pop()
            if low == high:
                continue
            middle = (low + high) // 2
            points[middle] = (middle * STRIDE - LIMIT, height)
            height -= 1
            pending.append((middle + 1, high))
            pending.append((low, middle))
    elif mode == NEAR_LINE_MAX:
        points = [
            (i * STRIDE - LIMIT, i * STRIDE + rng.randint(-JITTER, JITTER)) for i in range(MAX_N)
        ]
    elif mode == ARCH_MAX:
        edges = vectors()
        x, y = 0, 0
        points = []
        seen = set()
        # A convex chain crossing its lowest point, with distinct ordinates.
        for dx, dy in [(dx, -dy) for dx, dy in reversed(edges[: MAX_N // 2])] + edges:
            x += dx
            y += dy
            if y not in seen:
                points.append((x, -y))
                seen.add(y)
            if len(points) == MAX_N:
                break
    else:
        raise ValueError("unknown mode")
    rng.shuffle(points)
    return points


def main():
    mode, seed = map(int, sys.argv[1:])
    points = generate(mode, seed)
    print(len(points))
    sys.stdout.write("".join(f"{x} {y}\n" for x, y in points))


if __name__ == "__main__":
    main()
