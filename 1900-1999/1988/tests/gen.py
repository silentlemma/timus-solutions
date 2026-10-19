"""Usage: gen.py SEED MODE; modes: random, radial, visible, tangent, antipodal, minimum_speed, maximum_speed."""

import random
import sys

DIMENSIONS = 3
BOUND = 100


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "radial":
        a, s, speed = [99, 0, 0], [BOUND, 0, 0], BOUND
    elif mode == "visible":
        a, s, speed = [BOUND, BOUND, 0], [BOUND, BOUND, 1], BOUND
    elif mode == "tangent":
        a, s, speed = [BOUND, BOUND, 0], [-BOUND, -BOUND, 1], BOUND
    elif mode == "antipodal":
        a, s, speed = [BOUND, 0, 0], [-BOUND, 1, 0], 1
    else:
        assert mode in ("random", "minimum_speed", "maximum_speed")
        while True:
            a = [rng.randint(-BOUND, BOUND) for _ in range(DIMENSIONS)]
            s = [rng.randint(-BOUND, BOUND) for _ in range(DIMENSIONS)]
            if 0 < sum(x * x for x in a) < sum(x * x for x in s):
                break
        speed = (
            1
            if mode == "minimum_speed"
            else BOUND
            if mode == "maximum_speed"
            else rng.randint(1, BOUND)
        )
    axes = list(range(DIMENSIONS))
    rng.shuffle(axes)
    signs = [rng.choice((-1, 1)) for _ in range(DIMENSIONS)]
    return (
        [signs[i] * a[axes[i]] for i in range(DIMENSIONS)],
        [signs[i] * s[axes[i]] for i in range(DIMENSIONS)],
        speed,
    )


if __name__ == "__main__":
    carrier, ship, speed = generate(int(sys.argv[1]), sys.argv[2])
    print(*carrier)
    print(*ship)
    print(speed)
