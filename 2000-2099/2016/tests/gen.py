"""Usage: seed mode. Modes: vertical, horizontal, near_coincident,
near_coplanar, spatial, mixed. Every mode has 1000 integer-coordinate experiments.
The constructed circles have positive path height after the initial point;
all third circles remain above zero and horizontal threshold equality is avoided.
"""

import math
import random
import sys

COUNT = 1000
MAX_SPEED = 50000
MAX_ACCELERATION = 1000
MAX_COORDINATE = 1000000
KINDS = ("vertical", "horizontal", "near_coincident", "near_coplanar", "spatial")
FOUR = 4
FIVE = 5
SIX = 6
THREE = 3
HUNDRED = 100


def experiment(rng, kind):
    if kind == "vertical":
        s = rng.randint(1, MAX_COORDINATE // FOUR)
        centers = [(s, 0, 0), (s, 0, THREE * s), (FOUR * s, 0, THREE * s)]
        target = rng.choice((1, 2, THREE, FOUR)) * s
    elif kind == "horizontal":
        bound = 21
        s = rng.randint(1, MAX_COORDINATE // bound)
        centers = [(FOUR * s, 0, -THREE * s), (FOUR * s, 16 * s, 2 * s), (bound * s, 16 * s, 2 * s)]
        target = 2 * s
    elif kind == "near_coincident":
        k = rng.randint(10, MAX_COORDINATE // SIX)
        centers = [
            (THREE * k, FOUR * k, 0),
            (THREE * k + THREE, FOUR * k + FOUR, FIVE * k),
            (2 * k + THREE, FIVE * k + FOUR, SIX * k),
        ]
        target = SIX * k
    elif kind == "near_coplanar":
        t = rng.choice((1, 2, FIVE, 20, HUNDRED, 200, 350, FOUR * HUNDRED))
        u = 2 * t + 1
        x, y, r = u * u - t * t, 2 * u * t, u * u + t * t
        dz = rng.choice((0, t * t // 2))
        centers = [
            (x, y, 0),
            (x + THREE, y + FOUR, r),
            (x + THREE - t * t, y + FOUR + t * t, r + dz),
        ]
        target = r + dz
    else:
        assert kind == "spatial"
        s = rng.randint(1, MAX_COORDINATE // 10)
        h = rng.randint(1, 2 * s)
        q, y, ell = rng.randint(1, 2 * h), rng.randint(-h, h), rng.randint(0, h)
        if y == 0:
            y = 1
        centers = [
            (FOUR * s, 0, -THREE * s),
            (FOUR * s, 0, 2 * s + h),
            (FOUR * s + q, y, 2 * s + h + ell),
        ]
        target = 2 * s + h + ell
    acceleration = rng.randint(1, min(MAX_ACCELERATION, max(1, int(MAX_SPEED**2 / (2 * target)))))
    speed = max(
        1, min(MAX_SPEED, round(math.sqrt(2 * acceleration * target)) + rng.choice((-1, 0, 1)))
    )
    if kind == "horizontal" and speed * speed == FOUR * acceleration * s:
        speed = speed + 1 if speed < MAX_SPEED else speed - 1
    if kind == "near_coplanar" and speed * speed == 2 * acceleration * centers[-1][2]:
        speed = speed + 1 if speed < MAX_SPEED else speed - 1
    if rng.randrange(2):
        centers = [(-x, y, z) for x, y, z in centers]
    if rng.randrange(2):
        centers = [(y, x, z) for x, y, z in centers]
    return speed, acceleration, centers


def generate(seed, mode):
    if mode not in KINDS and mode != "mixed":
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    lines = [str(COUNT)]
    for _ in range(COUNT):
        kind = rng.choice(KINDS) if mode == "mixed" else mode
        speed, acceleration, centers = experiment(rng, kind)
        lines.append(f"{speed} {acceleration}")
        lines.extend(" ".join(map(str, center)) for center in centers)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
