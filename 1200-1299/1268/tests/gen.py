"""T primes: a seed and a mode. Mode 1 draws any primes below 65536,
mode 2 primes p with p - 1 having many small factors, where the search
for a primitive root takes longest."""

import random
import sys

LIMIT = 1 << 16
TESTS = 6553


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    primes = [p for p in range(3, LIMIT) if all(p % d for d in range(2, int(p**0.5) + 1))]
    if mode == 2:
        primes = [p for p in primes if (p - 1) % 30 == 0]
    t = rng.randint(1, TESTS)
    chosen = [rng.choice(primes) for _ in range(t)]
    sys.stdout.write("%d\n%s\n" % (t, "\n".join(map(str, chosen))))


if __name__ == "__main__":
    main()
