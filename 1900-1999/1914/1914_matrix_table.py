"""Print the table PRIMES of the solutions: the 35 smallest primes above 10^9.

Each of them lies strictly between 2^29 and 2^30, as the solutions need.
"""

COUNT = 35
START = 10**9


def is_prime(x):
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True


def main():
    primes = []
    x = START + 1
    while len(primes) < COUNT:
        if is_prime(x):
            primes.append(x)
        x += 1
    assert 1 << 29 < primes[0] and primes[-1] < 1 << 30
    print(", ".join(map(str, primes)))


main()
