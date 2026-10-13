"""Random people around the field: a seed and a mode. Umbrellas never
overlap and never cover a corner post. Mode 1 is a 10 000 by 10 000
field with 1000 people anywhere in range, mode 2 a long thin field with
people crowding its border, mode 3 a 1 by 1 to 3 by 3 field with the
few umbrellas that fit around it, mode 4 as many people as fit on a 60 by 40
field with centres near the border lines. Mode 5 places 1000 people along a
1 by 10 000 strip, mixing asymmetric crossings with near-external tangencies."""

import math
import random
import sys

LIMIT = 10000
PEOPLE = 1000


def place(rng, width, length, count, pick):
    corners = [(0, 0), (length, 0), (0, width), (length, width)]
    people = []
    for _ in range(count * 50):
        if len(people) == count:
            break
        x, y = pick()
        if any(math.hypot(x - cx, y - cy) < 1 for cx, cy in corners):
            continue
        if any(math.hypot(x - px, y - py) < 2 for px, py in people):
            continue
        people.append((x, y))
    return people


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        width = length = LIMIT
        people = place(
            rng,
            width,
            length,
            PEOPLE,
            lambda: (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)),
        )
    elif mode == 2:
        width, length = 3, LIMIT

        def pick():
            x = round(rng.uniform(-2, length + 2), 2)
            y = round(rng.choice([0, width]) + rng.uniform(-1.2, 1.2), 2)
            return x, y

        people = place(rng, width, length, PEOPLE, pick)
    elif mode == 3:
        width, length = rng.randint(1, 3), rng.randint(1, 3)

        def pick():
            return round(rng.uniform(-1.5, length + 1.5), 3), round(
                rng.uniform(-1.5, width + 1.5), 3
            )

        people = place(rng, width, length, 6, pick)
    elif mode == 5:
        width, length = 1, LIMIT
        people = []
        for i in range(PEOPLE):
            x = round(5 + 9 * i + rng.uniform(-0.4, 0.4), 6)
            y = rng.choice([-0.999999, -0.999, -0.5, 0.05, 0.2, 0.8, 1.6, 1.999999])
            y = round(y + rng.uniform(-0.0000001, 0.0000001), 8)
            people.append((x, y))
    else:
        width, length = 40, 60

        def pick():
            if rng.random() < 0.5:
                x = rng.choice([0, length]) + round(rng.uniform(-1, 1), 1)
                return x, round(rng.uniform(-1, width + 1), 1)
            y = rng.choice([0, width]) + round(rng.uniform(-1, 1), 1)
            return round(rng.uniform(-1, length + 1), 1), y

        people = place(rng, width, length, PEOPLE, pick)
    print(width, length)
    print(len(people))
    for x, y in people:
        print(x, y)


main()
