"""Random readings: a seed, n, m and a mode. Mode 0 takes random numbers
from 0 to n, mode 1 reads one side of m random cards (always possible),
mode 2 does the same and then changes one number by one, mode 3 reads
the larger number of every chosen card except card 1, which shows 0, mode 4
reads the smaller number of every chosen card and replaces the largest by a
copy of a random one, so with m = n the numbers up to that copy need one
card more than exists."""

import random
import sys


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 0:
        nums = [rng.randint(0, n) for _ in range(m)]
    else:
        cards = rng.sample(range(1, n + 1), m)
        nums = [card - rng.randint(0, 1) for card in cards]
        if mode == 2:
            k = rng.randrange(m)
            nums[k] = min(n, max(0, nums[k] + rng.choice((-1, 1))))
        elif mode == 3:
            nums = [card - (card == 1) for card in cards]
        elif mode == 4:
            nums = [card - 1 for card in cards]
            nums[nums.index(max(nums))] = rng.choice(nums)
    sys.stdout.write("%d %d\n%s\n" % (n, m, " ".join(map(str, nums))))


if __name__ == "__main__":
    main()
