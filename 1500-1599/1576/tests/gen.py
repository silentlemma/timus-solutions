"""One test from a seed and a mode: three tariffs and a list of calls.
Mode 1 has 1000 calls of any length, mode 2 many calls near the six
second and minute boundaries, mode 3 a few calls, mode 4 has 1000
sub-minute calls one paid minute below the allowance, and mode 5 has
1000 positive whole-minute calls."""

import random
import sys

TOP = 1000
CALLS = 1000
FEW = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        seconds = [rng.randrange(60) for _ in range(CALLS)]
        seconds[:3] = [0, 6, 7]
        rng.shuffle(seconds)
        print(rng.randint(1, TOP), rng.randint(1, TOP))
        print(rng.randint(1, TOP), sum(s > 6 for s in seconds) + 1, rng.randint(1, TOP))
        print(rng.randint(1, TOP))
        print(CALLS)
        for ss in seconds:
            print("00:%02d" % ss)
        return
    if mode == 5:
        print(rng.randint(1, TOP), rng.randint(1, TOP))
        print(rng.randint(1, TOP), rng.randint(1, TOP), rng.randint(1, TOP))
        print(rng.randint(1, TOP))
        print(CALLS)
        for _ in range(CALLS):
            print("%02d:00" % rng.randint(1, 59))
        return
    print(rng.randint(1, TOP), rng.randint(1, TOP))
    print(rng.randint(1, TOP), rng.randint(1, TOP), rng.randint(1, TOP))
    print(rng.randint(1, TOP))
    k = rng.randint(1, FEW) if mode == 3 else CALLS
    print(k)
    for _ in range(k):
        if mode == 2:
            mm = rng.choice([0, 0, rng.randint(0, 59)])
            ss = rng.choice([0, 1, 5, 6, 7, 59])
        else:
            mm, ss = rng.randint(0, 59), rng.randint(0, 59)
        print("%02d:%02d" % (mm, ss))


main()
