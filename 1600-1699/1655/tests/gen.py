"""One test from a seed and a mode: mode 1 a few ships, mode 2 500 ships
with generous distances, mode 3 500 ships that are barely reachable in
time, mode 4 ships straight ahead of the gun among others. Mode 5: 500
equally spaced ships at minimum gun speed. Mode 6: 500 tightly clustered
ships opposite the start, at maximum approach speed. Mode 7: 500 ships
with one off-axis ship already at one mile. Mode 8: seven random ships
with deadlines near their direct travel times. Mode 9: 500 ships with
successive exact deadlines along a semicircle, in shuffled input order."""

import random
import sys

MOST = 500
FULL = 360000  # thousandths of a degree


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode >= 5:
        extended(rng, mode)
        return
    n = rng.randint(1, 6) if mode == 1 else MOST
    a = rng.randrange(FULL)
    w = rng.randint(10, 1000)  # thousandths of a turn a minute
    azimuths = rng.sample(range(FULL), n)
    if mode == 4:
        azimuths[0] = a
    print("%.3f %.3f %d" % (a / 1000, w / 1000, n))
    for b in azimuths:
        if mode == 3:
            d = rng.randint(50000, 200000)
            v = rng.randint(5000, 100000)
        else:
            d = rng.randint(1000, 1000000)
            v = rng.randint(10, 100000)
        print("%.3f %.3f %.3f" % (b / 1000, d / 1000, v / 1000))


def extended(rng, mode):
    a = rng.randrange(FULL)
    if mode == 5:
        w = 10
        rows = [((a + 360 + 720 * k) % FULL, 1000000, 10) for k in range(MOST)]
    elif mode == 6:
        w = 1000
        offsets = rng.sample(range(-1000, 1001), MOST)
        rows = [((a + FULL // 2 + x) % FULL, 1000000, 100000) for x in offsets]
    elif mode == 7:
        w = 10
        azimuths = rng.sample(range(FULL - 1), MOST)
        azimuths = [b + (b >= a) for b in azimuths]
        urgent = rng.randrange(MOST)
        rows = [(b, 1000 if k == urgent else 1000000, 10)
                for k, b in enumerate(azimuths)]
    elif mode == 8:
        w = 125
        azimuths = rng.sample(range(FULL), 7)
        rows = []
        for b in azimuths:
            delta = min((b - a) % FULL, (a - b) % FULL)
            direct = delta / (360 * w)
            distance = round(1000 * (1 + direct * rng.uniform(0.9, 2.5)))
            rows.append((b, distance, 60000))
    elif mode == 9:
        w = 10
        direction = rng.choice((-1, 1))
        rows = [((a + direction * 360 * k) % FULL, 1000 + 100 * k, 60000)
                for k in range(1, MOST + 1)]
    else:
        raise ValueError('unknown mode')
    rng.shuffle(rows)
    print('%.3f %.3f %d' % (a / 1000, w / 1000, len(rows)))
    for b, d, v in rows:
        print('%.3f %.3f %.3f' % (b / 1000, d / 1000, v / 1000))


main()
