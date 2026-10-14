import math


def discrete_log(g, y, p, q):
    """The x in [0, q) with g^x = y modulo p, where g has order q:
    baby steps g^j for j < m, then giant steps y g^(-m i)."""
    m = math.isqrt(q - 1) + 1
    baby = {}
    cur = 1
    for j in range(m):
        baby.setdefault(cur, j)
        cur = cur * g % p
    step = pow(g, (q - m % q) % q, p)  # g^(-m), since g^q = 1
    cur = y % p
    for i in range(m + 1):
        if cur in baby:
            return (i * m + baby[cur]) % q
        cur = cur * step % p
    return None


def main():
    n_bits, l_bits, q, p, g, y, h = (int(v) for v in input().split())
    # the hash is fixed, so the signature needs the secret key x itself
    x = discrete_log(g, y, p, q)
    k = 0
    while True:
        k += 1
        r = pow(g, k, p) % q
        if r == 0:
            continue
        s = pow(k, q - 2, q) * (h + x * r) % q  # q is prime
        if s != 0:
            print(r, s)
            return


main()
