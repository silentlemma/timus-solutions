"""Checker: the output is a 12-digit number, written with leading zeros
if needed, that starts with the given digits and has no divisors other
than 1 and itself."""

import sys

DIGITS = 12


def no_divisors(n):
    """True for 1 and the primes, by trial division up to the root."""
    if n < 2:
        return n == 1
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    words = open(inp).read().split()
    prefix = "".join(words[1:])[: int(words[0])]
    got = open(output).read().split()
    if len(got) != 1 or len(got[0]) != DIGITS or not got[0].isdigit():
        fail("expected one number of 12 digits")
    if not got[0].startswith(prefix):
        fail("%s does not start with %s" % (got[0], prefix))
    if not no_divisors(int(got[0])):
        fail("%s has a divisor" % got[0])


if __name__ == "__main__":
    main()
