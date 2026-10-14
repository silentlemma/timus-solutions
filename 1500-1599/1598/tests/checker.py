"""Checker: two integers r and s with 0 < r, s < q that pass the DSA check
v = ((g^u1 y^u2) mod p) mod q = r, where w = s^-1, u1 = H w and u2 = r w
modulo q."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    n_bits, l_bits, q, p, g, y, h = (int(v) for v in open(source).read().split())
    got = open(output).read().split()
    if len(got) != 2 or not all(w.isdigit() for w in got):
        fail("expected two integers")
    r, s = (int(w) for w in got)
    if not (0 < r < q and 0 < s < q):
        fail("r or s out of range")
    w = pow(s, q - 2, q)
    u1, u2 = h * w % q, r * w % q
    v = pow(g, u1, p) * pow(y, u2, p) % p % q
    if v != r:
        fail("the signature does not verify")


main()
