"""RSA queries: a seed, K and a mode. Each picks distinct odd primes p, q
with n = p q at most 32000, an exponent e below (p - 1)(q - 1) and coprime
to it, and c = m^e mod n for a random m. Mode 0 is random, mode 1 uses the
largest n and e, mode 2 the smallest primes, mode 3 adds multiples of n to
c while it stays at most 32000, and lets m share a factor with n; m is never 0."""

import math
import random
import sys

LIMIT = 32000


def odd_primes():
    top = LIMIT // 3 + 1
    return [i for i in range(3, top) if all(i % d for d in range(2, math.isqrt(i) + 1))]


def main():
    seed, k, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    primes = odd_primes()
    pairs = [(p, q) for p in primes for q in primes if p < q and p * q <= LIMIT]
    if mode == 1:
        pairs = sorted(pairs, key=lambda pq: pq[0] * pq[1])[-20:]
    elif mode == 2:
        pairs = [(p, q) for p, q in pairs if q <= 13]
    lines = [str(k)]
    for _ in range(k):
        p, q = rng.choice(pairs)
        n, phi = p * q, (p - 1) * (q - 1)
        top = min(phi - 1, LIMIT)
        while True:
            e = rng.randint(max(1, top - 50), top) if mode == 1 else rng.randint(1, top)
            if math.gcd(e, phi) == 1:
                break
        m = rng.randrange(p, n, p) if mode == 3 and rng.random() < 1 / 2 else rng.randrange(1, n)
        c = pow(m, e, n)
        if mode == 3:
            c += n * rng.randint(0, (LIMIT - c) // n)
        lines.append("%d %d %d" % (e, n, c))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
