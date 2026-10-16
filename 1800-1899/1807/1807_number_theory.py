import sys
from math import isqrt, log

# the best split of a prime p < 31623 never uses a prime above 700
BOUND = 1000


def main():
    n = int(sys.stdin.read())
    p = next((d for d in range(2, isqrt(n) + 1) if n % d == 0), n)
    # the largest gcd is n / p: the pockets hold n/p times parts adding
    # up to p, and the lcm is n/p times the lcm of the parts. Parts that
    # are powers of distinct primes, padded with ones, give the best lcm
    unit = n // p
    sieve = bytearray([1]) * BOUND
    groups = []
    for q in range(2, min(p, BOUND)):
        if sieve[q]:
            sieve[q * q::q] = bytearray(len(sieve[q * q::q]))
            powers = []
            w = q
            while w < p:
                powers.append(w)
                w *= q
            groups.append(powers)
    # best[s]: the largest log of an lcm of parts with weight at most s
    best = [0.0] * (p + 1)
    choices = []
    for powers in groups:
        nxt = best[:]
        choice = bytearray(p + 1)
        for e, w in enumerate(powers, 1):
            value = log(w)
            for s in range(w, p + 1):
                candidate = best[s - w] + value
                if candidate > nxt[s]:
                    nxt[s] = candidate
                    choice[s] = e
        best = nxt
        choices.append(choice)
    parts = []
    s = p
    for powers, choice in zip(reversed(groups), reversed(choices)):
        e = choice[s]
        if e:
            parts.append(powers[e - 1])
            s -= powers[e - 1]
    parts += [1] * (p - sum(parts))
    print(" ".join(str(part * unit) for part in parts))


main()
