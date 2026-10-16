import sys


def main():
    n = int(sys.stdin.read())
    primes, exps = [], []
    rest, p = n, 2
    while p * p <= rest:
        if rest % p == 0:
            primes.append(p)
            exps.append(0)
            while rest % p == 0:
                rest //= p
                exps[-1] += 1
        p += 1
    if rest > 1:
        primes.append(rest)
        exps.append(1)
    # a divisor is its exponent vector, numbered in mixed radix: every
    # proper divisor of a divisor gets a smaller number
    radix = [1]
    for e in exps:
        radix.append(radix[-1] * (e + 1))
    count = radix[-1]
    expected = [0.0] * count
    for index in range(count):
        a = [index // radix[i] % (e + 1) for i, e in enumerate(exps)]
        if sum(a) <= 1:
            continue  # 1 or a prime: no gcd is taken
        # gcd(m, r) for a uniform r splits over the primes: the exponent
        # of p in it is b < a with chance (1 - 1/p) / p^b, or a with 1/p^a
        parts = [(0, 1.0)]
        for i, (q, top) in enumerate(zip(primes, a)):
            options = [(b * radix[i], (1 - 1 / q) / q ** b) for b in range(top)]
            options.append((top * radix[i], 1 / q ** top))
            parts = [(o + do, w * dw) for o, w in parts for do, dw in options]
        stay = parts[0][1] + parts[-1][1]  # gcd 1 or the number itself
        total = 1.0
        for offset, chance in parts[1:-1]:
            total += chance * (expected[offset] + expected[index - offset])
        expected[index] = total / (1 - stay)
    print("%.10f" % expected[count - 1])


main()
