"""One test from a seed and a mode: three odds from 0.01 to 100. Mode 1
draws them with two decimals, mode 2 with one, mode 3 near the extremes."""

import random
import sys

LOW, HIGH = 1, 10000  # in hundredths


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    odds = []
    for _ in range(3):
        if mode == 3:
            cents = rng.choice([LOW, LOW + 1, HIGH - 1, HIGH, rng.randint(LOW, HIGH)])
        elif mode == 2:
            cents = rng.randint(1, HIGH // 10) * 10
        else:
            cents = rng.randint(LOW, HIGH)
        odds.append("%d.%02d" % divmod(cents, 100))
    print(" ".join(odds))


main()
