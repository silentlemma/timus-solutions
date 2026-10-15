"""One test from a seed and a mode: the encoder of the statement with a
random zero level, amplitude and noise, every sample kept in [0, 1] with
five decimals. Mode 1 a short text, mode 2 the longest text with t = 5,
mode 3 a long t, mode 4 strong noise."""

import math
import random
import string
import sys

MOST_N = 10000
BITS = 8
ALPHABET = string.ascii_letters + string.digits + " .,!?-:;'\"()"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        t = rng.randint(5, 20)
        size = rng.randint(1, 10)
    elif mode == 2:
        t = 5
        size = MOST_N // (BITS * t)
    elif mode == 3:
        t = rng.choice((500, 625, 1000))
        size = MOST_N // (BITS * t)
    else:
        t = rng.randint(5, 50)
        size = MOST_N // (BITS * t)
    text = "".join(rng.choice(ALPHABET) for _ in range(size))
    amp = rng.uniform(0.2, 0.45)
    level = rng.uniform(amp + 0.05, 1 - amp - 0.05)
    noise = amp * (0.6 if mode == 4 else 0.25)
    samples = []
    for c in text:
        for j in range(BITS):
            for k in range(t):
                wave = 2 if ord(c) >> j & 1 else 4
                x = level + math.sin(wave * k * math.pi / t) * amp + rng.uniform(-noise, noise)
                samples.append(min(1.0, max(0.0, round(x, 5))))
    print(len(samples), t)
    for start in range(0, len(samples), t):
        print(" ".join("%.5f" % x for x in samples[start:start + t]))


main()
