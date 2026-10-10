"""One query on a Fibonacci-like sequence whose terms between the smallest
and largest index stay within 2e9: a seed and a mode. Mode 0 starts from
two small random terms, mode 1 from 0 and 1, which gives the longest
window of nonzero terms, mode 2 takes the zero sequence with far indices,
mode 3 puts n outside the two given indices."""

import random
import sys

BOUND = 2 * 10**9
INDEX = 1000
SMALL = 50


def window(f0, f1):
    # terms by index, as far both ways from 0 and 1 as the bound allows
    terms = {0: f0, 1: f1}
    k = 1
    while abs(terms[k] + terms[k - 1]) <= BOUND and k < 2 * INDEX:
        terms[k + 1] = terms[k] + terms[k - 1]
        k += 1
    k = 0
    while abs(terms[k + 1] - terms[k]) <= BOUND and k > -2 * INDEX:
        terms[k - 1] = terms[k + 1] - terms[k]
        k -= 1
    return terms


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        terms = window(0, 1)
    elif mode == 2:
        terms = window(0, 0)
    else:
        terms = window(rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL))
    lo, hi = min(terms), max(terms)
    width = hi - lo
    if width > 2 * INDEX:
        lo, hi = -INDEX, INDEX
    shift = rng.randint(-INDEX - lo, INDEX - hi) if width <= 2 * INDEX else 0
    if mode == 1:
        i, j = hi, lo
        n = rng.randint(lo, hi)
    elif mode == 3:
        i, j = sorted(rng.sample(range(lo + 1, hi), 2))
        n = rng.choice([rng.randint(lo, i), rng.randint(j, hi)])
        if rng.random() < 1 / 2:
            i, j = j, i
    else:
        i, j = rng.sample(range(lo, hi + 1), 2)
        n = rng.randint(lo, hi)
    line = (i + shift, terms[i], j + shift, terms[j], n + shift)
    sys.stdout.write("%d %d %d %d %d\n" % line)


if __name__ == "__main__":
    main()
