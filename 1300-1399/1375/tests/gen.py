"""Deterministic random residues modulo a randomly selected prime.

random SEED LOW HIGH REMAINDER: choose a prime p in the inclusive interval
[LOW, HIGH] with p % 4 == REMAINDER (1 or 3), then choose k uniformly in
[1, p - 2]. The nonzero interior avoids the separately stored border cases.
"""

from math import isqrt
import random
import sys


def main():
    if len(sys.argv) != 6 or sys.argv[1] != "random":
        raise ValueError("usage: gen.py random SEED LOW HIGH REMAINDER")
    seed, low, high, remainder = map(int, sys.argv[2:])
    if not (3 <= low <= high <= 10**6 and remainder in (1, 3)):
        raise ValueError("invalid prime interval or remainder")
    primes = [p for p in range(low, high + 1) if p % 4 == remainder
              and all(p % d for d in range(2, isqrt(p) + 1))]
    if not primes:
        raise ValueError("interval contains no suitable prime")
    rng = random.Random(seed)
    p = rng.choice(primes)
    print(rng.randrange(1, p - 1), p)


if __name__ == "__main__":
    main()
