"""Events from a seed; the generator follows the total height and Oleg's state, so
Oleg's level is always below the top and fire comes only while he drinks.

Mode 1: a dozen events with small heights and five names. Mode 2: 10^5 events
with many random names and large values. Mode 3: 10^5 events with three names,
frequent straws and fires.
Mode 4: 10^5 events accumulating the largest possible straw height.
Mode 5: 99999 distinct ten-letter names, shuffled pours, then a full drain.
Mode 6: 2500 small random events biased toward boundary straws and dry moments.
Mode 7: 10^5 events with seeded one-millimetre refills exactly at exhaustion.
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


def structured(mode, rng):
    if mode == 4:
        events = ["%d a %d" % (i, BIG_H) for i in range(MAX_N - 1)]
        events.append("%d Oleg %d" % (MAX_T, (MAX_N - 1) * BIG_H - 1))
    elif mode == 5:
        names = []
        for i in range(MAX_N - 1):
            letters = []
            for _ in range(MAX_NAME):
                letters.append(chr(ord("a") + i % 26))
                i //= 26
            names.append("".join(reversed(letters)))
        rng.shuffle(names)
        events = ["%d %s 1" % (i, name) for i, name in enumerate(names)]
        events.append("%d Oleg 0" % (MAX_N - 1))
    elif mode == 7:
        events = ["0 a %d" % BIG_H, "1 Oleg %d" % (BIG_H - 1)]
        events.extend("%d %s 1" % (i, rng.choice(["a", "m", "z"]))
                      for i in range(2, MAX_N))
    else:
        events = []
        t = total = straw = 0
        drinking = False
        names = ["a", "aa", "aaa", "ab", "b", "ba", "z", "zzzzzzzzzz"]
        for _ in range(2500):
            delta = rng.randint(1, 9)
            if drinking and 0 < total - straw <= 20 and rng.random() < 0.4:
                delta = max(1, total - straw + rng.choice([-1, 0, 1]))
            t += delta
            if drinking:
                available = total - straw
                total -= min(delta, available)
                drinking = delta <= available
            r = rng.random()
            if drinking and r < 0.15:
                events.append("%d fire" % t)
                drinking = False
            elif total and r < 0.6:
                straw = rng.choice([0, total - 1, rng.randrange(total)])
                events.append("%d Oleg %d" % (t, straw))
                drinking = True
            else:
                h = rng.randint(1, 7)
                events.append("%d %s %d" % (t, rng.choice(names), h))
                total += h
    print(len(events))
    print("\n".join(events))


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode in (4, 5, 6, 7):
        structured(mode, rng)
        return
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
