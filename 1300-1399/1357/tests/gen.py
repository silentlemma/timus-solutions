"""Students waking up: a seed and a mode.

Mode 1: 500 random moments of the day.
Mode 2: 500 moments in the last ten minutes, queuing into the next day.
Mode 3: small gaps around the boiling time of one portion.
Mode 4: 500 separate kettles, with random gaps of 168 to 172 seconds.
Mode 5: two random 250-student rushes in the first and last hours,
        separated by enough idle time to empty the queue completely.
"""

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
    elif mode == 4:
        moments, t = [], rng.randrange(100)
        for _ in range(LIMIT):
            moments.append(t)
            t += rng.randint(168, 172)
    elif mode == 5:
        moments = rng.sample(range(3600), LIMIT // 2)
        moments += rng.sample(range(DAY - 3600, DAY), LIMIT // 2)
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
