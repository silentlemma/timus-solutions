"""Events from a seed; the generator follows the total height and Oleg's state, so
Oleg's level is always below the top and fire comes only while he drinks.

Mode 1: a dozen events with small heights and five names. Mode 2: 10^5 events
with many random names and large values. Mode 3: 10^5 events with three names,
frequent straws and fires.
"""

import random
import string
import sys

SMALL_N = 12
MAX_N = 10 ** 5
MAX_T = 10 ** 9
MAX_NAME = 10
BIG_H = 10 ** 9
SMALL_H = 4
FEW_NAMES = ["a", "b", "c", "ab", "z"]
THREE_NAMES = ["gin", "kahlua", "rum"]
MANY_NAMES = 2000


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n, names, top_h, step = SMALL_N, FEW_NAMES, SMALL_H, SMALL_H
        p_oleg, p_fire = 0.3, 0.3
    elif mode == 2:
        n, top_h, step = MAX_N, BIG_H, MAX_T // MAX_N
        names = ["".join(rng.choice(string.ascii_lowercase)
                         for _ in range(rng.randint(1, MAX_NAME))) for _ in range(MANY_NAMES)]
        names = [s for s in names if s != "fire"]
        p_oleg, p_fire = 0.1, 0.05
    else:
        n, names, top_h, step = MAX_N, THREE_NAMES, SMALL_H, SMALL_H
        p_oleg, p_fire = 0.3, 0.2
    t, total, straw, drinking = 0, 0, 0, False
    events = []
    for _ in range(n):
        t += rng.randint(1, step)
        if drinking:
            # he drinks until t or until the level reaches the straw
            gone = min(t - clock, total - straw)
            total -= gone
            drinking = clock + gone == t
        clock = t
        r = rng.random()
        if drinking and r < p_fire:
            events.append("%d fire" % t)
            drinking = False
        elif total > 0 and r < p_fire + p_oleg:
            straw = rng.randrange(total)
            events.append("%d Oleg %d" % (t, straw))
            drinking = True
        else:
            h = rng.randint(1, top_h)
            events.append("%d %s %d" % (t, rng.choice(names), h))
            total += h
    print(len(events))
    print("\n".join(events))


main()
