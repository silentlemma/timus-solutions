import sys

FIRST_ODD = 3  # the smallest divisor worth trying


def paid(n):
    """Whether n is a product of an odd number of factors, each 2 or an odd
    number above 1: n = 2^twos * rest with rest odd."""
    twos = 0
    while n % 2 == 0:
        n //= 2
        twos += 1
    if n == 1:
        return twos % 2 == 1
    if twos % 2 == 0:
        return True  # rest as a single factor
    # an odd count needs rest split into two factors, so not a prime
    d = FIRST_ODD
    while d * d <= n:
        if n % d == 0:
            return True
        d += 2
    return False


def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    print("\n".join("YES" if paid(int(w)) else "NO" for w in data[1:1 + t]))


main()
