import sys
from array import array
from math import gcd, isqrt


FIRST_ODD_PRIME = 3


def smallest_factors(limit):
    root = isqrt(limit)
    prime = bytearray(b"\1") * (root + 1)
    primes = []
    for value in range(FIRST_ODD_PRIME, root + 1, 2):
        if prime[value]:
            primes.append(value)
            start = value * value
            if start <= root:
                prime[start::value] = b"\0" * ((root - start) // value + 1)

    factors = array("H", [0]) * ((limit + 1) // 2)
    # Descending primes let slice assignments leave the smallest divisor in each slot.
    for value in reversed(primes):
        start = value * value // 2
        count = (len(factors) - 1 - start) // value + 1
        factors[start::value] = array("H", [value]) * count
    return factors


def largest_factor(value, factors):
    if value % 2 == 0:
        value //= value & -value
        if value == 1:
            return 2
    while factors[value // 2]:
        value //= factors[value // 2]
    return value


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    factors = smallest_factors(max(data[1:]))
    pairs = iter(data)
    next(pairs)
    output = []
    for a, b in zip(pairs, pairs):
        common = gcd(a, b)
        if common != 1 and a != b:
            # Shared factors survive exactly when they are at least this threshold.
            threshold = max(
                largest_factor(a // common, factors), largest_factor(b // common, factors)
            )
            if threshold > 2:
                common //= common & -common
            while common > 1:
                prime = 2 if common % 2 == 0 else factors[common // 2] or common
                if prime >= threshold:
                    break
                common //= prime
        output.append(str(common))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
