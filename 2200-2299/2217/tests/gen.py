"""Generate one deterministic input: python gen.py MODE SEED, modes 1 through 10."""

import random
import sys

MAX_SIZE = 100_000
SMALL_SIZE = 64
MODE_COUNT = 10
TRANSFORMATIONS = 10
SMALL, RANDOM, MAX_RANDOM, UNIFORM, PALINDROME, REACHABLE, PARITY, LATE, TIGHT, BLOCKS = range(
    1, MODE_COUNT + 1
)


def main():
    mode, seed = map(int, sys.argv[1:])
    if not SMALL <= mode <= BLOCKS:
        raise SystemExit("mode must be between 1 and 10")
    rng = random.Random(seed)
    n = MAX_SIZE
    if mode == SMALL:
        n = rng.randint(1, SMALL_SIZE)
    elif mode == RANDOM:
        n = rng.randint(1, MAX_SIZE)
    elif mode in (PALINDROME, REACHABLE):
        n -= seed % 2

    if mode in (SMALL, RANDOM, MAX_RANDOM):
        s = "".join(rng.choice("01") for _ in range(n))
    elif mode == UNIFORM:
        s = str(seed % 2) * n
    elif mode in (PALINDROME, REACHABLE):
        half = "".join(rng.choice("01") for _ in range(n // 2))
        center = rng.choice("01") if n % 2 else ""
        s = half + center + half[::-1]
        if mode == REACHABLE:
            # Descending sorts reverse legal adjacent swaps, preserving a route back.
            for _ in range(TRANSFORMATIONS):
                left = rng.randrange(n)
                right = rng.randrange(left + 1, n + 1)
                zeros = s.count("0", left, right)
                block = "1" * (right - left - zeros) + "0" * zeros
                s = s[:left] + block + s[right:]
    elif mode == PARITY:
        position = rng.randrange(n)
        s = "0" * position + "1" + "0" * (n - position - 1)
    elif mode == LATE:
        # The penultimate prefix fails, but the two halves have equal zero counts.
        s = ["1"] * n
        s[n // 2 - 2] = "0"
        s[n // 2] = "0"
        s = "".join(s)
    elif mode == TIGHT:
        s = "10" * (n // 2)
    else:
        zeros = 2 * rng.randrange(n // 2 + 1)
        s = "0" * zeros + "1" * (n - zeros)
        if seed % 2:
            s = s[::-1]

    sys.stdout.write(f"{n}\n{s}\n")


if __name__ == "__main__":
    main()
