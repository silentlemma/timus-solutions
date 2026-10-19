"""Arguments: seed mode. Modes 1..8 create 1000 independent cylinders."""

import random
import sys

LIMIT = 1_000_000
COUNT = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    targets = {
        1: (1, 1000),
        2: (275807, 780100),
        3: (LIMIT, LIMIT),
        4: (3, 11),
        5: (LIMIT, 1),
        6: (1, 1),
        7: (rng.randint(1, LIMIT), rng.randint(1, LIMIT)),
        8: (780100, 275807),
    }
    width, height = targets[mode]
    cylinders = []
    for index in range(COUNT):
        if mode in (2, 8):
            cylinder_height = 746639 + rng.randint(-2, 2)
            circumference = 390050 + rng.randint(-2, 2)
        elif mode == 1:
            cylinder_height = rng.randint(1, 50)
            circumference = rng.randint(20, 500)
        elif mode == 4:
            cylinder_height = rng.randint(1, 15)
            circumference = rng.randint(1, 15)
        elif index % 4 == 0:
            cylinder_height, circumference = height, width
        elif index % 4 == 1:
            cylinder_height = max(1, height - 1)
            circumference = max(1, width - 1)
        else:
            cylinder_height = rng.randint(1, LIMIT)
            circumference = rng.randint(1, LIMIT)
        cylinders.append((cylinder_height, circumference))
    return width, height, cylinders


def render(width, height, cylinders):
    return f"{width} {height}\n{len(cylinders)}\n" + "".join(
        f"{cylinder_height} {circumference}\n"
        for cylinder_height, circumference in cylinders
    )


if __name__ == "__main__":
    print(render(*generate(int(sys.argv[1]), int(sys.argv[2]))), end="")
