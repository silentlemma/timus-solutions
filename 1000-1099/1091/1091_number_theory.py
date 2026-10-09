from math import comb

CAPACITY = 10000


def main():
    k, s = map(int, input().split())
    # Moebius function by a sieve: -1 per prime factor, 0 with a square factor
    mu = [1] * (s + 1)
    prime = [True] * (s + 1)
    for p in range(2, s + 1):
        if prime[p]:
            for m in range(p, s + 1, p):
                prime[m] = m == p
                mu[m] = -mu[m]
            for m in range(p * p, s + 1, p * p):
                mu[m] = 0
    # inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
    total = sum(-mu[d] * comb(s // d, k) for d in range(2, s + 1))
    print(min(total, CAPACITY))


main()
