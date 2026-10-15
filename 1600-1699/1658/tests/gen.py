"""One test from a seed and a mode.

Mode 1: a few queries from random numbers of up to 100 digits.
Mode 2: 10000 queries from random numbers of up to 100 digits.
Mode 3: 10000 queries anywhere in the input range (mostly impossible).
Mode 4: 10000 distinct random pairs with 1 <= s1 <= 60 and s1 <= s2 <= 9*s1,
concentrating on small reachable states and holes inside the feasible bounds.
"""

import random
import sys

MOST = 10000
LONGEST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    t = rng.randint(1, 10) if mode == 1 else MOST
    print(t)
    if mode == 4:
        pairs = [(s1, s2) for s1 in range(1, 61) for s2 in range(s1, 9 * s1 + 1)]
        for s1, s2 in rng.sample(pairs, t):
            print(s1, s2)
        return
    for _ in range(t):
        if mode == 3:
            print(rng.randint(1, MOST), rng.randint(1, MOST))
        else:
            digits = [rng.randint(0, 9) for _ in range(rng.randint(1, LONGEST))]
            s1 = sum(digits) or 1
            s2 = sum(d * d for d in digits) or 1
            print(s1, s2)


main()
