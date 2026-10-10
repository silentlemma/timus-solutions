import sys

# n is a product of two odd primes, so trial division starts here
SMALLEST = 3


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    k = next(tok)
    out = []
    for _ in range(k):
        e, n, c = next(tok), next(tok), next(tok)
        p = SMALLEST
        while n % p:
            p += 2
        phi = (p - 1) * (n // p - 1)
        # m^(e d) = m modulo n when e d = 1 modulo phi, so the private
        # exponent d undoes the public one
        d = pow(e, -1, phi)
        out.append(pow(c, d, n))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()
