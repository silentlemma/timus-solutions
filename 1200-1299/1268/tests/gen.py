"""T primes: a seed and a mode.

Mode 1 draws any primes below 65536. Mode 2 draws primes p with p - 1
divisible by 30. Mode 3 makes 6553 alternating small and large queries
from two randomly chosen pools, testing nonadjacent cached answers.
Mode 4 repeats a shuffled random sample of small primes in a new order,
allowing exhaustive checks of every candidate K.
"""

import random
import sys

LIMIT = 1 << 16
TESTS = 6553


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    primes = [p for p in range(3, LIMIT) if all(p % d for d in range(2, int(p**0.5) + 1))]
    if mode == 3:
        small = rng.sample([p for p in primes if p < 100], 8)
        large = rng.sample([p for p in primes if p > LIMIT - 1024], 8)
        chosen = [rng.choice(small if i % 2 == 0 else large) for i in range(TESTS)]
        sys.stdout.buffer.write(("%d\n%s\n" % (TESTS, "\n".join(map(str, chosen)))).encode())
        return
    if mode == 4:
        first = rng.sample([p for p in primes if p <= 251], 32)
        second = first[:]
        rng.shuffle(second)
        chosen = first + second
        sys.stdout.buffer.write(("%d\n%s\n" % (len(chosen), "\n".join(map(str, chosen)))).encode())
        return
    if mode == 2:
        primes = [p for p in primes if (p - 1) % 30 == 0]
    t = rng.randint(1, TESTS)
    chosen = [rng.choice(primes) for _ in range(t)]
    sys.stdout.write("%d\n%s\n" % (t, "\n".join(map(str, chosen))))


if __name__ == "__main__":
    main()
