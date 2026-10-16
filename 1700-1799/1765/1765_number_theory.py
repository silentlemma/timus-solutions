import sys


def prime_factors(n):
    primes = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            primes.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        primes.append(n)
    return primes


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    broken = [False] * n
    for w in data[2:2 + k]:
        broken[int(w) - 1] = True
    primes = prime_factors(n)
    # a balanced set of tips is a union of disjoint regular p-gons and q-gons,
    # and blades n / (p q) apart form a p by q grid whose rows are the q-gons
    # and whose columns are the p-gons
    p = primes[0]
    q = primes[1] if len(primes) > 1 else 1
    classes = n // (p * q)
    remove = []
    for base in range(classes):
        cells = [base + t * classes for t in range(p * q)]
        bad_rows = {t % p for t, c in enumerate(cells) if broken[c]}
        bad_cols = {t % q for t, c in enumerate(cells) if broken[c]}
        if not bad_rows:
            continue
        # a row and a column always share a cell, so the kept blades are
        # either all clean rows or all clean columns, whichever hold more, and
        # with one prime the rows are single blades that never balance
        by_rows = q > 1 and (p - len(bad_rows)) * q >= (q - len(bad_cols)) * p
        for t, c in enumerate(cells):
            dropped = t % p in bad_rows if by_rows else t % q in bad_cols
            if dropped and not broken[c]:
                remove.append(c + 1)
    if len(remove) + k == n:
        print(-1)
        return
    print(len(remove))
    print(" ".join(map(str, remove)))


main()
