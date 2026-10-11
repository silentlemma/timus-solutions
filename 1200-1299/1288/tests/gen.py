"""A signal: a seed and a mode. Mode 1 draws a short signal with walls,
low values and peaks in random places, mode 2 up to 10000 numbers,
mode 3 values near the thresholds 35 and 95 with a large attenuation."""

import random
import sys

COUNT = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(4, 30) if mode == 1 else rng.randint(4, COUNT)
    if mode == 3:
        pool = [33, 34, 35, 36, 60, 90, 93, 94, 95, 96]
    else:
        pool = list(range(101))
    signal = [
        rng.choice(pool) if rng.random() < 0.7 else rng.choice([0, 10, 35, 95, 100])
        for _ in range(n)
    ]
    d = rng.randint(1, max(1, min(n - 1, 12 if mode == 1 else n // 3)))
    zones = []
    for _ in range(2):
        s = rng.randint(1, n - 1)
        e = rng.randint(s, min(n - 1, s + (6 if mode == 1 else 200)))
        zones += [s, e, rng.randint(1, 100)]
    a = rng.choice([0, rng.randint(0, 100)]) if mode != 3 else rng.randint(50, 100)
    head = "%d %d %s %s.%03d" % (n, d, " ".join(map(str, zones)), "0", a)
    sys.stdout.write(head + "\n" + "\n".join(map(str, signal)) + "\n")


if __name__ == "__main__":
    main()
