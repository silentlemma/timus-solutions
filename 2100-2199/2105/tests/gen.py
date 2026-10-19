"""A ride from a seed: mode 1 small values, mode 2 the largest values with
10^5 touching feeding intervals, mode 3 a total distance that ends exactly on
a multiple of the length."""

import random
import sys

MAX_L = 10 ** 9
MAX_T = 10 ** 6
MAX_V = 10 ** 3
MAX_N = 10 ** 5
SMALL = 10
SEARCH = 10 ** 4  # divisors tried for an exact end


def intervals(rng, total, count):
    # for each kid, consecutive intervals that may touch but never overlap
    out = []
    for kid in (1, 2):
        t = 0
        for _ in range(count):
            if t > total:
                break
            d = rng.randint(0, max(0, (total - t) // max(1, count)))
            out.append((kid, t, d))
            t += d + rng.randint(0, 1)
    out = [x for x in out if x[1] + x[2] <= total]
    out.sort(key=lambda x: x[1])
    return out


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        length, total = rng.randint(1, SMALL), rng.randint(1, SMALL)
        va, vb = rng.randint(1, SMALL), rng.randint(1, SMALL)
        feed = intervals(rng, total, rng.randint(0, SMALL // 2))
    else:
        length, total = rng.randint(1, MAX_L), MAX_T
        va, vb = MAX_V, rng.randint(1, MAX_V)
        feed = intervals(rng, total, MAX_N // 2)
        if mode == 3:
            rest = [sum(d for k, _, d in feed if k == kid) for kid in (1, 2)]
            ridden = va * (total - rest[0]) + vb * (total - rest[1])
            divisors = [d for d in range(1, SEARCH) if ridden % d == 0 and ridden // d <= MAX_L]
            if not divisors:
                # without feeding the distance is a multiple of 10^6
                feed, ridden = [], (va + vb) * total
                divisors = [d for d in range(1, SEARCH) if ridden % d == 0 and ridden // d <= MAX_L]
            length = ridden // rng.choice(divisors)
    print(length, total, va, vb)
    print(len(feed))
    for kid, t, d in feed:
        print(kid, t, d)


main()
