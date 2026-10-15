"""One test from a seed and a mode: mode 1 any K, mode 2 an even K with
many divisors, mode 3 the totient of a random N (so an answer exists),
mode 4 a small K."""

import random
import sys

TOP = 2 * 10 ** 9


def phi(n):
    result, p = n, 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k = rng.randint(1, TOP)
    elif mode == 2:
        k = 1
        while True:
            q = rng.choice((2, 2, 2, 3, 3, 5, 7, 11, 13))
            if k * q > TOP:
                break
            k *= q
    elif mode == 3:
        while True:
            k = phi(rng.randint(1, 3 * 10 ** 9))
            if k <= TOP:
                break
    else:
        k = rng.randint(1, 1000)
    print(k)


main()
