import sys

WITNESSES = (2, 3, 5, 7)  # enough for a deterministic test below 3.2 * 10^9
DEPTH = 10000


def is_prime(n):
    """Miller-Rabin with fixed witnesses, exact for these sizes."""
    if n < 2:
        return False
    for p in WITNESSES:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in WITNESSES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def divisors(k):
    found = [1]
    p = 2
    while p * p <= k:
        if k % p == 0:
            power, size = 1, len(found)
            while k % p == 0:
                k //= p
                power *= p
                found += [x * power for x in found[:size]]
        p += 1
    if k > 1:
        found += [x * k for x in found]
    return sorted(found)


def main():
    k = int(sys.stdin.read())
    # student j is admitted exactly when gcd(j, N) = 1, so K = phi(N). With
    # N = p1^e1 ... pr^er, phi(N) is the product of (p - 1) p^(e - 1), so
    # every p - 1 divides K: the candidate primes are the d + 1 for d | K
    divs = divisors(k)
    primes = [d + 1 for d in divs if is_prime(d + 1)]
    memo = {}

    def least(rest, start):
        """The smallest product of powers of primes[start:] whose totient is
        rest, or 0 if there is none."""
        if rest == 1:
            return 1
        key = (rest, start)
        if key in memo:
            return memo[key]
        best = 0
        for i in range(start, len(primes)):
            p = primes[i]
            if p - 1 > rest:
                break
            if rest % (p - 1):
                continue
            part, power = rest // (p - 1), p
            while True:
                sub = least(part, i + 1)
                if sub and (best == 0 or power * sub < best):
                    best = power * sub
                if part % p:
                    break
                part //= p
                power *= p
        memo[key] = best
        return best

    sys.setrecursionlimit(DEPTH)
    print(least(k, 0))


main()
