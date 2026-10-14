"""One test from a seed and a mode: n objects with coordinates up to 10^4
and speeds up to 100, all starting farther apart than d. Mode 1 is 500
random objects, mode 2 500 objects flying away from the origin, mode 3
pairs heading straight at each other, mode 4 a few objects with a large
d, mode 5 objects with tiny relative speeds, mode 6 a common-velocity
fleet whose only pair to reach distance d is the last two objects."""

import math
import random
import sys

MOST = 500
FAR = 10000
FAST = 100
FEW = 8


def velocity(rng, speed):
    while True:
        v = [rng.uniform(-1, 1) for _ in range(3)]
        norm = math.sqrt(sum(c * c for c in v))
        if norm > 0:
            return [c / norm * speed for c in v]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        # All preceding objects have the same velocity, and their x/y
        # coordinates stay far from the last object's vertical path.
        objs = [
            [-9000 + 500 * (i % 30), -9000 + 500 * (i // 30), 0, 3, 4, 0]
            for i in range(MOST - 2)
        ]
        rng.shuffle(objs)
        speed = rng.randint(1, 20)
        objs.extend([[9000, 9000, -10, 3, 4, 0], [9000, 9000, 10, 3, 4, -speed]])
        print(MOST, 1)
        for o in objs:
            print(*o)
        return
    if mode in (1, 2, 5):
        n = MOST
    elif mode == 3:
        n = rng.randint(2, 40)
    else:
        n = rng.randint(2, FEW)  # few enough to fit far apart in the zone
    d = round(rng.uniform(0.1, 1000), 2) if mode != 4 else round(rng.uniform(1000, FAR / 2), 2)
    objs = []
    while len(objs) < n:
        pos = [round(rng.uniform(-FAR, FAR), 2) for _ in range(3)]
        if mode == 2:
            norm = math.sqrt(sum(c * c for c in pos)) or 1
            vel = [round(c / norm * FAST * 0.99, 2) for c in pos]
        elif mode == 3 and objs and len(objs) % 2 == 1:
            # aim at the previous object's position
            other = objs[-1][:3]
            dirn = [o - p for o, p in zip(other, pos)]
            norm = math.sqrt(sum(c * c for c in dirn)) or 1
            vel = [round(c / norm * rng.uniform(1, FAST * 0.99), 2) for c in dirn]
        elif mode == 5:
            vel = [round(rng.uniform(-0.05, 0.05), 2) for _ in range(3)]
        else:
            vel = [round(c, 2) for c in velocity(rng, rng.uniform(0, FAST * 0.99))]
        if all(math.dist(pos, o[:3]) > d * 1.01 for o in objs):
            objs.append(pos + vel)
    print(n, d)
    for o in objs:
        print(*o)


main()
