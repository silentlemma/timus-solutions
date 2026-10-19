import sys
from math import isqrt

MOD = 10 ** 9 + 7


def main():
    n = int(sys.stdin.read())
    # F_n is the product of k^fib(n - k + 1) over k from 1 to n, with
    # fib(1) = fib(2) = 1; weight[k] = fib(n - k + 1) modulo MOD
    fib = [0, 1] + [0] * n
    for i in range(2, n + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD
    weight = fib[n + 1:0:-1]
    sieve = bytearray([1]) * (n + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytes(len(range(p * p, n + 1, p)))
    # the exponent of a prime p sums the weights of the multiples of p, of
    # p^2, and so on; the divisors number the product of exponents plus 1
    answer = 1
    for p in range(2, n + 1):
        if sieve[p]:
            power, exponent = p, 0
            while power <= n:
                exponent += sum(weight[power::power])
                power *= p
            answer = answer * ((exponent + 1) % MOD) % MOD
    print(answer)


main()
