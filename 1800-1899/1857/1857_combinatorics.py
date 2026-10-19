import sys


def main():
    a, n = map(int, sys.stdin.read().split())
    primes, rest, p = [], n, 2
    while p * p <= rest:
        if rest % p == 0:
            primes.append(p)
            while rest % p == 0:
                rest //= p
        p += 1
    if rest > 1:
        primes.append(rest)
    # keys up to rotation without a shorter period are Lyndon words: by
    # Moebius inversion n times their number is the sum over square-free
    # divisors d of n of mu(d) a^(n / d)
    total = 0
    for mask in range(1 << len(primes)):
        d, sign = 1, 1
        for i, p in enumerate(primes):
            if mask >> i & 1:
                d *= p
                sign = -sign
        total += sign * a ** (n // d)
    # the answer has up to 14 000 digits, past the default limit of str()
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    print(total // n)


main()
