"""One stalk from a seed and a mode: mode 1 a short stalk with a few
supports, mode 2 the longest stalk with the most random supports, mode
3 the longest stalk with supports packed near the middle, mode 4 the
longest stalk with two supports at the ends, mode 5 every integer position
on the shortest stalk admitting the maximum support count, mode 6 the
longest stalk with random supports in two separated quarter-point bands
and one support near each end."""

import random
import sys

LIMIT = 10 ** 9
MOST = 100000
SMALL = 30


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        if mode == 1:
            length = rng.randint(3, SMALL)
            supports = rng.sample(range(1, length), rng.randint(2, min(8, length - 1)))
        elif mode == 3:
            length = LIMIT
            middle = length // 2
            supports = rng.sample(range(middle - MOST, middle + MOST), MOST)
        elif mode == 4:
            length = LIMIT
            supports = [1, length - 1]
        elif mode == 5:
            length = MOST + 1
            supports = list(range(1, length))
        elif mode == 6:
            length = LIMIT
            half = (MOST - 2) // 2
            quarter = length // 4
            supports = [1, length - 1]
            supports += rng.sample(range(quarter - MOST, quarter + MOST), half)
            supports += rng.sample(range(3 * quarter - MOST, 3 * quarter + MOST), half)
        else:
            length = LIMIT - rng.randint(0, 1000)
            supports = rng.sample(range(1, length), MOST)
        supports.sort()
        # the whole stalk must stand: its centre between the outer supports
        if 2 * supports[0] <= length <= 2 * supports[-1]:
            break
    print(length, len(supports))
    print(*supports)


main()
