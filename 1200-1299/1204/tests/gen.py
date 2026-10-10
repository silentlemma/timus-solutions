"""Products of two different primes: a seed, the number of tests and a mode.
Mode 1 takes both primes at random, mode 2 one tiny and one huge prime,
mode 3 two primes close to the square root of 10^9,
mode 4 a shuffled repeating pool of small and large products,
mode 5 random small products suitable for exhaustive checking."""

import random
import sys

LIMIT = 10**9


def is_prime(v):
    if v < 2:
        return False
    d = 2
    while d * d <= v:
        if v % d == 0:
            return False
        d += 1
    return True


def prime_near(rng, lo, hi):
    while True:
        v = rng.randint(lo, hi)
        if is_prime(v):
            return v


def main():
    seed, k, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    out = [str(k)]
    if mode == 4:
        pairs = [(2, 3), (3, 7), (5, 11), (7, 13), (101, 103),
                 (1009, 2017), (10007, 10009), (30011, 30013), (67, 14925373)]
        values = [p * q for p, q in pairs]
        values = [values[i % len(values)] for i in range(k)]
        rng.shuffle(values)
        sys.stdout.write("\n".join(out + [str(n) for n in values]) + "\n")
        return
    for _ in range(k):
        while True:
            if mode == 1:
                p = prime_near(rng, 2, 31622)
                q = prime_near(rng, 2, (LIMIT - 1) // p)
            elif mode == 2:
                p = rng.choice([2, 3, 5, 7])
                q = prime_near(rng, (LIMIT - 1) // p - 1000, (LIMIT - 1) // p)
            elif mode == 5:
                p = prime_near(rng, 2, 311)
                q = prime_near(rng, 2, 311)
            else:
                p = prime_near(rng, 31000, 31622)
                q = prime_near(rng, 31000, (LIMIT - 1) // p)
            if p != q:
                break
        out.append(str(p * q))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
