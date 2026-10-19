"""Check arbitrary sequences by prime factorization; verify Impossible by independent search."""

from array import array
from math import isqrt
from pathlib import Path
import re
import sys

MIN_LENGTH = 2
MAX_LENGTH = 100000
MAX_TERM = 300
INITIAL_FACTOR = 16
MIN_SEARCH = 64


def primes_up_to(bound):
    sieve = bytearray(b"\1") * (bound + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(bound) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b"\0" * ((bound - p * p) // p + 1)
    return [p for p in range(2, bound + 1) if sieve[p]]


def divisor_count(value, primes):
    result = 1
    for p in primes:
        if p * p > value:
            break
        exponent = 0
        while value % p == 0:
            value //= p
            exponent += 1
        result *= exponent + 1
    return result * (2 if value > 1 else 1)


def exists(n):
    cap = MAX_TERM * n
    bound = min(cap, max(MIN_SEARCH, INITIAL_FACTOR * n))
    while True:
        divisors = array("H", [0]) * (bound + 1)
        for d in range(1, bound + 1):
            for multiple in range(d, bound + 1, d):
                divisors[multiple] += 1
        depth = array("I", [0]) * (bound + 1)
        for total in range(1, bound + 1):
            term = divisors[total]
            current = int(total <= MAX_TERM)
            if term <= MAX_TERM and total > term and depth[total - term]:
                current = max(current, depth[total - term] + 1)
            depth[total] = current
            if current >= n:
                return True
        if bound == cap:
            return False
        bound = min(cap, bound * 2)


def validate(n, raw):
    if not MIN_LENGTH <= n <= MAX_LENGTH:
        return False
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if tokens == ["Impossible"]:
        return not exists(n)
    if len(tokens) != n or any(re.fullmatch(r"[0-9]+", word) is None for word in tokens):
        return False
    try:
        values = list(map(int, tokens))
    except ValueError:
        return False
    if not all(1 <= value <= MAX_TERM for value in values):
        return False
    primes = primes_up_to(isqrt(sum(values)))
    total = values[0]
    for value in values[1:]:
        total += value
        if divisor_count(total, primes) != value:
            return False
    return True


def main():
    n = int(Path(sys.argv[1]).read_text(encoding="ascii"))
    if not validate(n, Path(sys.argv[3]).read_bytes()):
        print("Wrong length, term range, prefix divisor count, or Impossible claim")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
