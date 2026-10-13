"""Students waking up: a seed and a mode. Mode 1 gives up to 500 random
moments of the day, mode 2 all 500 within a few minutes before
midnight, so the queue runs through the next day, mode 3 small gaps
around the boiling time of one portion."""

import random
import sys

LIMIT = 500
DAY = 24 * 60 * 60


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        moments = rng.sample(range(DAY), LIMIT)
    elif mode == 2:
        moments = rng.sample(range(DAY - 600, DAY), LIMIT)
    else:
        moments, t = [], rng.randint(0, 3600)
        while len(moments) < LIMIT and t < DAY:
            moments.append(t)
            t += rng.choice((1, 60, 167, 168, 335, 336, 838))
    moments.sort()
    print(len(moments))
    for t in moments:
        print("%02d:%02d:%02d" % (t // 3600, t // 60 % 60, t % 60))


main()
