"""One test from a seed and a mode: mode 1 small numbers, mode 2 the
largest numbers, mode 3 heavy flows at slow speeds (the green time is
tight), mode 4 all flows equal."""

import random
import sys

FLOWS = 12
MOST = 1000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        cars = [rng.randint(0, 20) for _ in range(FLOWS)]
        speed = [rng.randint(1, 5) for _ in range(FLOWS)]
    elif mode == 2:
        cars = [rng.randint(0, MOST) for _ in range(FLOWS)]
        speed = [rng.randint(1, MOST) for _ in range(FLOWS)]
    elif mode == 3:
        cars = [rng.randint(MOST // 2, MOST) for _ in range(FLOWS)]
        speed = [rng.randint(40, 120) for _ in range(FLOWS)]
    else:
        value, rate = rng.randint(0, MOST), rng.randint(1, MOST)
        cars, speed = [value] * FLOWS, [rate] * FLOWS
    print(*cars)
    print(*speed)


main()
