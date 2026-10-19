from itertools import compress
from math import isqrt

LIMIT = 10 ** 6  # square root of the largest R
CUBE = 3


def main():
    left, right = map(int, input().split())
    composite = bytearray(LIMIT + 1)
    composite[0] = composite[1] = 1
    for i in range(2, isqrt(LIMIT) + 1):
        if not composite[i]:
            composite[i * i::i] = b"\x01" * len(range(i * i, LIMIT + 1, i))
    # the only unsatisfying numbers are p^k, k >= 2, with k + 1 divisors and k + 1 prime.
    # Squares: the primes p with left <= p^2 <= right, counted on a slice of the sieve
    low, high = isqrt(left - 1) + 1, isqrt(right)
    bad = max(0, high - low + 1 - sum(composite[low:high + 1]))
    # higher powers need p^3 <= right, so few primes remain
    cube_root = round(right ** (1 / CUBE)) + 1
    for p in compress(range(cube_root + 1), (not c for c in composite[:cube_root + 1])):
        power, k = p ** CUBE, CUBE
        while power <= right:
            if power >= left and not composite[k + 1]:
                bad += 1
            power *= p
            k += 1
    print(right - left + 1 - bad)


main()
