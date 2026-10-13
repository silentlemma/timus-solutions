"""Checker: every line holds primes that add up to its N, and there are
as few of them as possible: one for a prime, two for an even N or when
N - 2 is prime, three otherwise."""

import sys


def is_prime(n):
    """Trial division up to the root."""
    if n < 2:
        return False
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


def fewest(n):
    if is_prime(n):
        return 1
    return 2 if n % 2 == 0 or is_prime(n - 2) else 3


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    words = open(inp).read().split()
    numbers = [int(w) for w in words[1 : int(words[0]) + 1]]
    lines = [line.split() for line in open(output).read().splitlines() if line.strip()]
    if len(lines) != len(numbers):
        fail("expected %d lines, got %d" % (len(numbers), len(lines)))
    for n, line in zip(numbers, lines):
        if not all(w.isdigit() for w in line):
            fail("not a list of numbers for %d" % n)
        parts = [int(w) for w in line]
        if sum(parts) != n:
            fail("%s does not add up to %d" % (" ".join(line), n))
        bad = [p for p in parts if not is_prime(p)]
        if bad:
            fail("%d is not prime" % bad[0])
        if len(parts) != fewest(n):
            fail("%d primes for %d, %d is enough" % (len(parts), n, fewest(n)))


if __name__ == "__main__":
    main()
