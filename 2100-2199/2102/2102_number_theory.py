TARGET = 20
BOUND = 2 * 10 ** 6  # trial divisors; beyond them at most two prime factors remain


def main():
    n = int(input())
    count = 0
    d = 2
    while d <= BOUND and d * d <= n:
        while n % d == 0:
            n //= d
            count += 1
        d += 1
    if n > 1:
        if d * d > n:
            count += 1  # what is left is prime
        else:
            # n >= BOUND^2 here, so the divided part is at most 10^18 / BOUND^2,
            # fewer than 18 factors, and the rest adds at most two
            count = -1
    print("Yes" if count == TARGET else "No")


main()
