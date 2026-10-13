import sys

# these bases make Miller-Rabin exact for every n below 3.2 * 10^9
BASES = (2, 3, 5, 7)
SMALLEST_SPLIT = 4  # the smallest even number that is a sum of two primes


def is_prime(n):
    if n < 2:
        return False
    for b in BASES:
        if n % b == 0:
            return n == b
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for b in BASES:
        x = pow(b, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def two_primes(n):
    """An even n >= 4 as the smallest prime p and n - p."""
    p = 2
    while not (is_prime(p) and is_prime(n - p)):
        p += 1
    return [p, n - p]


def split(n):
    if is_prime(n):
        return [n]
    if n % 2 == 0:
        return two_primes(n)
    if is_prime(n - 2):
        return [2, n - 2]
    # the largest prime p that leaves an even rest of at least 4
    p = n - SMALLEST_SPLIT
    while not is_prime(p):
        p -= 2
    return [p] + two_primes(n - p)


def main():
    data = sys.stdin.read().split()
    count = int(data[0]) if data else 0
    out = [" ".join(map(str, split(int(n)))) for n in data[1 : count + 1]]
    print("\n".join(out))


main()
