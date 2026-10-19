"""Usage: gen.py SEED MODE; modes: unique_levels,same_level,zigzag,staggered,wide_sparse,outside,late_pinch,random."""

import random
import sys

MAXIMUM = 100000
BOUND = 1000000000


def generate(seed, mode):
    rng = random.Random(seed)
    count = MAXIMUM
    if mode == "random":
        ly = [0] + sorted(rng.sample(range(1, 20), rng.randrange(7))) + [20]
        ry = [0] + sorted(rng.sample(range(1, 20), rng.randrange(7))) + [20]
        shift = rng.choice((-BOUND + 100, 0, BOUND - 100))
        left = [(shift + rng.randint(-30, -1), y) for y in ly]
        right = [(shift + rng.randint(1, 30), y) for y in ry]
        poles = sorted(
            [(shift + rng.randint(-40, 40), rng.randint(-3, 23)) for _ in range(rng.randrange(25))],
            key=lambda p: p[1],
        )
        return left, right, poles
    if mode == "wide_sparse":
        left, right = [(-BOUND, -BOUND), (-BOUND, BOUND)], [(BOUND, -BOUND), (BOUND, BOUND)]
        poles = [(0, -BOUND + i * (2 * BOUND) // (count - 1)) for i in range(count)]
    elif mode == "zigzag":
        left = [((i % 2) * (BOUND - 1), i) for i in range(count)]
        right = [(x + 1, y) for x, y in left]
        poles = left.copy()
    elif mode == "staggered":
        left = [((i % 2) * 1000, 2 * i) for i in range(count)]
        ys = [0] + [2 * i + 1 for i in range(count - 2)] + [2 * (count - 1)]
        right = [(2000, y) for y in ys]
        poles = [(-1, 2 * i) for i in range(count)]
    elif mode == "interleaved":
        left = [((i % 2) * 1000, 3 * i) for i in range(count)]
        ys = [0] + [3 * i + 1 for i in range(count - 2)] + [3 * (count - 1)]
        right = [(2000, y) for y in ys]
        poles = [(500, 3 * i + 2) for i in range(count)]
    elif mode == "outside":
        left = [(i % 7 - 10, i) for i in range(count)]
        right = [(x + 20, y) for x, y in left]
        poles = [(0, i - count) for i in range(count)]
    else:
        assert mode in ("unique_levels", "same_level", "late_pinch")
        left = [(0, i) for i in range(count)]
        width = count + 1 if mode == "same_level" else 1000000
        right = [(width, i) for i in range(count)]
        if mode == "unique_levels":
            poles = [(width // 2, i) for i in range(count)]
        elif mode == "same_level":
            poles = [((i * 7919) % count + 1, count // 2) for i in range(count)]
        else:
            right[-1] = (7, count - 1)
            poles = []
    return left, right, poles


def render(left, right, poles):
    return "".join(
        str(len(points)) + "\n" + "".join(f"{x} {y}\n" for x, y in points)
        for points in (left, right, poles)
    )


if __name__ == "__main__":
    sys.stdout.write(render(*generate(int(sys.argv[1]), sys.argv[2])))
