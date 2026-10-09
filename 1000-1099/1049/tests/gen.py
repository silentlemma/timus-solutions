"""Ten random numbers: a seed and the mode. random: from 1 to 10000;
primes: random primes; small: from 1 to 30; powers: powers of 2 and 3."""

import random
import sys

LIMIT = 10000
COUNT = 10


def main():
    seed, mode = int(sys.argv[1]), sys.argv[2]
    rng = random.Random(seed)
    if mode == "primes":
        primes = [p for p in range(2, LIMIT + 1) if all(p % q for q in range(2, int(p**0.5) + 1))]
        nums = [rng.choice(primes) for _ in range(COUNT)]
    elif mode == "small":
        nums = [rng.randint(1, 30) for _ in range(COUNT)]
    elif mode == "powers":
        nums = [
            rng.choice([2**k for k in range(14)] + [3**k for k in range(9)]) for _ in range(COUNT)
        ]
    else:
        nums = [rng.randint(1, LIMIT) for _ in range(COUNT)]
    sys.stdout.write("\n".join(map(str, nums)) + "\n")


if __name__ == "__main__":
    main()
