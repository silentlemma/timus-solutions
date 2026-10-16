"""One test from a seed and a mode: mode 1 100 numbers up to 10^18,
mode 2 100 numbers up to 10^6, mode 3 100 numbers just below and at
record holders, the smallest numbers with more divisors than any
smaller number; mode 4 100 numbers sampled across bit lengths 1..60."""

import random
import sys

LIMIT = 10 ** 18
SMALL = 10 ** 6
TESTS = 100
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)


def records():
    found = []
    stack = [(0, 64, 1, 1)]
    while stack:
        index, cap, value, divisors = stack.pop()
        found.append((value, divisors))
        if index < len(PRIMES):
            for e in range(1, cap + 1):
                if value > LIMIT // PRIMES[index]:
                    break
                value *= PRIMES[index]
                stack.append((index + 1, e, value, divisors * (e + 1)))
    found.sort()
    out, top = [], 0
    for value, divisors in found:
        if divisors > top:
            top = divisors
            out.append(value)
    return out


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 3:
        pool = records()
        numbers = []
        for _ in range(TESTS // 2):
            r = rng.choice(pool)
            numbers += [max(1, r - 1), r]
    elif mode == 4:
        numbers = []
        for _ in range(TESTS):
            bits = rng.randint(1, LIMIT.bit_length())
            numbers.append(rng.randint(2 ** (bits - 1), min(LIMIT, 2 ** bits - 1)))
    else:
        top = LIMIT if mode == 1 else SMALL
        numbers = [rng.randint(1, top) for _ in range(TESTS)]
    print(len(numbers))
    print("\n".join(map(str, numbers)))


main()
